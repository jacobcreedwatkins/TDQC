# Python 3 server set up for demonstration of a JQR demo I did in JCY. 
# note that python3 has a simple http server it can natively run, but for demonstration purposes this was a better way of demonstrating it

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "192.168.210.129" #VMware kali machine
serverPort = 8000 #whatever port you want to host on

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://myJQR_demo.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Looks like netsh port forwarding can do stuff and things...</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
