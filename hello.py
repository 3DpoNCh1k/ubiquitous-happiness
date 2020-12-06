from pprint import pprint


def app(environ, start_response):
    # pprint(environ)
    # print(type(environ))
    # print(start_response)
    # print(type(start_response))
    data = "\n".join(environ["QUERY_STRING"].split("&"))
    # print(data)
    data = data.encode()
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        # ("Content-Length", str(len(data)))
    ])
    return iter([data])
