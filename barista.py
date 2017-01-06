from bottle import route, run, static_file, template, error
import pump

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


run(host='127.0.0.1', port=8080)
