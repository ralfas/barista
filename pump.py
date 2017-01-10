from time import sleep

try:
	import RPi.GPIO as io
except ImportError:
	import GPIO_mock as io

from gpio_utils import set_pwm


class Pump:
	"""Uses a pump to dispense liquid."""

	in1_pin = 4
	in2_pin = 17
	stop_speed = 0
	default_run_speed = 11


	def __init__(self):
		io.setmode(io.BCM)

		io.setup(Pump.in1_pin, io.OUT)
		io.setup(Pump.in2_pin, io.OUT)
		
		set_pwm("delayed", "0")
		set_pwm("mode", "pwm")
		set_pwm("frequency", "500")
		set_pwm("active", "1")
		set_pwm("duty", Pump.stop_speed)

		self.state = 'stopped'


	def forward(self):
		io.output(Pump.in1_pin, True)    
		io.output(Pump.in2_pin, False)
		set_pwm("duty", Pump.default_run_speed)
		self.state = 'running'

	 
	def reverse(self):
		io.output(Pump.in1_pin, False)
		io.output(Pump.in2_pin, True)
		set_pwm("duty", Pump.default_run_speed)
		self.state = 'reverse'


	def stop(self):
		io.output(Pump.in1_pin, False)
		io.output(Pump.in2_pin, False)
		set_pwm("duty", Pump.stop_speed)
		self.state = 'stopped'


	def status(self):
		return self.state


	def dispense(self, ml):
		print 'telling the pump to dispense %s' % (ml)

		set_pwm("duty", self._ml_to_speed(ml))
		sleep(self._sleep_for_ml(ml))
		set_pwm("duty", Pump.stop_speed)


	def cleanup(self):
		io.cleanup()


	def _ml_to_speed(self, ml):
		"""How fast to go to dispense ml"""

		return 0


	def _sleep_for_ml(self, ml):
		"""How long to sleep to dispense ml"""

		return 0
