from flask import Flask, render_template, url_for, flash, redirect, request
from Modules.SignUp.signup import signup_form_submit

vac = Flask(__name__)
vac.secret_key = b'shdihdwq$%%^&^%fhkhjhk&(*)&*(&^&$%%#$%$#^VKJGVJGFVGJVFJHBK'


@vac.route('/')
def home_page_():
    return render_template('index.html')

@vac.route('/sign_up/', methods=['GET', 'POST'])
def signup_():
    if request.method == 'POST':
        signup_form_submit()
        return render_template('signup_addr_info.html')
    else:
        return render_template('signup_personal_info.html')


