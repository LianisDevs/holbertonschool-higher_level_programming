"""
This is the http_server module

Contains-

HTTPWebServer()
start-server()
"""
import http.server
import socketserver
import time
import json
import os

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
            self.end_headers()
            string = "Hello, this is a simple API!"
            self.wfile.write(string.encode(encoding="utf_8"))

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            python_obj = {"name": "John", "age": 30, "city": "New York"}
            json_string = json.dumps(python_obj)
            self.wfile.write(json_string.encode(encoding="utf_8"))

        elif self.path == "/status":
            self.send_response(200)
            self.end_headers()
            string = "OK"
            self.wfile.write(string.encode(encoding="utf_8"))

        else:
            self.send_response(404)
            self.end_headers()
            string = "Endpoint not found"
            self.wfile.write(string.encode(encoding="utf_8"))


def start_server():
    """
    This is the start_server() function
    This starts the server
    """
    os.system('clear')
    time.sleep(1)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), HTTPWebServer) as httpd:
        httpd.serve_forever()


start_server()
