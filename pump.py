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
	default_duty_cycle = 100#Minimum ~50 for opperation
	default_frequency = 500#Hz


	def __init__(self):
		io.setmode(io.BCM)

		io.setup(Pump.enable_pin, io.OUT)
		io.setup(Pump.in1_pin, io.OUT)
		io.setup(Pump.in2_pin, io.OUT)

		self.pwm = io.PWM(Pump.enable_pin, Pump.default_frequency)

		self.state = 'stopped'


	def forward(self):
		print 'telling the pump to run forward'

		self.pwm.stop()
		io.output(Pump.in1_pin, io.HIGH)
		io.output(Pump.in2_pin, io.LOW)
		self.pwm.start(Pump.default_duty_cycle)
		self.state = 'running'

	 
	def reverse(self):
		print 'telling the pump to run in reverse'

		self.pwm.stop()
		io.output(Pump.in1_pin, io.LOW)
		io.output(Pump.in2_pin, io.HIGH)
		self.pwm.start(Pump.default_duty_cycle)
		self.state = 'reverse'


	def stop(self):
		self.pwm.stop()
		io.output(Pump.in1_pin, io.LOW)
		io.output(Pump.in2_pin, io.LOW)
		self.state = 'stopped'


	def status(self):
		return self.state


	def dispense(self, ml):
		print 'telling the pump to dispense %s' % (ml)

		self.pwm.ChangeDutyCycle(Pump.default_duty_cycle)
		sleep(self._sleep_for_ml(ml))
		self.pwm.ChangeDutyCycle(Pump.stop_duty_cycle)


	def cleanup(self):
		io.cleanup()


	def _sleep_for_ml(self, ml):
		"""How long to sleep to dispense ml"""

		return 0
