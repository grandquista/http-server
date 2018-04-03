from http.server import HTTPServer, BaseHTTPRequestHandler
from json import dumps, loads
from urllib.parse import urlparse, parse_qs
from cowpy import cow

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
    COW = cow.Moose()

    def get_index(self, parsed_path):
        """
        Handle `/` path get request.
        """
        self.send_response(200)
        self.end_headers()
        self.wfile.write(INDEX)

    def get_cowsay(self, parsed_path):
        """
        Handle `/cowsay` path get request.
        """
        self.send_response(200)
        self.end_headers()
        self.wfile.write(COWSAY)

    def get_cow(self, parsed_path):
        """
        Handle `/cow[?msg=<message>]` path get request.
        """
        parsed_qs = parse_qs(parsed_path.query)
        msg = parsed_qs.get('msg', 'You should speak up for yourself.')
        self.send_response(200)
        self.end_headers()
        self.wfile.write(self.COW.milk(msg).encode())

    def post_cow(self, parsed_path):
        """
        Handle `/cow[?msg=<message>]` path post request.
        """
        parsed_qs = parse_qs(parsed_path.query)
        msg = parsed_qs.get('msg', 'You should speak up for yourself.')
        self.send_response(200)
        self.end_headers()
        self.wfile.write(dumps({"content": self.COW.milk(msg)}).encode())

    def do_GET(self):
        """
        Dispatch get to known paths or handle 404 status.
        """
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
        """
        Dispatch post to known paths or handle 404 status.
        """
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/cow':
            return self.post_cow(parsed_path)

        self.send_response(404)
        self.end_headers()
        self.wfile.write(b'Not Found')


def create_server():
    """
    Initialize a default server for cowsay.
    """
    return HTTPServer(ADDRESS, SimpleHTTPRequestHandler)


def main():
    """
    Entry point for server application.
    """
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
