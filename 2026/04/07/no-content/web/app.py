from http.server import BaseHTTPRequestHandler, HTTPServer
import os

FLAG = os.environ.get("FLAG", "Alpaca{REDACTED}")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            body = FLAG.encode("utf-8")

            self.send_response(204) # No Content
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", "0") # Make sure there's no content
            self.end_headers()
            self.wfile.write(body) # Oops!
        else:
            self.send_error(404, "Not Found")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 3000), Handler)
    server.serve_forever()