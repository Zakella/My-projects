from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import parse_qs
import dispatcher


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.path)
        print(parse_qs(self.path[2:]))
        dispatcher.read_data_from_db(parse_qs(self.path[2:]))

    def do_POST(self):
        '''Reads post request body'''
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        req_datas = self.rfile.read(int(self.headers['content-length']))
        data = json.loads(req_datas.decode('utf-8'))
        dispatcher.write_data_in_db(data)


def run():
    httpd = HTTPServer(('localhost', 8080), Serv)
    httpd.serve_forever()
