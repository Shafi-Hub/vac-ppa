from flask import Flask, render_template, url_for, flash, redirect, request
from Modules.SignUp.signup import signup_form_user_info, signup_form_Personal_info, signup_form_Address_info

vac = Flask(__name__)
vac.secret_key = b'shdihdwq$%%^&^%fhkhjhk&(*)&*(&^&$%%#$%$#^VKJGVJGFVGJVFJHBK'


@vac.route('/')
def home_page_():
    return render_template('index.html')

@vac.route('/signup-user_type')
def _signup_form_user_info_():
    if request.method == 'POST':
        signup_form_user_info()
        return render_template('signup/signup_personal_info.html')
    else:
        return render_template('signup/signup_user_info.html')


@vac.route('/signup-personal_info/', methods=['GET', 'POST'])
def _signup_form_personal_info_():
    if request.method == 'POST':
        signup_form_Personal_info()
        return render_template('signup/signup_addr_info.html')
    else:
        return render_template('signup/signup_personal_info.html')


@vac.route('/signup-address_info/', methods=['GET', 'POST'])
def _signup_form_Address_info_():
    if request.method == 'POST':
        signup_form_Address_info()
        return render_template('signup/signup_qualification_info.html')
    else:
        return render_template('signup/signup_addr_info.html')

