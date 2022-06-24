import obd, sys
from time import sleep

def get_value(command, unit=None):
    try:
        response = connection.query(command).value

        if unit:
            response = response.to(unit)
        
        return float(response.magnitude)
    except:
        return float(0)

def upload_values(values):
    print(values)

tries = 0

while True:
    connection = obd.OBD()

    if connection.is_connected():
        print("Connected to OBDII adapter")
        break

    if tries > 5:
        print("Connection could not be established")
        print("Restarting...")
        sys.exit(1)

    tries += 1
    sleep(5)

while True:
    upload_values({
        "speed": get_value(obd.commands.SPEED, "kph"),
        "rpm": get_value(obd.commands.RPM),
        "throttel_pos": get_value(obd.commands.THROTTLE_POS),
        "engine_load": get_value(obd.commands.ENGINE_LOAD),
        "coolant_temp": get_value(obd.commands.COOLANT_TEMP)
    })
