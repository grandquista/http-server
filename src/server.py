import json

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

ADDRESS = ('127.0.0.1', 3000)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.send_response(200)
            self.end_headers()

            self.wfile.write(b'You did a thing!')
            return

        elif parsed_path.path == '/test':
            try:
                cat = json.loads(parsed_qs['category'][0])
            except KeyError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'You did a bad thing')
                return

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'we did the thing with the qs')
            return

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.send_response_only()


def create_server():
    return HTTPServer(ADDRESS, SimpleHTTPRequestHandler)


def main():
    with create_server() as server:
        print(f'Starting server on port { ADDRESS[1] }')
        server.serve_forever()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print(f'Stopping server on port { ADDRESS[1] }')
