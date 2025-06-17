from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    email = StringField('email') 
    password = PasswordField('password')    
    submit= SubmitField('Login')  

app = Flask(__name__)
#app.config['WTF_CSRF_ENABLED'] = True

app.config['SECRET_KEY'] = 'ushatkjashdjkashdjkashdjkashdjkashdjkashdj'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        # Here you would typically check the credentials against a database
        # For this example, we will just print them to the console
        print(f"Email: {email}, Password: {password}")
        return render_template('success.html', email=email)
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
