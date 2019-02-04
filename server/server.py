import http.server
import socketserver
import os

class Node:

    def __init__(self):
        self.PORT = 8080
        self.Handler = http.server.SimpleHTTPRequestHandler
        return None

    def start(self):
        web_dir = os.path.join(os.path.dirname(__file__), '')
        os.chdir(web_dir)
        with socketserver.TCPServer(("", self.PORT), self.Handler) as httpd:
            print("serving at port", self.PORT)
            httpd.serve_forever()
