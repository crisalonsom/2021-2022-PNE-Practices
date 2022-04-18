import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs


PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_get(self):

        termcolor.cprint(self.requestline, 'green')

        if self.path == "/":
            contents = Path('form-EX01.html').read_text()
            self.send_response(200)
        elif self.path.startswith("/echo?"):
            url = urlparse(self.path)
            paran = parse_qs(url.query)
            try:
                msg = paran['msg'][0]
                contents = f""""
                    <!DOCTYPE html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Result</title>
                      </head>
                      <body>
                        <h1>Received message:</h1>
                        <p>{msg}</p>
                        <a href="/">Main page</a>
                      </body>
                    </html>"""
                self.send_response(200)
            except (KeyError, IndexError):
                contents = Path('Error.html').read_text()
                self.send_response(404)
        else:
            contents = Path('Error.html').read_text()
            self.send_response(404)
        self.send_header('Content-Type','text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))

        return


Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()