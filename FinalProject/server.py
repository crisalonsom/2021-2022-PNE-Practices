import http.server
import socketserver
import termcolor
import json
from pathlib import Path
import jinja2 as j
from urllib.parse import urlparse, parse_qs
import http.client


SERVER = "rest.ensembl.org"
PORT = 8080

def  read_html_file (filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents

def read_template_html_file(filename):
    import jinja2
    from pathlib import Path
    content = jinja2.Template(Path(filename).read_text())
    return content


def request_creation(endpoint, arguments):
    conn = http.client.HTTPConnection(SERVER)
    param = "?content-type=application/json"

    try:
        conn.request("GET", endpoint+ param + arguments)
    except ConnectionRefusedError:
        print("ERROR! Is not possible to connect to the Server")
        exit()

    resp = conn.getresponse()
    print(f"Response received: {resp.status} {resp.reason}\n")
    data = json.loads(resp.read().decode("utf-8"))
    return data

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
                in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happytest server: It always returns a message saying
        # that everything is ok
        url= urlparse(self.path)
        path = url.path
        argum = parse_qs(url.query)
        # Message to send back to the client
        contents = ""

        if path == "/":
            contents = Path("indexfinalproject.html").read_text()
            self.send_response(200)
        elif path == "/listSpecies":
            try:
                sp_dict = request_creation("/info/species", "")
                spec = sp_dict["species"]
                number_species = len(spec)
                limit = int(argum['limit'][0])

                if len(argum) == 1:
                    limit = int(argum['limit'][0])
                elif len(argum) == 0:
                    limit = number_species

                else:
                    contents = Path("Error.html").read_text()
                    self.send_response(404)

                list_sp = []
                for s in range(0, int(argum['limit'][0])):
                    list_sp.append(spec[s]["name"])
                species = ""

                for l in list_sp:
                    species += f"·{l.capitalize()}<br>"
                    contents = read_html_file(path[1:] + ".html"). \
                    render(context={"species": species,
                                    "total": number_species,
                                    "limit": limit})



            except Exception:
                contents = read_html_file("Error.html") \
                    .render(context={})


        elif path == "/karyotype":
            try:
                if len(argum) == 1:
                    species_name = argum['species'][0]
                    dictionary = request_creation("info/assembly/" + species_name, "")
                    kar_dict = dictionary["karyotype"]
                    contents = read_html_file(path[1:] + ".html"). \
                        render(context={'karyotype': kar_dict})

                else:
                    contents = Path("Error.html").read_text()
                    self.send_response(404)
            except Exception:
                contents = read_html_file("Error.html") \
                    .render(context={})



        elif path == "/chromosomeLength":
            try:
                if len(argum) == 2:
                    name_sp = argum['species'][0]
                    chrom = argum['chromosomes'][0]
                    chr_dict = request_creation("info/assembly/" + name_sp, "")
                    chr_dict_2 = chr_dict["top_level_region"]
                    length = 0
                    for c in range(0, len(chr_dict_2)):
                        if chr_dict_2[c]["name"] == chrom:
                            length += int(chr_dict_2[c]["length"])
                    contents = read_html_file(path[1:] + ".html").\
                        render(context={'length': length})

                else:
                    contents = Path("Error.html").read_text()
                    self.send_response(404)
            except Exception:
                contents = read_html_file("Error.html") \
                    .render(context={})



        else:
            contents = Path("Error.html").read_text()
            self.send_response(404)

        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return

Hanler = TestHandler
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
        print("Serving at PORT...", PORT)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print()
            print("Stopped by the user")
            httpd.server_close()

