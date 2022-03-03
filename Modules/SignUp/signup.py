from flask import Flask, render_template, url_for, flash, redirect, request
from markupsafe import escape
from mysql.connector import connect

mydb = connect(host='localhost', user='root', password='SHA@123', database='demo1')
mycursor = mydb.cursor()

def signup_form_Personal_info():

   F_NAME = escape(request.form["fname_input"])
   L_NAME = escape(request.form["lname_input"])
   FATH_NAME = escape(request.form["fath_name_input"])
   MOTH_NAME = escape(request.form["moth_name_input"])
   RELIGION = escape(request.form["religion_select"])
   CASTE = escape(request.form["caste_select"])
   DATE_OF_BIRTH = escape(request.form["dob_input"])
   AGE = escape(request.form["age_input"])
   PLACE_OF_BIRTH = escape(request.form["pob_input"])
   BLOOD_GROUP = escape(request.form["bloodgrp_input"])
   GENDER = escape(request.form["radio_gender"])
   MARITAL_STATUS = escape(request.form["rdo_maritalstats"])

   insert = '''INSERT INTO demotab(F_NAME, L_NAME, FATH_NAME, MOTH_NAME, RELIGION, CASTE, DATE_OF_BIRTH,AGE, PLACE_OF_BIRTH,
                   BLOOD_GROUP, GENDER,MARITAL_STATUS) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
   val = (F_NAME, L_NAME, FATH_NAME, MOTH_NAME, RELIGION, CASTE, DATE_OF_BIRTH, AGE, PLACE_OF_BIRTH, BLOOD_GROUP, GENDER, MARITAL_STATUS)
   mycursor.execute(insert, val)
   mydb.commit()
   if mycursor.rowcount > 0:
        return "Success"




