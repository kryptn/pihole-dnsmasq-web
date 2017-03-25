import yaml
from flask import Flask, request, render_template, redirect, url_for

with open('config.yml') as fd:
    config = yaml.load(fd)

app = Flask(__name__)

@app.route('/')
def index():
    with open(config['hostsfile']) as fd:
        data = fd.read()
    
    return render_template('index.html', data=data)

@app.route('/edit/', methods=['POST'])
def edit():
    data = request.form['hosts']
    with open(config['hostsfile'], 'w') as fd:
        fd.write(data)

    # restart dnsmasq

    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
