from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return'Flask App Minia Group !'


@app.route('/aboshaymaa')
def test():
    return 'Hello'

if __name__=='__main__':
   app.run(debug=False,host='0.0.0.0',port=5000)

