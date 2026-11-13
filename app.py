from flask import Flask, render_template

app = Flask(__name__)

#this is basic flask code right 
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
