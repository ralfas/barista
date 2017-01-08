import RPi.GPIO as io
from time import sleep

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
		
		self._set("delayed", "0")
		self._set("mode", "pwm")
		self._set("frequency", "500")
		self._set("active", "1")
		self._set("duty", Pump.stop_speed)


	def forward(self):
		io.output(Pump.in1_pin, True)    
		io.output(Pump.in2_pin, False)
		self._set("duty", Pump.default_run_speed)

	 
	def reverse(self):
		io.output(Pump.in1_pin, False)
		io.output(Pump.in2_pin, True)
		self._set("duty", Pump.default_run_speed)


	def stop(self):
		io.output(Pump.in1_pin, False)
		io.output(Pump.in2_pin, False)
		self._set("duty", Pump.stop_speed)


	def dispense(self, ml):
		print 'telling the pump to dispense %s' % (ml)

    	self._set("duty", self._ml_to_speed(ml))
    	sleep(self._sleep_for_ml(ml))
    	self._set("duty", Pump.stop_speed)


    def _set(property, value):
		try:
			f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
			f.write(value)
			f.close()
		except:
			print("Error writing to: " + property + " value: " + value)


    def _ml_to_speed(self, ml):
    	"""How fast to go to dispense ml"""

    	return 0


    def _sleep_for_ml(self, ml):
    	"""How long to sleep to dispense ml"""

    	return 0
