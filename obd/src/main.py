import obd
from time import sleep

while True:
    connection = obd.OBD()

    if connection.is_connected():
        print("Connected to OBDII adapter")
        break

    sleep(5)