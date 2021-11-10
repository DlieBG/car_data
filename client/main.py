import obd
from time import sleep

connection = obd.OBD() # auto-connects to USB or RF port

def getValue(command, unit=None):
    try:
        response = connection.query(obd.commands.SPEED).value

        if unit:
            response = response.to(unit)

        return float(response.magnitude)
    except:
        return float(0)

while True:
    print('')
    print('')
    
    print('SPEED: ' + getValue(obd.commands.SPEED, "kph"))
    print('RPM: ' + getValue(obd.commands.RPM))
    print('THROTTLE_POS: ' + getValue(obd.commands.THROTTLE_POS))
    print('OIL_TEMP: ' + getValue(obd.commands.OIL_TEMP))
    print('ENGINE_LOAD: ' + getValue(obd.commands.ENGINE_LOAD))
    print('COOLANT_TEMP: ' + getValue(obd.commands.COOLANT_TEMP))

    sleep(1)
