
try:
	import RPi.GPIO
	
	def set_pwm(property, value):
		try:
			f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
			f.write(value)
			f.close()
		except:
			print("Error writing to: " + property + " value: " + value)	

except ImportError:

	def set_pwm(property, value):
		pass

