from flask import Flask, render_template, json, request
from flask_sqlachemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash


app = Flask(__name__)



@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        
if __name__ == "__main__":
    app.run(port=5002)
