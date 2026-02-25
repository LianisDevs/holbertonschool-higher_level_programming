"""
This is the http_server module

Contains-

HTTPWebServer()
start-server()
"""
import http.server
import socketserver
import json

PORT = 8000


class HTTPWebServer(http.server.BaseHTTPRequestHandler):
    """
    This is the HTTPWebServer class
    Inherits: http.server.BaseHTTPRequestHandler class

    Methods:
    do_GET()
    """
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            json_string = json.dumps("Hello, this is a simple API!")
            self.wfile.write(json_string.encode(encoding="utf_8"))
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            python_obj = {"name": "John", "age": 30, "city": "New York"}
            json_string = json.dumps(python_obj)
            self.wfile.write(json_string.encode(encoding="utf_8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            obj = {"version": "1.0",
                   "description": "A simple API built with http.server"
                   }
            json_string = json.dumps(obj)
            self.wfile.write(json_string.encode(encoding="utf_8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            json_string = json.dumps("Endpoint Not Found")
            self.wfile.write(json_string.encode(encoding="utf_8"))


def start_server():
    """
    This is the start_server() function
    This starts the server
    """
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), HTTPWebServer) as httpd:
        httpd.serve_forever()


start_server()
