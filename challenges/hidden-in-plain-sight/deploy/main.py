import itertools
import os
from flask import Flask, make_response, request, send_file

app = Flask(__name__)

VALID_IPS = [f'175.45.{x}.{y}' for x, y in itertools.product(range(176, 180), range(256))]

@app.route('/')
def index():
    return 'This is a set of beginner web challenges for <a href="https://acmcyber.com">ACM Cyber</a>.'

@app.route('/web1')
def web1():
    response = make_response("Hello, nothing to see here!")
    response.headers['X-Flag'] = 'flag{here_all_along}'
    return response

@app.route('/web2')
def web2():
    admin = request.cookies.get('admin')
    if admin == 'true':
        return "Yup, you're an admin! flag{c00k13}"
    response = make_response("Hey, you're not an admin >:(<br>How can I tell? You're cookie, of course.")
    response.set_cookie('admin', 'false')
    return response

@app.route('/web3', methods=['GET', 'POST'])
def web3():
    if request.method == 'POST':
        if request.form.get('item') == 'flag':
            return 'Ok, here you go: flag{but_it_was_disabled}'
        return 'Ok, here you go:'
    return 'Hi, what do you want?<form method="POST">' \
        '<input type="radio" name="item" value="noflag"><label for="noflag">No flag</label><br>' \
        '<input type="radio" name="item" value="flag" disabled><label for="flag">Flag</label><br>' \
        '<input type="submit"></form>'

@app.route('/web4')
def web4():
    if request.headers.get('X-Forwarded-For', request.remote_addr) in VALID_IPS:
        return 'flag{ryugyong_dong}'
    return 'Unauthorized: request not from North Korea'

@app.route('/web5', methods=['GIMME_THE_FLAG'])
def web5():
    return "flag{cust0m_m3th0d5}"

@app.route('/web6/')
def web6():
    return 'Check out my pokemon team!' \
        '<ul><li><a href="furret.png">furret</a></li><li><a href="furretfaster.gif">furret</a></li></ul>'

@app.route('/web6/<path:file>')
def view_file(file):
    prefix = os.path.abspath('./files/')
    path = os.path.abspath(os.path.join('./files/pokemon/', file))
    if not path.startswith(prefix):
        return 'out of scope ;)<br>come ask me for a black sticker'
    return send_file(os.path.join('./files/pokemon', file))
