#!/usr/bin/env python3
import http.server
import socketserver
import sys

# Find a free port
def find_free_port():
    for port in range(8000, 8010):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                s.close()
                return port
        except OSError:
            continue
    return None

# Find free port and start server
port = find_free_port()
if port is None:
    port = 8000  # fallback

print(f"Starting server on http://localhost:{port}")

server = http.server.HTTPServer(('localhost', port), http.server.SimpleHTTPRequestHandler)
print(f"Server running at http://localhost:{port}")
server.serve_forever()
