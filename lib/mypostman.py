"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
from collections import OrderedDict
import os
import json
from operator import attrgetter
import uuid
import argparse
from urllib.parse import urlencode

from mitmproxy import ctx

HOST_FILTER_PARAM = "host_filter"
COLLECTION_NAME_PARAM = "collection_name"


def load(l):
    l.add_option(HOST_FILTER_PARAM, str, "example.com", "Host filter option")
    l.add_option(
        COLLECTION_NAME_PARAM, str, "collection_name", "Collection name option"
    )


class Postman:
    def __init__(self):
        self.num = 0
        self.keywords = ["facebook", "fbcdn"]
        self.folder_dict = {}

    def request(self, flow):
        self.num = self.num + 1
        self.collection = Collection.getInstance(request_no=self.num)
        ctx.log.info("REQUEST NO: %d : %s" % (self.num, flow.request.host))
        is_present = False
        for keyword in self.keywords:
            if keyword in flow.request.host:
                is_present = True
                break
        if not is_present:
            return
        ctx.log.info(
            "INITATING POSTMAN REQUEST CONSTRUCTION:%s , %s"
            % (flow.request.host, ctx.options.host_filter)
        )
        headers = {}
        for k, v in flow.request.headers.items():
            if k != "Content-Length":
                headers[k] = v
        content = flow.request.content
        if content:
            content = content.decode("utf-8")
        print(
            "{url} ({method})".format(
                **{"url": flow.request.url, "method": flow.request.method}
            )
        )
        data = None
        is_json = False
        path = self.get_path(flow.request)
        try:
            content = json.loads(content)
        except Exception:
            pass
        if flow.request.method in ["POST", "PUT"]:
            data = content
            if "form-urlencoded" in headers.get("Content-Type", ""):
                try:
                    data = {x.split("=")[0]: x.split("=")[1] for x in data.split("&")}
                except Exception:
                    pass
            elif "json" in headers.get("Content-Type", ""):
                is_json = True

        print("DATA:")
        print(data)
        req = Request(
            name=path,
            url=flow.request.url,
            method=flow.request.method,
            headers=headers,
            data=data,
            is_json=is_json,
            request_no=self.num,
            description=None,
            parent=None,
        )
        add_to_folder = False
        folder_name = ""
        if path and path != "/":
            if path[0] == "/":
                path = list(path)
                path[0] = ""
                path = "".join(path)
            sub_path = path.split("/")
            if len(sub_path) > 1:
                add_to_folder = True
                folder_name = sub_path[0]
        if not add_to_folder:
            self.collection.add_request(req)
        else:
            if self.folder_dict.get(folder_name):
                folder = self.folder_dict.get(folder_name)
            else:
                folder = Folder(name=folder_name, request_no=self.num, collection=self.collection)
                self.collection.add_folder(folder)
                self.folder_dict[folder_name] = folder
            folder.add_request(req)
        self.collection.save_to_file()

    @staticmethod
    def get_path(req):
        """
        Get path of the domain
        :param req: HTTPRequest object
        :return: domain path
        """
        path = req.path
        if "?" in req.path:
            path = req.path[: req.path.find("?")]
        return path


class Collection(object):
    __instance = None

    @staticmethod
    def getInstance(request_no):
        """ Static access method. """
        name = ctx.options.collection_name
        if Collection.__instance == None:
            Collection(name=ctx.options.collection_name, request_no=request_no)
        return Collection.__instance

    def __init__(self, name, request_no, description=None):
        """
        A Collection object represents a single postman collection
        :param name: Collection name
        :param description: Description for the collection
        """
        # if Collection.__instance == None:
        if Collection.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Collection.__instance = self
            self.id = str(uuid.uuid4())
            self.request_no = request_no
            self.name = name
            self._requests = []
            self._folders = []
            self.description = description
            # print("INITITATLED Collection CLASS WITH NAME:", name)

    def get_collection_id(self):
        """
        :return: collection id
        """
        print("FETCHED Collection:", self.id)
        return self.id

    def add_request(self, request):
        """
        Add request to the collection
        :param request: Request object
        :return: None
        """
        request._parent = self
        self._requests.append(request)
        print("ADDED Collection Request")

    def add_folder(self, folder):
        """
        Add folder to the collection
        :param folder: Folder object
        :return: None
        """
        print("Existing Folders", self._folders)
        print("ADDED Folder", folder)
        self._folders.append(folder)
        folder._collection = self
        print("Now Folders", self._folders)

    def get_all_requests(self):
        """
        Get all requests including those in the folders
        :return: list of Request objects
        """
        requests = list(self._requests)
        print("Before Collection requests:", self._requests)
        print("FETCHED Collection requests:", requests)
        for f in self._folders:
            requests.extend(f._requests)
        print("New Collection requests:", self._requests)
        return sorted(requests, key=attrgetter("id"))

    def serialize(self):
        """
        Serialize Collection object
        :return: Collection dict
        """
        obj = OrderedDict()
        obj["id"] = self.id
        obj["name"] = self.name
        if self.description is not None:
            obj["description"] = self.description
        obj["order"] = [r.id for r in self._requests]
        obj["folders"] = [
            f.serialize() for f in sorted(self._folders, key=attrgetter("id"))
        ]
        requests = self.get_all_requests()
        obj["requests"] = [r.serialize() for r in requests]
        print("serialized Collection :", obj)
        return obj

    def save_to_file(self):
        """
        Save Postman collection to file
        :return: None
        """
        obj = self.serialize()
        if not os.path.exists("output/" + self.name):
            os.makedirs("output/" + self.name)

        filename = "{file_name}.json".format(**{"file_name": self.name})
        with open("output/" + self.name + filename, "wt") as f:
            json.dump(obj, f, indent=4, ensure_ascii=False)
        print("save Collection to file:", self.name)


class Request(object):
    def __init__(
        self,
        name,
        url,
        method=None,
        headers=None,
        data=None,
        is_json=False,
        request_no=None,
        description=None,
        parent=None,
    ):
        """
        A Request object represents a single Postman Request
        :param name: Name of the request
        :param url: URL to send the request
        :param method: HTTP method
        :param headers: Headers dict
        :param data: Body of the request
        :param is_json: Whether data is a json
        :param description: Description for the request
        """
        print("RequestRequestRequestRequestRequestRequestRequest:")
        print(object)
        if request_no:
            self.id = str(request_no).zfill(4) + "_" + str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())

        self.name = name
        self.url = url
        self.method = method
        self.headers = headers
        self.data = data
        self.is_json = is_json
        self.description = description
        self._parent = parent

    def set_parent(self, parent):
        """
        Set a parent for the Request object
        :param parent: Collection or Folder object
        :return: None
        """
        self._parent = parent

    def serialize(self):
        """
        Serialize Request object
        :return: Request dict
        """
        headers = {} if self.headers is None else self.headers
        obj = OrderedDict()
        obj["id"] = self.id
        obj["name"] = self.name
        obj["url"] = self.url
        obj["method"] = self.method
        if self.data is not None and isinstance(self.data, dict) and not self.is_json:
            obj["dataMode"] = "urlencoded"
            obj["data"] = [
                dict(key=k, value=v, enabled=True, type="text")
                for k, v in self.data.items()
            ]
        elif self.data is not None and not self.is_json:
            obj["dataMode"] = "raw"
            obj["rawModeData"] = str(self.data)
        elif self.data is not None and self.is_json:
            obj["dataMode"] = "raw"
            obj["rawModeData"] = json.dumps(self.data, indent=4)
        obj["headers"] = "".join("%s: %s\n" % kv for kv in headers.items())
        if self.description is not None:
            obj["descriptionFormat"] = "markdown"
            obj["description"] = self.description
        if self._parent is not None:
            obj["collectionId"] = self._parent.get_collection_id()
        if isinstance(self._parent, Folder):
            obj["folder"] = self._parent.id
        return obj


class Folder(object):
    def __init__(self, name, request_no, collection=None):
        """
        A Folder object represents a single Postman folder
        :param name: Name of the folder
        :param collection: Collection object (collection to which the folder belongs)
        """
        print("FolderFolderFolderFolderFolderFolderFolder:")
        print(object)
        if request_no:
            self.id = str(request_no).zfill(4) + "_" + str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
        self.name = name
        self.order = []
        self._requests = []
        self._collection = collection

    def get_collection_id(self):
        """
        Get the id of the collection to which the folder belongs
        :return: collection id
        """
        return self._collection.id

    def add_request(self, request):
        """
        Add Request to the Folder
        :param request: Request object
        :return: None
        """
        request._parent = self
        self._requests.append(request)

    def serialize(self):
        """
        Serialize Folder object
        :return: Folder dict
        """
        obj = OrderedDict()
        obj["id"] = self.id
        obj["name"] = self.name
        obj["order"] = [r.id for r in self._requests]
        return obj


addons = [Postman()]
