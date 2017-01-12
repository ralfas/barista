import time
from gpio_utils import set_pwm

try:
	import RPi.GPIO as io
except ImportError:
	import GPIO_mock as io


io.setmode(io.BCM)

enable_pin = 18
in1 = 17
in2 = 24

io.setup(enable_pin, io.OUT)
io.setup(in1, io.OUT)
io.setup(in2, io.OUT)

pwm = io.PWM(18, 500)

try:
	while True:
		cmd = raw_input("Command > ")
		if cmd == "help":
			print "(f)requency, (start), (stop), (d)uty, (p17), (p24), (q)"
		elif cmd[0] == "f":
			pwm.ChangeFrequency(cmd[2:])
			print "setting frequency to %s" % (cmd[2:])
		elif cmd == "start":
			pwm.start(1)
			print "started with duty 1"
		elif cmd == "stop":
			pwm.stop()
			print "stopped"
		elif cmd[0] == "d":
			pwm.ChangeDutyCycle(cmd[2:])
			print "setting duty cycle to %s" % (cmd[2:])
		elif cmd[0] == "p" and cmd[1:3] in ("17", "24"):

			value = io.LOW
			if cmd[4] == "0":
				value = io.LOW
			elif cmd[4] == "1":
				value = io.HIGH
			else:
				continue
			io.output(cmd[1:3], value)
			print "setting pin %s to %d" % (cmd[1:3], value)
		elif cmd[0] == "q":
			pwm.stop()
			io.cleanup()
			break
except KeyboardInterrupt:
	pwm.stop()
	io.cleanup()
