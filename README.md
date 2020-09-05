# MITM Postman

A tool that creates a Postman collection from App / Web API calls

# Setup

Install mitm proxy

```sh
pip3 install mitmproxy
```

Clone mitm_postman

```sh
git clone https://github.com/ishandutta2007/mitm_postman.git
```

```sh
cd mitm_postman
```

The following command does three things 
1)Starts the mitmproxy
2)Ceeates postman Collection
3)Creates response Group
To explain the arguments it filters all urls containing either of instagram or facebook or fbcdn or ip-api and saves the output in a folder named fb5 and collection named fb5

```sh
./mitm instagram,facebook,fbcdn,ip-api fb5
```

Configure the proxy settings on the client (port 9500)

