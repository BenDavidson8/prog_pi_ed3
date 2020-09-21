# 12_02_rover_web.py

from bottle import route, run, template
from motor_driver_i2c import MotorDriver

IP_ADDRESS = '192.168.1.54' # of your Pi

motors = MotorDriver()

# Handler for the home page
@route('/')
def index():
    cmd = request.GET.get('command', '')
    if cmd == 'f':
        motors.forward()
    elif cmd == 'l':
        motors.left(0, 0.5) # turn at half speed
    elif cmd == 's':
        motors.stop()
    elif cmd == 'r':
        motors.right(0, 0.5)
    elif cmd == 'b':
        motors.reverse(0, 0.3) # reverse slowly
    return template('home.tpl')
        
run(host=IP_ADDRESS, port=80)