#!/usr/bin/env python3
"""Simple HTTP logger service.

Accepts POST requests with JSON payloads and appends them to the
file defined by FILE_NAME. Designed for use with the chat widget in
index4.html.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

FILE_NAME = "Data_Bot"
PORT = 8000

class LoggerHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length)
        try:
            payload = json.loads(data.decode('utf-8'))
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            return

        with open(FILE_NAME, 'a', encoding='utf-8') as f:
            f.write(json.dumps(payload) + '\n')

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()


def run():
    server = HTTPServer(('0.0.0.0', PORT), LoggerHandler)
    print(f"Logging server running on port {PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    run()
