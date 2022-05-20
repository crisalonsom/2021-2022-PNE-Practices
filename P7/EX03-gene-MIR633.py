import http.client
from http import HTTPStatus
import json


SERVER = "rest.ensembl.org"
PORT = 80


GENE = 'MIR633'
RESOURCE = f"/sequence/id/ENSG00000207552?content-type=application/json"

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

    raw_data = response.read().decode("utf-8")
    data = json.loads(raw_data)
    print(f"Gene: {GENE}")
    print(f"Description: {data['desc']}")
    print(f"Bases: {data['seq']}")
