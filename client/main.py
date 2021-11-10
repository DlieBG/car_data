import obd
from time import sleep

connection = obd.OBD() # auto-connects to USB or RF port

while True:
    print('')
    print('')
    
    print('SPEED: ' + str(float(connection.query(obd.commands.SPEED).value.to("kph").magnitude)))
    print('RPM: ' + str(float(connection.query(obd.commands.RPM).value)))
    print('THROTTLE_POS: ' + str(float(connection.query(obd.commands.THROTTLE_POS).value)))
    print('OIL_TEMP: ' + str(float(connection.query(obd.commands.OIL_TEMP).value)))
    print('ENGINE_LOAD: ' + str(float(connection.query(obd.commands.ENGINE_LOAD).value)))
    print('COOLANT_TEMP: ' + str(float(connection.query(obd.commands.COOLANT_TEMP).value)))

    sleep(1)
