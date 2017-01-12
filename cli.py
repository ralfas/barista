import time
from gpio_utils import set_pwm

try:
	import RPi.GPIO as io
except ImportError:
	import GPIO_mock as io


io.setmode(io.BCM)

io.setup(17, io.OUT)
io.setup(18, io.OUT)
io.setup(24, io.OUT)

#defaults
set_pwm("delayed", "0")
set_pwm("mode", "pwm")
#these can be tweaked in the CLI
set_pwm("frequency", "500")
set_pwm("active", "1")
set_pwm("duty", 0)

try:
	while True:
		cmd = raw_input("Command > ")
		if cmd == "help":
			print "(f)requency, (a)ctive, (d)uty, (p17), (p18), (p24), (q)"
		elif cmd[0] == "f":
			set_pwm("frequency", cmd[2:])
			print "setting frequency to %s" % (cmd[2:])
		elif cmd[0] == "a":
			set_pwm("active", cmd[2:])
			print "setting active to %s" % (cmd[2:])
		elif cmd[0] == "d":
			set_pwm("duty", cmd[2:])
			print "setting duty to %s" % (cmd[2:])
		elif cmd[0] == "p":

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
			io.cleanup()
			break
except KeyboardInterrupt:
	io.cleanup()
