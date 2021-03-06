import http.server, ssl

server_address = ('0.0.0.0', 8000)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile='/Users/netsec/.vim/bin/server_cert.pem',
                               keyfile='/Users/netsec/.vim/bin/server_key.pem',
                               ssl_version=ssl.PROTOCOL_TLS)
httpd.serve_forever()
