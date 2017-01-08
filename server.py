from bottle import route, run, static_file, template, error
from pump import Pump


pump = Pump()

@route('/')
def index():
	
	return template('templates/index')


@route('/configure')
def configure():

	return template('templates/configure')


@route('/dispense/<volume>')
def dispense(volume):

	pump.dispense(volume)

	return template('Dispensing {{volume}} ml of espresso', volume=volume)


@route('/static/<filename:path>')
def send_static(filename):

	return static_file(filename, root='./static')


@error(404)
def error404(error):

	return 'Nothing here'

try:
	run(host='127.0.0.1', port=8080)
except KeyboardInterrupt:
	pass

pump.stop()
io.cleanup()
