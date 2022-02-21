from flask import Flask, render_template, url_for, flash, redirect, request
from markupsafe import escape

vac = Flask(__name__)