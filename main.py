from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/notfound')
def notfound():
    return render_template('404.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)