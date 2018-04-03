import json

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from cowpy import main

ADDRESS = ('127.0.0.1', 3000)

INDEX = b'''
<!DOCTYPE html>
<html>
<head>
    <title> cowsay </title>
</head>
<body>
    <header>
        <nav>
        <ul>
            <li><a href="/cowsay">cowsay</a></li>
        </ul>
        </nav>
    <header>
    <main>
        <!-- project description -->
    </main>
</body>
</html>
'''

COWSAY = b'''
<!DOCTYPE html>
<html>
<head>
    <title> cowsay </title>
</head>
<body>
    <header>
        <nav>
        <ul>
            <li><a href="/cow?msg=text">cow?msg=text</a></li>
        </ul>
        </nav>
    <header>
    <main>
        /cow?msg=text
    </main>
</body>
</html>
'''


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def get_index(self, parsed_path):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(INDEX)

    def get_cowsay(self, parsed_path):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(COWSAY)

    def get_cow(self, parsed_path):
        parsed_qs = parse_qs(parsed_path.query)
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

    def post_cow(self, parsed_path):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(COWSAY)

    def do_GET(self):
        parsed_path = urlparse(self.path)

        if parsed_path.path == '/':
            return self.get_index(parsed_path)

        if parsed_path.path == '/cowsay':
            return self.get_cowsay(parsed_path)

        if parsed_path.path == '/cow':
            return self.get_cow(parsed_path)

        self.send_response(404)
        self.end_headers()
        self.wfile.write(b'Not Found')

    def do_POST(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/cow':
            return self.post_cow(parsed_path)

        self.send_response(404)
        self.end_headers()
        self.wfile.write(b'Not Found')


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
