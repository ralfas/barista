#!/usr/bin/env python

from bottle import route, run, static_file, template, error, hook, response
from pump import Pump


pump = Pump()

@hook('after_request')
def no_cache():
#    response.headers['Cache-Control'] = 'max-age=0, no-cache, no-store'
	pass


@route('/')
def index():
	
	return template('templates/index')


@route('/configure')
def configure():

	return template('templates/configure')


@route('/maintain')
def maintain():

	return template('templates/maintain')


@route('/run/reverse')
def run_reverse():

	pump.reverse()

	return 'Running the pump in reverse'


@route('/run/stop')
def run_stop():

	pump.stop()

	return 'Stopped the pump'


@route('/run/start')
def run_start():

	pump.forward()

	return 'Started the pump'


@route('/run/state')
def run_state():

	return pump.status()


@route('/dispense/<volume:int>')
def dispense(volume):

	pump.dispense(volume)

	return template('Dispensing {{volume}} ml of espresso', volume=volume)


@route('/static/<filename:path>')
def serve_static(filename):

	return static_file(filename, root='./static')


@error(404)
def error404(error):

	return 'Nothing here'

try:
	run(host='127.0.0.1', port=8080)
except KeyboardInterrupt:
	pass

pump.stop()
pump.cleanup()
