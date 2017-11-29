import main
import json
import os
import urllib
import random
import string

from http.server import HTTPServer as BaseHTTPServer, SimpleHTTPRequestHandler

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class WrongInput(Exception):
    def __init__(self, type):
        Exception.__init__(self)
        self.type = type

def transformURL(URL):
    JSONdata = json.loads(urllib.parse.unquote(urllib.parse.unquote(URL)).replace("/xray-1.0/?info=", ""))
    for i in JSONdata:
        info = i.strip().split(" ")
        if len(info) != 2:
            raise WrongInput("Неверный аргумент - " + i)
        yield info

class HTTPHandler(SimpleHTTPRequestHandler):
    """This handler uses server.base_path instead of always using os.getcwd()"""
    def translate_path(self, path):
        path = SimpleHTTPRequestHandler.translate_path(self, path)
        relpath = os.path.relpath(path, os.getcwd())
        fullpath = os.path.join(self.server.base_path, relpath)
        return fullpath

    def do_POST(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        try:
            info = list(transformURL(self.path))
            outinfo = []
            for i in info:
                i[0] = float(i[0])
                i[1] = int(i[1])
                outinfo.append(tuple(i))


            outlist = list(main.find(outinfo))
            outtext = ""
            for i in outlist:
                outtext += i[0] + " " + str(round(i[1], 2)) + " %\n"
            print(outtext)
            self.wfile.write(bytes(outtext.encode('utf-8')))
        except WrongInput as err:
            self.wfile.write(bytes(err.type, "utf8"))
        return


class HTTPServer(BaseHTTPServer):
    """The main server, you pass in base_path which is the path you want to serve requests from"""
    def __init__(self, base_path, server_address, RequestHandlerClass=HTTPHandler):
        self.base_path = base_path
        BaseHTTPServer.__init__(self, server_address, RequestHandlerClass)

web_dir = os.path.join(os.path.dirname(__file__), 'html')
httpd = HTTPServer(web_dir, ("", 8000))
httpd.serve_forever()