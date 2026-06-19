from flask import Flask, render_template, request
  
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('logpage.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == "swetha" and password == "1314":
        return "<h1>Login Successful!</h1>"
    else:
        return "<h1>Invalid Username or Password</h1>"

if __name__ == '__main__':
    app.run(debug=True)