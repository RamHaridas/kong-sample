import json, os

def handle(req):
    # read headers and query parameters
    query_param = os.getenv("Http_Query","") # reading query params
    header = os.getenv("Http_Test","") # reading header
    header2 = os.getenv("Http_Test2","") # reading header 2
    res = {
        "queryString":query_param,
        "headers":{
            "Test":header,
            "Test2":header2
        },
        "request_body":req
    }
    return json.dumps(res)

    
