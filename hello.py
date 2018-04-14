from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return('<h1>hello world! dgy</h1>')

@app.route('/user/<name>')
def user(name):
    return('<h1>hello,%s</h1>'% name)

if __name__ == '__main__':
    print('start the main loop')   
    app.run(debug = True)
