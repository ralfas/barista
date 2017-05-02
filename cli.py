from time import sleep
import argparse

try:
	import RPi.GPIO as io
except ImportError:
	import GPIO_mock as io


io.setmode(io.BCM)

enable_pin = 25
in1 = 17
in2 = 24

io.setup(enable_pin, io.OUT)
io.setup(in1, io.OUT)
io.setup(in2, io.OUT)

# setting frequency to 60
pwm = io.PWM(enable_pin, 60)

# facing pump
# with pump red connected to L293D 1Y
# with pump black connected to L293D 2Y
# GPIO #17 connected to L293D 1A
# GPIO #24 connected to L293D 2A


def percent(string):
    value = float(string)
    if value < 0 or value > 100:
        raise argparse.ArgumentTypeError('Value has to be between 0 and 100')
    return value

parser = argparse.ArgumentParser(description='Run the pump for a fixed time duration')
parser.add_argument('direction', choices=['cw', 'acw'], help='clockwise or anti-clockwise')
parser.add_argument('duration', type=float, help='duration in seconds')
parser.add_argument('duty_cycle', type=percent, help='duty cycle (0 to 100)')

args = parser.parse_args()

try:
	print "running pump"
	if args.direction == "cw":
		io.output(24, io.LOW)
		io.output(17, io.HIGH)
	else:
		io.output(24, io.HIGH)
		io.output(17, io.LOW)

	pwm.start(args.duty_cycle)
	sleep(args.duration)
	pwm.stop()
	print "stopped pump"
	io.cleanup()
except KeyboardInterrupt:
	pwm.stop()
	io.cleanup()
