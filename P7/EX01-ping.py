import http.client
from http import HTTPStatus
import json


SERVER = "rest.ensembl.org"
PORT = 80
RESOURCE = "/info/ping?content-type=application/json"


conn = http.client.HTTPConnection(SERVER, PORT)

try:
    conn.request("GET", RESOURCE)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

response = conn.getresponse()
print(response)
print(f"Server: {SERVER}")
print(f"URL: {SERVER}{RESOURCE}")

if response.status == HTTPStatus.OK:
    print(f"Response received: {response.status} {response.reason}")
    print()

    data = response.read().decode("utf-8")
    ping = json.loads(data)['ping']
    if ping == 1:
        print("PING OK! The database is running!")
