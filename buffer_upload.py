import requests

my_encoding = "gzip, deflate, br"
my_language = "en-GB,en-US;q=0.9,en;q=0.8"
my_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3882.0 Safari/537.36"
cfduid_str = "__cfduid=dea031463893bc43ff99146214b8fa4dc1600757097"
buffer_marketing_str = "buffer-marketing=eyJ2aXNpdG9ySWQiOiJiZTAwNmE0Zi1jZTk0LTQ5ODMtYmMyOS1mMDBlMGI1MDQyMzgiLCJ0cmFja2luZyI6eyJyZWZlcnJlciI6Im5vbmUifSwidXRtcyI6eyJ2YWx1ZXMiOnt9LCJ1cGRhdGVkQXQiOjE2MDA3NTcwOTg2Mzh9fQ=="
buffer_marketingsig_str = "buffer-marketing.sig=11OChn2sOFLbPZPYS5d3wHADIEQ"
buffer_signup_str = "buffer-signup=eyJ2aXNpdG9ySWQiOiJiZTAwNmE0Zi1jZTk0LTQ5ODMtYmMyOS1mMDBlMGI1MDQyMzgifQ=="
ajs_anonymous_id = "ajs_anonymous_id=%22be52f79b-f4dc-4c96-9615-a43ef4ac1600%22"
mp_90f7 = "mp_90f73cfa0608e74231d66fdf4f31e120_mixpanel=%7B%22"
device_id = "device_id%22%3A%20%22174b48f13231b4-01237e4325629-623e0a70-fa000-174b48f132469d%22%2C%22"
mp_lib = "mp_lib%22%3A%20%22Segment%3A%20web%22%2C%22%24"
initial_referring_domain = "initial_referring_domain%22%3A%20%22%24direct%22%" + "7D"
fbp = "_fbp=fb.1.1600757110432.775138595"
buffer_session = "buffer_session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uSWQiOiJ2MV81ZDQxMzI1NGJkZDlhYTI2Zjc0NDg2Y2NfMjkxZGRmYjgtOWJhZS00OTliLThlZmYtYmY0M2E3MjAyMTQ3Iiwic2Vzc2lvblZlcnNpb24iOiJ2MSIsImlhdCI6MTYwMDc1NzExNn0.nTUgi-aGm6R-r9XBfYI-H8LUPNn5z-DtkVc6SV39788"
bufferapp_ci_session = "bufferapp_ci_session=b9I9s49vV2QX5x3xuwkYxI4il2d4pBD1NgIn9zdmKKz3BnBB%2Bu8UHcgT30FlOZ%2Fkz38JxjuFDWBmnelw10njM9Ct8iUNv9mXxDtwe1XK1Cnwv8z2BQNgFWLhoPMe1dVYbj4h3VlKXzVQkmVCK%2F34rTyT27oenXPBAEnAd1jV6XeSLCAB4uLYphpkcBqTvOEASSBUKh9Z%2BQ%2FRD5LZ9qAkFwYzeQFVha4iqhwCmbF6wmDBwYHCx6CMeLptrhP62vMZxa2WZ7TKEJ8CTrUN1x5R7baLfTkEDv8mT4k%2FdWX9KxAtMOY2C%2BrDhoWXnjJSGjwNTgFyRCxHYRtEFgH7IapclPgsstwWpk3WAhc06TIYpNT1eCHfC3RWDl4vsFqGvKa5vF7GJmU%2BkNfFqglEDxeopiGhooOoj%2BZzSY2VUcb4ex1tRvdZETGGkOix1eY4RFgpLDUhYaY8WxO%2BYvyubP6GSBNoqICAOCUJktBq2S7DGcJZ4x7j%2FSjICXqbI%2Be%2B%2Fc3mOnghGFek7AXlzckFEw4wwEJCgqZaSCrvoYyhw5AHoeP3L%2BiPH1y%2BLAWktotbpTYnJ5AabjXoKjp44K09NV%2BDPFUBn1l1aH%2FAC3aZ%2F6KoCHcjgoEbtTKhVs9ns6gwXUKP5p8qsNXtFUMpIOwNMh2H%2FW74zwkvCMa9tZOmpaosQazohj4YwQ7zSjg7gng9ntk8XZCFGIJk3p6on4bpylsIpg%3D%3D"
dd_s1 = "_dd_s=rum=0&expire=1600758020615"
dd_s2 = "_dd_s=rum=0&expire=1600758030036"
dd_s3 = "_dd_s=rum=0&expire=1600758111632"

cioid = "_cioid=5d413254bdd9aa26f74486cc"
stripe_mid = "__stripe_mid=90454907-556b-42dd-aee1-921ccb2d64aa6e73ab"
stripe_sid = "__stripe_sid=1bb40d25-187b-458a-85a8-f875d1109d81e2dbcf"
ajs_user_id = "ajs_user_id=%225d413254bdd9aa26f74486cc%22"
cio = "_cio=de1a76aa-e470-92f6-f48c-15d3bac6792a"
iter_id = "iter_id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhaWQiOiI1ZjY5OWRhNWRjNTUxODAwMDE5MDA5N2IiLCJjb21wYW55X2lkIjoiNWQ1ZjIxMzUxMzU5ZDMwMDAxMDE3N2IxIiwiaWF0IjoxNjAwNzU3MTU3fQ.kX6_RhnQua2Uunh6SzgfeQ5-nihQIgKzqSlFlkG5qwk"
initial_referrer = "initial_referrer%22%3A%20%22%24direct%22%2C%22%24"
initial_referring_domain = (
    "initial_referring_domain%22%3A%20%22%24direct%22%" + "2C%22%24"
)
distinct_id = "distinct_id%22%3A%20%225d413254bdd9aa26f74486cc%22%2C%22%24"
distinct_id2 = "distinct_id%22%3A%20%22174b48f13231b4-01237e4325629-623e0a70-fa000-174b48f132469d%22%2C%22%24"
mp_name_tag = "mp_name_tag%22%3A%20%22mandhanasmrithi%40gmail.com%22%2C%22"
productSolutionName = "productSolutionName%22%3A%20null%2C%22id%22%3A%20%225d413254bdd9aa26f74486cc%22%2C%22%24"
user_id = "user_id%22%3A%20%225d413254bdd9aa26f74486cc%22%2C%22"
email = "email%22%3A%20%22mandhanasmrithi%40gmail.com%22%2C%22%24"
first_name = "first_name%22%3A%20%22smrithi.mandhana.fc%22%2C%22%24"
name = "name%22%3A%20%22smrithi.mandhana.fc%22%7D"


def get_login_braking_brand_logo():
    url = "https://static.buffer.com/login/public/img/breaking-brand-logo.svg"
    payload = {}
    headers = {
        "": "authority: static.buffer.com",
        "sec-fetch-mode": "no-cors",
        "user-agent": my_useragent,
        "accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        "sec-fetch-site": "same-site",
        "referer": "https://login.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_login_buffer_logo():
    url = "https://static.buffer.com/login/public/img/buffer-logo.svg"
    payload = {}
    headers = {
        "": "authority: static.buffer.com",
        "sec-fetch-mode": "no-cors",
        "user-agent": my_useragent,
        "accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        "sec-fetch-site": "same-site",
        "referer": "https://login.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_publish_bundle_6_css():
    url = "https://static.buffer.com/publish/bundle.6edd00fd.css"
    payload = {}
    headers = {
        "": "authority: static.buffer.com",
        "sec-fetch-mode": "no-cors",
        "user-agent": my_useragent,
        "accept": "text/css,*/*;q=0.1",
        "sec-fetch-site": "same-site",
        "referer": "https://publish.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_publish_bundle_d_js():
    url = "https://static.buffer.com/publish/bundle.d96486bf.js"
    payload = {}
    headers = {
        "": "authority: static.buffer.com",
        "sec-fetch-mode": "cors",
        "origin": "https://publish.buffer.com",
        "user-agent": my_useragent,
        "accept": "*/*",
        "sec-fetch-site": "same-site",
        "referer": "https://publish.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_publish_vendorf_js():
    url = "https://static.buffer.com/publish/vendor.fdc8bda8.js"
    payload = {}
    headers = {
        "": "authority: static.buffer.com",
        "sec-fetch-mode": "cors",
        "origin": "https://publish.buffer.com",
        "user-agent": my_useragent,
        "accept": "*/*",
        "sec-fetch-site": "same-site",
        "referer": "https://publish.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_publish_0_js():
    url = "https://static.buffer.com/publish/0.74926ce6.js"
    payload = {}
    headers = {
        "": "authority: static.buffer.com",
        "sec-fetch-mode": "no-cors",
        "user-agent": my_useragent,
        "accept": "*/*",
        "sec-fetch-site": "same-site",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + ajs_user_id
        + "; "
        + mp_90f7
        + distinct_id
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + user_id
        + mp_name_tag
        + productSolutionName
        + email
        + first_name
        + name
        + "; "
        + cioid,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_publish_composer_2_css():
    url = "https://static.buffer.com/publish/composer.20a28bcd.css"
    payload = {}
    headers = {
        "": "authority: static.buffer.com",
        "sec-fetch-mode": "no-cors",
        "user-agent": my_useragent,
        "accept": "text/css,*/*;q=0.1",
        "sec-fetch-site": "same-site",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + ajs_user_id
        + "; "
        + mp_90f7
        + distinct_id
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + user_id
        + mp_name_tag
        + productSolutionName
        + email
        + first_name
        + name
        + "; "
        + cioid,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_publish_composer_f_js():
    url = "https://static.buffer.com/publish/composer.f1f1e798.js"
    payload = {}
    headers = {
        "": "authority: static.buffer.com",
        "sec-fetch-mode": "no-cors",
        "user-agent": my_useragent,
        "accept": "*/*",
        "sec-fetch-site": "same-site",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + ajs_user_id
        + "; "
        + mp_90f7
        + distinct_id
        + device_id
        + "mp_lib%22%3A%20%22Segment%3A%20web%22%2C%22%24"
        + initial_referrer
        + initial_referring_domain
        + user_id
        + mp_name_tag
        + productSolutionName
        + email
        + first_name
        + name
        + "; "
        + cioid,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_buffer_icons():
    url = "https://icons.buffer.com/0.16.4/buffer-icons.css"
    payload = {}
    headers = {
        "": "authority: icons.buffer.com",
        "sec-fetch-mode": "no-cors",
        "user-agent": my_useragent,
        "accept": "text/css,*/*;q=0.1",
        "sec-fetch-site": "same-site",
        "referer": "https://publish.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_webfonts_buffer_icons():
    url = "https://icons.buffer.com/0.16.4/webfonts/buffer-icons.woff?372676aab1a5bc21bfe6f82fd95bc84a"
    payload = {}
    headers = {
        "": "authority: icons.buffer.com",
        "sec-fetch-mode": "cors",
        "origin": "https://publish.buffer.com",
        "user-agent": my_useragent,
        "accept": "*/*",
        "sec-fetch-site": "same-site",
        "referer": "https://icons.buffer.com/0.16.4/buffer-icons.css",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_v1ToV2UpgradeDetails():
    url = "https://publish.buffer.com/rpc/v1ToV2UpgradeDetails"
    payload = "args=%7B%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "13",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_environment():
    url = "https://publish.buffer.com/rpc/environment"
    payload = "args=%7B%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "13",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_clientAccess():
    url = "https://publish.buffer.com/rpc/clientAccess"
    payload = "args=%7B%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "13",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_profiles():
    url = "https://publish.buffer.com/rpc/profiles"
    payload = "args=%7B%22forAnalyze%22%3Afalse%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "33",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_getGlobalOrganizationId():
    url = "https://publish.buffer.com/rpc/getGlobalOrganizationId"
    payload = "args=%7B%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "13",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_organizations():
    url = "https://publish.buffer.com/rpc/organizations"
    payload = "args=%7B%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "13",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_user():
    url = "https://publish.buffer.com/rpc/user"
    payload = "args=%7B%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "13",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_getCounts():
    url = "https://publish.buffer.com/rpc/getCounts"
    payload = "args=%7B%22profileId%22%3A%225d60f84034f95b18092d9172%22%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "55",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5d60f84034f95b18092d9172/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_getLinkShortener():
    url = "https://publish.buffer.com/rpc/getLinkShortener"
    payload = "args=%7B%22profileId%22%3A%225d60f84034f95b18092d9172%22%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "55",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5d60f84034f95b18092d9172/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_getHashtagGroups():
    url = "https://publish.buffer.com/rpc/getHashtagGroups"
    payload = "args=%7B%22organizationId%22%3A%225d4132550ca715734f7d5936%22%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "60",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5d60f84034f95b18092d9172/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_checkRemindersStatus():
    url = "https://publish.buffer.com/rpc/checkRemindersStatus"
    payload = "args=%7B%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "13",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_globalAccount():
    url = "https://publish.buffer.com/rpc/globalAccount"
    payload = "args=%7B%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "13",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5d60f84034f95b18092d9172/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_queuedPosts():
    url = "https://publish.buffer.com/rpc/queuedPosts"
    payload = "args=%7B%22profileId%22%3A%225d60f84034f95b18092d9172%22%2C%22isFetchingMore%22%3Afalse%2C%22count%22%3A300%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "94",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5d60f84034f95b18092d9172/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_getStoryGroups():
    url = "https://publish.buffer.com/rpc/getStoryGroups"
    payload = "args=%7B%22profileId%22%3A%225d60f84034f95b18092d9172%22%2C%22isFetchingMore%22%3Afalse%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "80",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5d60f84034f95b18092d9172/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_getStoryGroups():
    url = "https://publish.buffer.com/rpc/getStoryGroups"
    payload = "args=%7B%22profileId%22%3A%225e3ce9067741b0698b6680e2%22%2C%22isFetchingMore%22%3Afalse%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "80",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + "; "
        + dd_s2,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_enabledApplicationModes():
    url = "https://publish.buffer.com/rpc/enabledApplicationModes"
    payload = "args=%7B%22comprehensive%22%3Atrue%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "35",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5d60f84034f95b18092d9172/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_getLinkShortener():
    url = "https://publish.buffer.com/rpc/getLinkShortener"
    payload = "args=%7B%22profileId%22%3A%225e3ce9067741b0698b6680e2%22%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "55",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + "; "
        + dd_s2,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_queuedPosts():
    url = "https://publish.buffer.com/rpc/queuedPosts"
    payload = "args=%7B%22profileId%22%3A%225e3ce9067741b0698b6680e2%22%2C%22isFetchingMore%22%3Afalse%2C%22count%22%3A300%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "94",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + "; "
        + dd_s2,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_getCounts():
    url = "https://publish.buffer.com/rpc/getCounts"
    payload = "args=%7B%22profileId%22%3A%225e3ce9067741b0698b6680e2%22%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "55",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + "; "
        + dd_s2,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_getHashtagGroups():
    url = "https://publish.buffer.com/rpc/getHashtagGroups"
    payload = "args=%7B%22organizationId%22%3A%225d4132550ca715734f7d5936%22%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "60",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + "; "
        + dd_s2,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_gridPosts():
    url = "https://publish.buffer.com/rpc/gridPosts"
    payload = "args=%7B%22profileId%22%3A%225e3ce9067741b0698b6680e2%22%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "55",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + "; "
        + dd_s2,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_composerApiProxy3():
    url = "https://publish.buffer.com/rpc/composerApiProxy"
    payload = "args=%7B%22url%22%3A%22/1/profiles/5e3ce9067741b0698b6680e2/schedules/slots.json%22%2C%22args%22%3A%7B%22start_day%22%3A%222020-09-01%22%2C%22end_day%22%3A%222020-09-30%22%7D%2C%22HTTPMethod%22%3A%22GET%22%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "172",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + ajs_user_id
        + "; "
        + mp_90f7
        + distinct_id
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + user_id
        + mp_name_tag
        + productSolutionName
        + email
        + first_name
        + name
        + "; "
        + cioid
        + "; "
        + stripe_mid
        + "; "
        + stripe_sid
        + "; "
        + "_dd_s=rum=0&expire=1600758042012",
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_composerApiProxy2():
    url = "https://publish.buffer.com/rpc/composerApiProxy"
    payload = "args=%7B%22url%22%3A%22/i/upload_image.json%22%2C%22args%22%3A%7B%22key%22%3A%225d4132550ca715734f7d5935/uploads/1600757188961-18_smriti_18_100952172_659976514851291_6579743220330684928_n.jpg%22%2C%22csrf_token%22%3A%221234%22%7D%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "204",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + ajs_user_id
        + "; "
        + mp_90f7
        + distinct_id
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + user_id
        + mp_name_tag
        + productSolutionName
        + email
        + first_name
        + name
        + "; "
        + cioid
        + "; "
        + stripe_mid
        + "; "
        + stripe_sid
        + "; "
        + iter_id
        + "; "
        + "_dd_s=rum=0&expire=1600758085103",
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_composerApiProxy():
    url = "https://publish.buffer.com/rpc/composerApiProxy"
    payload = "args=%7B%22url%22%3A%22/1/updates/create.json%22%2C%22args%22%3A%7B%22now%22%3Afalse%2C%22top%22%3Afalse%2C%22is_draft%22%3Afalse%2C%22shorten%22%3Atrue%2C%22text%22%3A%22Hello%22%2C%22fb_text%22%3A%22%22%2C%22entities%22%3Anull%2C%22profile_ids%22%3A%5B%225e3ce9067741b0698b6680e2%22%5D%2C%22attachment%22%3Afalse%2C%22via%22%3Anull%2C%22source%22%3Anull%2C%22version%22%3Anull%2C%22scheduled_at%22%3A1600758360%2C%22pinned%22%3Atrue%2C%22service_geolocation_id%22%3Anull%2C%22service_geolocation_name%22%3Anull%2C%22service_user_tags%22%3Anull%2C%22media%22%3A%7B%22progress%22%3A100%2C%22uploaded%22%3Atrue%2C%22photo%22%3A%22https%3A//buffer-media-uploads.s3.amazonaws.com/5d4132550ca715734f7d5935/5f699dcc52289e6e4478a2a4/28517b70d3c8fcb81d582b331d3f94ba.original.jpg%22%2C%22picture%22%3A%22https%3A//buffer-media-uploads.s3.amazonaws.com/5d4132550ca715734f7d5935/5f699dcc52289e6e4478a2a4/28517b70d3c8fcb81d582b331d3f94ba.original.jpg%22%2C%22thumbnail%22%3A%22https%3A//buffer-media-uploads.s3.amazonaws.com/5d4132550ca715734f7d5935/5f699dcc52289e6e4478a2a4/28517b70d3c8fcb81d582b331d3f94ba.original.jpg%22%2C%22alt_text%22%3Anull%7D%7D%2C%22HTTPMethod%22%3A%22POST%22%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "990",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + ajs_user_id
        + "; "
        + mp_90f7
        + distinct_id
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + user_id
        + mp_name_tag
        + productSolutionName
        + email
        + first_name
        + name
        + "; "
        + cioid
        + "; "
        + stripe_mid
        + "; "
        + stripe_sid
        + "; "
        + iter_id
        + "; "
        + dd_s3,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_queuedPosts():
    url = "https://publish.buffer.com/rpc/queuedPosts"
    payload = "args=%7B%22profileId%22%3A%225e3ce9067741b0698b6680e2%22%2C%22isFetchingMore%22%3Afalse%2C%22hideLoading%22%3Atrue%2C%22count%22%3A300%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "115",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + ajs_user_id
        + "; "
        + mp_90f7
        + distinct_id
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + user_id
        + mp_name_tag
        + productSolutionName
        + email
        + first_name
        + name
        + "; "
        + cioid
        + "; "
        + stripe_mid
        + "; "
        + stripe_sid
        + "; "
        + iter_id
        + "; "
        + "_dd_s=rum=0&expire=1600758111632",
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_rpc_gridPosts():
    url = "https://publish.buffer.com/rpc/gridPosts"
    payload = "args=%7B%22profileId%22%3A%225e3ce9067741b0698b6680e2%22%7D"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "55",
        "accept": "application/json",
        "user-agent": my_useragent,
        "sec-fetch-mode": "cors",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + ajs_user_id
        + "; "
        + mp_90f7
        + distinct_id
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + user_id
        + mp_name_tag
        + productSolutionName
        + email
        + first_name
        + name
        + "; "
        + cioid
        + "; "
        + stripe_mid
        + "; "
        + stripe_sid
        + "; "
        + iter_id
        + "; "
        + dd_s3,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_static_buffer_avatar32():
    url = "https://static.buffer.com/ui/avatar-mask-32.svg"
    payload = {}
    headers = {
        "": "authority: static.buffer.com",
        "sec-fetch-mode": "no-cors",
        "user-agent": my_useragent,
        "accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        "sec-fetch-site": "same-site",
        "referer": "https://publish.buffer.com/",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + mp_90f7
        + distinct_id2
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_s3_bufferui_defaultavatar():
    url = "https://s3.amazonaws.com/buffer-ui/Default+Avatar.png"
    payload = {}
    headers = {
        "Host": "s3.amazonaws.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Mode": "no-cors",
        "User-Agent": my_useragent,
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        "Sec-Fetch-Site": "cross-site",
        "Referer": "https://publish.buffer.com/",
        "Accept-Encoding": my_encoding,
        "Accept-Language": my_language,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_pusher_app_n1():
    url = "https://ws.pusherapp.com/app/bd9ba9324ece3341976e?protocol=7&client=js&version=4.1.0&flash=false"
    payload = {}
    headers = {
        "Host": "ws.pusherapp.com",
        "Connection": "Upgrade",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "User-Agent": my_useragent,
        "Upgrade": "websocket",
        "Origin": "https://publish.buffer.com",
        "Sec-WebSocket-Version": "13",
        "Accept-Encoding": my_encoding,
        "Accept-Language": my_language,
        "Sec-WebSocket-Key": "3vMO5Vp3qJoNAsc+3Ml/9g==",
        "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_pusher_auth4():
    url = "https://publish.buffer.com/pusher/auth"
    payload = "socket_id=299572.710297&channel_name=private-updates-org-5ed4bdb81423dd88c39e8392"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "81",
        "sec-fetch-mode": "cors",
        "user-agent": my_useragent,
        "content-type": "application/x-www-form-urlencoded",
        "accept": "*/*",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s2
        + "; "
        + ajs_user_id
        + "; "
        + mp_90f7
        + distinct_id
        + device_id
        + mp_lib
        + initial_referrer
        + "initial_referring_domain%22%3A%20%22%24direct%22%"
        + "2C%22%24"
        + user_id
        + mp_name_tag
        + productSolutionName
        + email
        + first_name
        + name
        + "; "
        + cioid,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_pusher_auth3():
    url = "https://publish.buffer.com/pusher/auth"
    payload = (
        "socket_id=299572.710297&channel_name=private-updates-5d60f84034f95b18092d9172"
    )
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "77",
        "sec-fetch-mode": "cors",
        "user-agent": my_useragent,
        "content-type": "application/x-www-form-urlencoded",
        "accept": "*/*",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s2
        + "; "
        + ajs_user_id
        + "; "
        + mp_90f7
        + distinct_id
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + user_id
        + mp_name_tag
        + productSolutionName
        + email
        + first_name
        + name
        + "; "
        + cioid,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_pusher_auth2():
    url = "https://publish.buffer.com/pusher/auth"
    payload = (
        "socket_id=299572.710297&channel_name=private-updates-5e3ce9067741b0698b6680e2"
    )
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "77",
        "sec-fetch-mode": "cors",
        "user-agent": my_useragent,
        "content-type": "application/x-www-form-urlencoded",
        "accept": "*/*",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s2
        + "; "
        + ajs_user_id
        + "; "
        + mp_90f7
        + distinct_id
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + user_id
        + mp_name_tag
        + productSolutionName
        + email
        + first_name
        + name
        + "; "
        + cioid,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def post_publish_pusher_auth():
    url = "https://publish.buffer.com/pusher/auth"
    payload = "socket_id=299572.710297&channel_name=private-story-groups-5e3ce9067741b0698b6680e2"
    headers = {
        "": "authority: publish.buffer.com",
        "content-length": "82",
        "sec-fetch-mode": "cors",
        "user-agent": my_useragent,
        "content-type": "application/x-www-form-urlencoded",
        "accept": "*/*",
        "origin": "https://publish.buffer.com",
        "sec-fetch-site": "same-origin",
        "referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "accept-encoding": my_encoding,
        "accept-language": my_language,
        "cookie": cfduid_str
        + "; "
        + buffer_marketing_str
        + "; "
        + buffer_marketingsig_str
        + "; "
        + buffer_signup_str
        + "; "
        + ajs_anonymous_id
        + "; "
        + cio
        + "; "
        + fbp
        + "; "
        + buffer_session
        + "; "
        + bufferapp_ci_session
        + "; "
        + dd_s2
        + "; "
        + ajs_user_id
        + "; "
        + mp_90f7
        + distinct_id
        + device_id
        + mp_lib
        + initial_referrer
        + initial_referring_domain
        + user_id
        + mp_name_tag
        + productSolutionName
        + email
        + first_name
        + name
        + "; "
        + cioid,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_aws_publish_dragplaceholder():
    url = "https://s3.amazonaws.com/buffer-publish/images/drag-placeholder.png"
    payload = {}
    headers = {
        "Host": "s3.amazonaws.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Mode": "no-cors",
        "User-Agent": my_useragent,
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        "Sec-Fetch-Site": "cross-site",
        "Referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "Accept-Encoding": my_encoding,
        "Accept-Language": my_language,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_buffer_s3_upload_n4_n5():
    url = "https://buffer-media-uploads.s3.amazonaws.com/5f6997a152a6b316cd105ef2/a3ffbd36fd4474644ca57a09f85ac6fce104f018_a390ab3a73567756c033c63941527818a62b29db_instagram"
    payload = {}
    headers = {
        "Host": "buffer-media-uploads.s3.amazonaws.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Mode": "no-cors",
        "User-Agent": my_useragent,
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        "Sec-Fetch-Site": "cross-site",
        "Referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "Accept-Encoding": my_encoding,
        "Accept-Language": my_language,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_stats_pusher():
    url = "https://stats.pusher.com/timeline/v2/jsonp/1?session=MzY0MTE0MTQ1&bundle=MQ%3D%3D&key=YmQ5YmE5MzI0ZWNlMzM0MTk3NmU%3D&lib=anM%3D&version=NC4xLjA%3D&features=WyJ3cyJd&timeline=W3siaW5zdGFuY2VzIjoxLCJ0aW1lc3RhbXAiOjE2MDA3NTcxMjY5NTl9LHsic3RhdGUiOiJjb25uZWN0aW5nIiwidGltZXN0YW1wIjoxNjAwNzU3MTI2OTYwfSx7ImNpZCI6MSwidHJhbnNwb3J0Ijoid3NzIiwidGltZXN0YW1wIjoxNjAwNzU3MTI2OTYyfSx7ImNpZCI6MSwic3RhdGUiOiJpbml0aWFsaXplZCIsInRpbWVzdGFtcCI6MTYwMDc1NzEyNjk2Mn0seyJjaWQiOjEsInN0YXRlIjoiY29ubmVjdGluZyIsInRpbWVzdGFtcCI6MTYwMDc1NzEyNjk2Nn0seyJjaWQiOjIsInRyYW5zcG9ydCI6Inhocl9zdHJlYW1pbmdzIiwidGltZXN0YW1wIjoxNjAwNzU3MTI4OTY4fSx7ImNpZCI6Miwic3RhdGUiOiJpbml0aWFsaXplZCIsInRpbWVzdGFtcCI6MTYwMDc1NzEyODk2OH0seyJjaWQiOjIsInN0YXRlIjoiY29ubmVjdGluZyIsInRpbWVzdGFtcCI6MTYwMDc1NzEyODk3Mn0seyJjaWQiOjEsInN0YXRlIjoib3BlbiIsInRpbWVzdGFtcCI6MTYwMDc1NzEzMDg0Mn0seyJjaWQiOjIsInN0YXRlIjoiY2xvc2VkIiwicGFyYW1zIjp7Indhc0NsZWFuIjp0cnVlfSwidGltZXN0YW1wIjoxNjAwNzU3MTMwODU3fSx7InN0YXRlIjoiY29ubmVjdGVkIiwicGFyYW1zIjp7InNvY2tldF9pZCI6IjI5OTU3Mi43MTAyOTcifSwidGltZXN0YW1wIjoxNjAwNzU3MTMwODU5fV0%3D"
    payload = {}
    headers = {
        "Host": "stats.pusher.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Mode": "no-cors",
        "User-Agent": my_useragent,
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "Accept-Encoding": my_encoding,
        "Accept-Language": my_language,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))


def get_buffer_s3_upload_n1_n2_n3():
    url = "https://buffer-media-uploads.s3.amazonaws.com/5d4132550ca715734f7d5935/5f699dcc52289e6e4478a2a4/28517b70d3c8fcb81d582b331d3f94ba.original.jpg"
    payload = {}
    headers = {
        "Host": "buffer-media-uploads.s3.amazonaws.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Mode": "no-cors",
        "User-Agent": my_useragent,
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        "Sec-Fetch-Site": "cross-site",
        "Referer": "https://publish.buffer.com/profile/5e3ce9067741b0698b6680e2/tab/queue",
        "Accept-Encoding": my_encoding,
        "Accept-Language": my_language,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode("utf8"))
