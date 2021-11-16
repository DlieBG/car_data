import obd
from time import sleep
import sys
import time
import threading, http.server, socketserver
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

values = {
    "speed": 0.0,
    "rpm": 0.0,
    "throttlePos": 0.0,
    "egnineLoad": 0.0,
    "coolantTemp": 0.0,
}

class OBD:
    connection = None

    def __init__(self):
        while True:
            self.connection = obd.OBD()

            if self.connection.is_connected():
               print("Connected to OBDII adapter")
               break

            sleep(5)

        while True:
            self.getValue(obd.commands.SPEED, "speed", "kph")
            self.getValue(obd.commands.RPM, "rpm")
            self.getValue(obd.commands.THROTTLE_POS, "throttlePos")
            self.getValue(obd.commands.ENGINE_LOAD, "engineLoad")
            self.getValue(obd.commands.COOLANT_TEMP, "coolantTemp")

            sleep(1)

    def getValue(self, command, field, unit=None):
        try:
            response = self.connection.query(command).value

            if unit:
               response = response.to(unit)
            
            values[field] = float(response.magnitude)
        except:
            values[field] = float(0)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        if "/json" in self.path:
            self.wfile.write(json.dumps(values).encode(encoding='utf_8'))

class Server:
    def __init__(self):
        httpd = HTTPServer(('', 2148), SimpleHTTPRequestHandler)
        httpd.serve_forever()


obdThread = threading.Thread(target=OBD)
obdThread.daemon = True
obdThread.start()

serverThread = threading.Thread(target=Server)
serverThread.daemon = True
serverThread.start()

obdThread.join()
serverThread.join()
