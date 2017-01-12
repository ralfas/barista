from time import sleep

try:
	import RPi.GPIO as io
except ImportError:
	import GPIO_mock as io


class Pump:
	"""Uses a pump to dispense liquid."""

	enable_pin = 18
	in1_pin = 4
	in2_pin = 17
	stop_duty_cycle = 0
	default_duty_cycle = 80#Minimum ~50 for opperation
	default_frequency = 500#Hz


	def __init__(self):
		io.setmode(io.BCM)

		io.setup(Pump.enable_pin, io.OUT)
		io.setup(Pump.in1_pin, io.OUT)
		io.setup(Pump.in2_pin, io.OUT)

		self.pwm = io.PWM(Pump.enable_pin, Pump.default_frequency)

		self.state = 'stopped'


	def forward(self):
		io.output(Pump.in1_pin, io.HIGH)
		io.output(Pump.in2_pin, io.LOW)
		self.pwm.ChangeDutyCycle(Pump.default_duty_cycle)
		self.state = 'running'

	 
	def reverse(self):
		io.output(Pump.in1_pin, io.LOW)
		io.output(Pump.in2_pin, io.HIGH)
		self.pwm.ChangeDutyCycle(Pump.default_duty_cycle)
		self.state = 'reverse'


	def stop(self):
		io.output(Pump.in1_pin, io.LOW)
		io.output(Pump.in2_pin, io.LOW)
		self.pwm.ChangeDutyCycle(Pump.stop_duty_cycle)
		self.state = 'stopped'


	def status(self):
		return self.state


	def dispense(self, ml):
		print 'telling the pump to dispense %s' % (ml)

		self.pwm.ChangeDutyCycle(self._ml_to_duty_cycle(ml))
		sleep(self._sleep_for_ml(ml))
		self.pwm.ChangeDutyCycle(Pump.stop_duty_cycle)


	def cleanup(self):
		io.cleanup()


	def _ml_to_duty_cycle(self, ml):
		"""How fast to go to dispense ml"""

		return 0


	def _sleep_for_ml(self, ml):
		"""How long to sleep to dispense ml"""

		return 0
