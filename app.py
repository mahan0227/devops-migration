from http.server import BaseHTTPRequestHandler, HTTPServer


def greeting() -> str:
    return "Hello from my first DevOps pipeline!"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = greeting().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):  # keep container logs quiet
        return


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
