from flask import Flask, render_template, url_for, flash, redirect, request
from markupsafe import escape

vac = Flask(__name__)


@vac.route('/')
def home_page_():
    return render_template('index.html')

@vac.route('/sign_up/', methods=['GET', 'POST'])
def signup_():
    if request.method == 'POST':
        signup_form_submit()
    else:
        return render_template('signup.html')


