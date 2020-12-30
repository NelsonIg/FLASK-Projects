from flask import Flask, render_template
import xmlrpc.client

app = Flask(__name__)
app.config["DEBUG"] = True


def rpd_client(ip: str, port):
    return xmlrpc.client.ServerProxy(f'http://{ip}:{port}')


def write_led(state: int):
    s = rpd_client('localhost', 8000)
    return s.write_led(state)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/LED/<int:state>', methods=['GET', 'POST'])
def led(state):
    resp = write_led(state)
    return f'LED set to {state}'


if __name__ == '__main__':
    app.run(port=8080, threaded=False)



# curl localhost:8080/LED/1