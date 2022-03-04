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

   global insert_personal_info, insert_personal_info_val

   insert_personal_info = ''' INSERT INTO demotab(F_NAME, L_NAME, FATH_NAME, MOTH_NAME, RELIGION, CASTE, DATE_OF_BIRTH,
                              AGE, PLACE_OF_BIRTH, BLOOD_GROUP, GENDER,MARITAL_STATUS) VALUES
                              (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); '''
   insert_personal_info_val = (F_NAME, L_NAME, FATH_NAME, MOTH_NAME, RELIGION, CASTE, DATE_OF_BIRTH, AGE, PLACE_OF_BIRTH,
                               BLOOD_GROUP, GENDER, MARITAL_STATUS)

def signup_form_Address_info():

   HOUSE_NAME_P = escape(request.form["P-House_Name_input"])
   PLACE_NAME_P = escape(request.form["P-Place_name_input"])
   POST_NAME_P = escape(request.form["P-Post_Name_input"])
   PIN_CODE_P = escape(request.form["P-Pin_Code_input"])
   VILLAGE_P = escape(request.form["P-Village_input"])
   DISTRICT_P = escape(request.form["P-District_input"])
   MOBILE_NO_P = escape(request.form["P-Mobile_No_input"])
   EMAIL_P = escape(request.form["P-Email_input"])

   HOUSE_NAME_T = escape(request.form["T-House_Name_input"])
   PLACE_NAME_T = escape(request.form["T-Place_name_input"])
   POST_NAME_T = escape(request.form["T-Post_Name_input"])
   PIN_CODE_T = escape(request.form["T-Pin_Code_input"])
   VILLAGE_T = escape(request.form["T-Village_input"])
   DISTRICT_T = escape(request.form["T-District_input"])
   MOBILE_NO_T = escape(request.form["T-Mobile_No_input"])
   EMAIL_T = escape(request.form["T-Email_input"])

   global insert_address_info, insert_address_info_val

   insert_address_info = ''' INSERT INTO EMP_ADDR( HOUSE_NAME_P, PLACE_NAME_P, POST_NAME_P, PIN_CODE_P, VILLAGE_P, 
                             DISTRICT_P, MOBILE_NO_P, EMAIL_P, HOUSE_NAME_T, PLACE_NAME_T, POST_NAME_T, PIN_CODE_T, 
                             VILLAGE_T, DISTRICT_T, MOBILE_NO_T, EMAIL_T) VALUES
                             (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); '''

   insert_address_info_val = (HOUSE_NAME_P, PLACE_NAME_P, POST_NAME_P, PIN_CODE_P, VILLAGE_P, DISTRICT_P,  MOBILE_NO_P,
                              EMAIL_P, HOUSE_NAME_T, PLACE_NAME_T, POST_NAME_T, PIN_CODE_T, VILLAGE_T, DISTRICT_T,
                              MOBILE_NO_T, EMAIL_T)

def signup_form_submit( ):

   mycursor.execute(insert_personal_info, insert_personal_info_val)
   mycursor.execute(insert_address_info,insert_address_info_val)
   mydb.commit()
   if mycursor.rowcount > 0:
        return "Success"




