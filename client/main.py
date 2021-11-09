import obd
from time import sleep

connection = obd.OBD() # auto-connects to USB or RF port

while True:
    print('')
    print('')
    
    print('SPEED: ' + connection.query(obd.commands.SPEED).value.to("kmh"))
    print('RPM: ' + connection.query(obd.commands.RPM).value)
    print('THROTTLE_POS: ' + connection.query(obd.commands.THROTTLE_POS).value)
    print('OIL_TEMP: ' + connection.query(obd.commands.OIL_TEMP).value)
    print('ENGINE_LOAD: ' + connection.query(obd.commands.ENGINE_LOAD).value)
    print('COOLANT_TEMP: ' + connection.query(obd.commands.COOLANT_TEMP).value)

    sleep(1)
