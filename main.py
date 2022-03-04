from flask import Flask, render_template, url_for, flash, redirect, request
from Modules.SignUp.signup import signup_form_submit, signup_form_Personal_info, signup_form_Address_info

vac = Flask(__name__)
vac.secret_key = b'shdihdwq$%%^&^%fhkhjhk&(*)&*(&^&$%%#$%$#^VKJGVJGFVGJVFJHBK'


@vac.route('/')
def home_page_():
    return render_template('index.html')


@vac.route('/signup_personal/', methods=['GET', 'POST'])
def _signup_form_personal_info_():
    if request.method == 'POST':
        signup_form_Personal_info()
        return render_template('signup/signup_addr_info.html')
    else:
        return render_template('signup/signup_personal_info.html')

@vac.route('/signup_address/', methods=['GET', 'POST'])
def _signup_form_Address_info_():

    if request.method == 'POST':
        signup_form_Address_info()
        return render_template('signup/signup_qualification_info.html')
    else:
        return render_template('signup/signup_addr_info.html')

