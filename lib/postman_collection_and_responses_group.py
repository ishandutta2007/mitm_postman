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
import re

from mitmproxy import ctx

# HOST_FILTER_PARAM = "host_filter"
COLLECTION_NAME_PARAM = "collection_name"
HOSTGROUP_FILTER_PARAM = "hostgroup_filter"


def load(l):
    # l.add_option(HOST_FILTER_PARAM, str, "example.com", "Host filter option")
    l.add_option(
        COLLECTION_NAME_PARAM, str, "collection_name", "Collection name option"
    )
    l.add_option(
        HOSTGROUP_FILTER_PARAM, str, "hostgroup_filter", "hostgroup filter option"
    )


class Postman:
    def __init__(self):
        self.num = 0
        # self.keywords = ["facebook", "fbcdn", "ip-api", "instagram"]
        self.folder_dict = {}

    def request(self, flow):
        print("hostgroup_filter", ctx.options.hostgroup_filter)
        self.num = self.num + 1
        self.collection = Collection.getInstance(request_no=self.num)
        ctx.log.info("REQUEST NO: %d : %s" % (self.num, flow.request.host))
        is_present = False
        for keyword in ctx.options.hostgroup_filter.split(","):
            if keyword in flow.request.host:
                is_present = True
                break
        if not is_present:
            return
        ctx.log.info(
            "INITATING POSTMAN REQUEST CONSTRUCTION:%s , %s"
            % (flow.request.host, ctx.options.hostgroup_filter)
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

        print("REQUEST DATA:")
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
                folder = Folder(
                    name=folder_name, request_no=self.num, collection=self.collection
                )
                self.collection.add_folder(folder)
                self.folder_dict[folder_name] = folder
            folder.add_request(req)
        self.collection.save_to_file()

    def response(self, flow):
        print("RESPONSE NO:", self.num)
        is_present = False
        for keyword in ctx.options.hostgroup_filter.split(","):
            if keyword in flow.request.host:
                is_present = True
                break
        if not is_present:
            return
        # print(flow.response)
        response = flow.response
        print("response.content:", response.content[:100])
        print("response.cookies:", response.cookies)
        # decode(strict=True)[source]
        # encode(e)[source]
        # get_content(strict: bool = True) → bytes[source]
        # get_text(strict: bool = True) → typing.Union[str, NoneType][source]
        print("response.headers:", response.headers)
        print("response.http_version:", response.http_version)
        print("response.raw_content:", response.raw_content[:100])
        print("response.reason:", response.reason)
        # refresh(now=None)[source]
        # replace(pattern, repl, flags=0, count=0)[source]
        print("response.status_code:", response.status_code)
        print("response.text:", response.text[:100])
        print("response.timestamp_end:", response.timestamp_end)
        print("response.timestamp_start:", response.timestamp_start)
        self.group_of_responses = GroupOfResponses.getInstance(response_no=self.num)
        self.group_of_responses.add_response(response)
        self.group_of_responses.save_to_file()

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
        # print("serialized Collection :", obj)
        return obj

    def save_to_file(self):
        """
        Save Postman collection to file
        :return: None
        """
        obj = self.serialize()
        if not os.path.exists("output/{}/postman_collections/".format(self.name)):
            os.makedirs("output/{}/postman_collections/".format(self.name))

        filename = "{file_name}.json".format(**{"file_name": self.name})
        with open(
            "output/{}/postman_collections/".format(self.name) + "/" + filename, "wt"
        ) as f:
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
            self.id = str(request_no).zfill(5) + "_" + str(uuid.uuid4())
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


class Response(object):
    def __init__(
        self, name, response, response_no=None,
    ):
        """
        A Response object represents a single Postman Response
        :param name: Name of the response
        :param response: URL to send the response
        :param response_no: HTTP method
        """
        print("ResponseResponseResponseResponseResponseResponseRequest:")
        print(object)
        if response_no:
            self.id = str(response_no).zfill(5) + "_" + str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())

        self.name = name
        # self.response = response

        self.content = response.content
        # print("response.content:", self.content)

        self.cookies = response.cookies
        print("response.cookies:", self.cookies)
        # decode(strict=True)[source]
        # encode(e)[source]
        # get_content(strict: bool = True) → bytes[source]
        # get_text(strict: bool = True) → typing.Union[str, NoneType][source]
        self.headers = response.headers
        print("response.headers:", self.headers)

        self.http_version = response.http_version
        print("response.http_version:", self.http_version)

        self.raw_content = response.raw_content
        # print("response.raw_content:", self.raw_content)

        self.reason = response.reason
        print("response.reason:", self.reason)
        # refresh(now=None)[source]
        # replace(pattern, repl, flags=0, count=0)[source]

        self.status_code = response.status_code
        print("response.status_code:", self.status_code)

        self.text = response.text
        # print("response.text:", self.text)

        self.timestamp_end = response.timestamp_end
        print("response.timestamp_end:", self.timestamp_end)

        self.timestamp_start = response.timestamp_start
        print("response.timestamp_start:", self.timestamp_start)

    def serialize(self):
        """
        Serialize Response object
        :return: Response dict
        """
        # headers = {} if self.headers is None else self.headers
        obj = OrderedDict()
        obj["id"] = self.id
        obj["name"] = self.name

        try:
            obj["content"] = self.content.decode("unicode_escape")
        except Exception as e:
            obj["content"] = ""

        try:
            obj["cookies"] = list(self.cookies)
        except Exception as e:
            obj["cookies"] = []

        # obj["headers"] = self.headers
        try:
            obj["headers"] = "".join("%s: %s\n" % kv for kv in self.headers.items())
        except Exception as e:
            obj["headers"] = {}

        try:
            obj["http_version"] = self.http_version
        except Exception as e:
            obj["http_version"] = ""

        try:
            obj["raw_content"] = json.dumps(
                self.raw_content.decode("unicode_escape"), indent=4
            )
        except Exception as e:
            obj["raw_content"] = {}

        try:
            obj["reason"] = self.reason
        except Exception as e:
            obj["reason"] = ""

        try:
            obj["status_code"] = self.status_code
        except Exception as e:
            obj["status_code"] = ""

        try:
            obj["text"] = self.text.decode("unicode_escape")
        except Exception as e:
            obj["text"] = ""

        try:
            obj["timestamp_start"] = self.timestamp_start
        except Exception as e:
            obj["timestamp_start"] = ""

        try:
            obj["timestamp_end"] = self.timestamp_end
        except Exception as e:
            obj["timestamp_end"] = ""

        # if self.data is not None and isinstance(self.data, dict) and not self.is_json:
        #     obj["dataMode"] = "urlencoded"
        #     obj["data"] = [
        #         dict(key=k, value=v, enabled=True, type="text")
        #         for k, v in self.data.items()
        #     ]
        # elif self.data is not None and not self.is_json:
        #     obj["dataMode"] = "raw"
        #     obj["rawModeData"] = str(self.data)
        # elif self.data is not None and self.is_json:
        #     obj["dataMode"] = "raw"
        #     obj["rawModeData"] = json.dumps(self.data, indent=4)
        # if self.description is not None:
        #     obj["descriptionFormat"] = "markdown"
        #     obj["description"] = self.description

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
            self.id = str(request_no).zfill(5) + "_" + str(uuid.uuid4())
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


class GroupOfResponses(object):
    __instance = None

    @staticmethod
    def getInstance(response_no):
        """ Static access method. """
        name = ctx.options.collection_name
        if GroupOfResponses.__instance == None:
            GroupOfResponses(name=ctx.options.collection_name, response_no=response_no)
        return GroupOfResponses.__instance

    def __init__(self, name, response_no, description=None):
        """
        A GroupOfResponses object represents a single postman collection
        :param name: GroupOfResponses name
        :param description: Description for the GroupOfResponses
        """
        # if Collection.__instance == None:
        if GroupOfResponses.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            GroupOfResponses.__instance = self
            self.id = str(uuid.uuid4())
            self.response_no = response_no
            self.name = name
            self._responses = []
            self.description = description
            # print("INITITATLED Collection CLASS WITH NAME:", name)

    # def get_GroupOfResponses_id(self):
    #     :return: GroupOfResponses id
    #     print("FETCHED GroupOfResponses:", self.id)
    #     return self.id

    def add_response(self, response):
        """
        Add request to the GroupOfResponses
        :param request: Request object
        :return: None
        """
        response = Response(self.name, response, response_no=self.response_no)
        self._responses.append(response)
        print("ADDED GroupOfResponses Response")

    def get_all_responses(self):
        """
        Get all requests including those in the folders
        :return: list of Request objects
        """
        responses = list(self._responses)
        print("Before GroupOfResponses responses:", self._responses)
        print("FETCHED GroupOfResponses responses:", responses)
        print("New GroupOfResponses responses:", self._responses)
        # return responses#, key=attrgetter("id"))
        return sorted(responses, key=attrgetter("id"))

    def serialize(self):
        """
        Serialize GroupOfResponses object
        :return: GroupOfResponses dict
        """
        obj = OrderedDict()
        obj["id"] = self.id
        obj["name"] = self.name
        # if self.description is not None:
        #     obj["description"] = self.description
        # obj["order"] = [r.id for r in self.responses]
        responses = self.get_all_responses()
        obj["responses"] = [r.serialize() for r in responses]
        # print("serialized GroupOfResponses :", obj)
        return obj

    def save_to_file(self):
        """
        Save Postman GroupOfResponses to file
        :return: None
        """
        obj = self.serialize()
        if not os.path.exists("output/{}/responses_groups/".format(self.name)):
            os.makedirs("output/{}/responses_groups/".format(self.name))

        filename = "{file_name}.json".format(**{"file_name": self.name})
        try:
            with open(
                "output/{}/responses_groups/".format(self.name) + "/" + filename, "wt",
            ) as f:
                json.dump(obj, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print("ERRRRRRRRRRRRRRR DUMPING RESPONSES")
            print(e)
            s = str(e)  # int(s[57:63])int(s[50:56])
            nums = re.findall(r"\d+", s)
            l = nums[1]  # int(s[50:56])
            print(obj[l - 10 : l + 100])
        print("save GroupOfResponses to file:", self.name)


addons = [Postman()]
