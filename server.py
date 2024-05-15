# server.py

from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

from convert import convert_currency

class MyHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        parsed_data = parse_qs(post_data.decode('utf-8'))

        amount = float(parsed_data['amount'][0])
        from_currency = parsed_data['fromCurrency'][0]
        to_currency = parsed_data['toCurrency'][0]

        result = convert_currency(amount, from_currency, to_currency)

        if result is not None:
            response = f'{{"success": true, "result": {result}}}'
        else:
            response = '{"success": false}'

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

if __name__ == '__main__':
    port = 8000
    server_address = ('', port)

    with HTTPServer(server_address, MyHandler) as httpd:
        print(f'Serving at port {port}')
        httpd.serve_forever()
