from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Rule 1: The Homepage
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))
            
        # Rule 2: The Data Endpoint (Aligned perfectly under 'if')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            sample_dataset = {"name": "John", "age": 30, "city": "New York"}
            json_string = json.dumps(sample_dataset)
            self.wfile.write(json_string.encode('utf-8'))
            
        # Rule 3: The Status Endpoint (Aligned perfectly under 'elif')
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))
            
        # Rule 4: The Catch-All 404 (Aligned perfectly at the bottom)
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write("Endpoint not found".encode('utf-8'))

# The Engine: Pushed all the way to the far left wall
if __name__ == '__main__':
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Server running on http://localhost:8000...")
    httpd.serve_forever()
