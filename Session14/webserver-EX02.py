import http.server
import socketserver
import termcolor
from pathlib import Path


PORT = 8080


socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_get(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')
        if self.path == "/" or self.path == "/index.html":
            contents = Path("index.html").read_text()
            self.send_response(200)
        else:
            contents = Path("Error.html").read_text()
            self.send_response(404)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))
        self.end_headers()
        self.wfile.write(contents.encode())

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()