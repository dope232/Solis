
import streamlit as st 

import pandas as pd
import os
import random
import math
import time
from PIL import Image
import numpy as np

from streamlit_marquee import streamlit_marquee
import pyrebase
import cgi
from base64 import b64decode

from streamlit_player import st_player
from st_on_hover_tabs import on_hover_tabs
import cv2
import smtplib






@st.cache
def load_image(picture):
    img = Image.open(picture)
    return img
#Login Authorization

st.set_page_config(page_title= "SolisVEGAS", page_icon='web_logo.jpg', layout="wide", initial_sidebar_state="auto", menu_items={'Get Help': 'https://www.extremelycoolapp.com/help', 'About' : 'https://www.extremelycoolapp.com/help'})
st.title("SolisVEGAS- The Tax info App! ")

hide_menu_style = """
    <style>

    footer {visibility:hidden;}
    </style>"""

st.markdown('<style>' + open('style/style3.css').read() + '</style>', unsafe_allow_html=True)

primaryColor="#F63366"
backgroundColor="#121"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

with st.sidebar:

    tabs = on_hover_tabs(tabName=['Dashboard', 'Advice from CA', ],
                         iconName=['dashboard', 'money'], default_choice=0)



    st.title("Credits:")
    st.write("Dhanush ")
    st.write("Ashutosh ")
    st.write("Gaurav")
    st.write("Balaji K")




st.markdown(hide_menu_style, unsafe_allow_html=True)
image = Image.open('web_logo.jpg')

st.image(image, width=95, clamp=False, channels="RGB", output_format="auto")

left_column, center_column, right_column = st.columns(3)

with center_column:
    image = Image.open('taxone.jpg')
    st.image(image, width=600, clamp=False, channels="RGB", output_format="auto")

with left_column:
    streamlit_marquee(**{
        # the marquee container background color
        'background': "#0e1117",
        # the marquee text size
        'font-size': '200px',
        # the marquee text color
        "color": "#ffffff",
        # the marquee text content
        'content': 'Tax deduction when taking out a home loan: If you use section 80C of the Income Tax Act to your advantage when structuring your house loan and reducing your taxable income, you can get a benefit of Rs. 1.5 lakhs on the principal amount and Rs. 2 lakhs on the interest paid as per section 24.Earnings from Interest on Savings Accounts: For a maximum of Rs. 10,000, interest earned on savings accounts is generally tax-exempt. This sum represents the total of all savings accounts. For senior citizens, this cap is increased to Rs. 50,000 under section 80TTB.Money Received from Life Insurance Policy: The maturity amount or bonus is completely free from income tax under Section 10 if the premium is below 10% of the sum assured (if the policy is purchased after 1st of April, 2012). The maturity amount is tax-free for policies purchased before this date if the premium is 20% of the sum assured. Policies issued after April 1, 2013 that cover the life of a person with a disability or a disease listed under Sections 80U or 80DDB, respectively, are also included in this category. In these cases, the amount received at maturity is tax-free as long as the premium is below 15% of the sum assured.',

        # the marquee container width
        'width': '900px',
        # the marquee container line height
        'lineHeight': "100px",
        # the marquee duration
        'animationDuration': '120s',
    })
with right_column:
    streamlit_marquee(**{
        # the marquee container background color
        'background': "#0e1117",
        # the marquee text size
        'font-size': '200px',
        # the marquee text color
        "color": "#ffffff",
        # the marquee text content
        'content': ' NIFTY 50 	18027.70 	-80.10 	-0.44 || SENSEX 	60621.77 	-236.66 	-0.39 || SENSEX 	60621.77 	-236.66 	-0.39 NIFTY IT 	29529.70 	-102.65 	-0.35 S&P BSE Smallcap 	28630.19 	-143.08 	-0.50 Reliance 	2,442.65 	-29.40 	1,689.76 HDFC Bank 	1,660.95 	16.85 	1,565.50 HUL 	2,548.75 	-101.00 	1,172.35 Infosys 	1,525.55 	-13.35 	994.97  ',

        # the marquee container width
        'width': '900px',
        # the marquee container line height
        'lineHeight': "100px",
        # the marquee duration
        'animationDuration': '80s',

        'key' : 'one'
    })
    st.header("NIFTY")
    st.metric(label=" Market Summary", value=18069.10, delta=+1.47,
              )


    st.header("BSE")
    st.metric(label="SENSEX", value=60751.23, delta=1.51, )


if tabs == 'Advice from CA':
    st.header("Here are some advices from some CA's and professional youtubers!")

    st_player("https://www.youtube.com/watch?v=LLdKcFpHgM8")
    st_player("https://www.youtube.com/watch?v=G9GVK1gGD6M")
    st_player("https://www.youtube.com/watch?v=BTOHpoC-XsE")
    st_player("https://www.youtube.com/watch?v=fIJ86j0HIxM")














firebaseConfig = {

  'apiKey': "AIzaSyARYPbP8eMvcvy9zIBC7eQQdxRDOqmpqns",

  'authDomain': "miniprojectsolis2.firebaseapp.com",

  'projectId': "miniprojectsolis2",

  'databaseURL': "https://miniprojectsolis2-default-rtdb.europe-west1.firebasedatabase.app/",

  'storageBucket': "miniprojectsolis2.appspot.com",

  'messagingSenderId': "137552857999",

  'appId': "1:137552857999:web:dba7e32a4809141a60d9fa",

  'measurementId': "G-MJMGBJC98Y"

};



# Firebase authentication

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


#Database initalization


db = firebase.database()
storage = firebase.storage()

form4 = st.form(key = 'form4')







choice = st.selectbox('Login/Signup',['Login', 'Signup'])








email = st.text_input("Please enter your email")
if not email:
    st.error("Please enter your email")

password = st.text_input("Please enter your password", type = "password")
if not password:
    st.error("Please enter your password")


if choice == 'Signup':
    st.write("Signup")
    form = st.form(key="annotation")

    with form:

        name = st.text_input("Please enter your full name", key="name")

        genre = st.radio(
            "Select your gender",
            ('Male', 'Female', 'Transexual', 'Other'))

        if genre == 'Other':
            other_gender = st.text_input("Please enter your specified gender", key = "other_gender")




        address = st.text_input("Please enter your Address", key="Address")

        city = st.text_input("Please enter the city you are currently living in", key="city")

        df = pd.DataFrame({
            'first column': ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat",
                             "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala",
                             "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
                             "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
                             "Uttarakhand", "West Bengal", "Andaman and Nicobar", "Chandigarh",
                             "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "Delhi", "Puducherry"]

        })

        option = st.selectbox(
            'Please enter your state',
            df['first column'])

        date = st.date_input("Please enter your date of birth,", key="date")
        uploaded_file = st.file_uploader(
            "Please upload your **AADHAAR CARD**  for verification(in the form of .jprg,.png and .pdf only")
        uploaded_file2 = st.file_uploader(
            "Please upload your **PAN CARD**  for verification(in the form of .jprg,.png and .pdf only")
        picture = st.camera_input("Take a picture of yourself to ensure you are not a bot")

        # if picture is not None:
        #     file_details = {"FileName": picture.name, "FileType": picture.type}
        #     st.write(file_details)
        #     img = load_image(picture)
        #     st.image(img, height=250, width=250)
        #     with open(os.path.join("tempDir", picture.name), "wb") as f:
        #         f.write(picture.getbuffer())
        #     st.success("Saved File")

        submitted = st.form_submit_button(label="Submit")

        if submitted:

            user = auth.create_user_with_email_and_password(email,password)
            st.success("Congrats! You have been verified")
            if picture is not None:
                file_details = {"FileName": picture.name, "FileType": picture.type}
                st.write(file_details)
                img = load_image(picture)
                st.image(img)
                with open(os.path.join("tempDir", picture.name), "wb") as f:
                    f.write(picture.getbuffer())
                st.success("Saved File")
            st.balloons()


            


            user = auth.sign_in_with_email_and_password(email, password)
            db.child(user['localID']).child("Handle").set(name)
            db.child(user['localID']).child("ID").set(user['localID'])
            db.child(user['localID']).chile("Picture").set(picture)
            st.title('Welcome' + name)
            st.info('Login via login drop down selection')
















if choice == 'Login':



    user = auth.sign_in_with_email_and_password(email,password)

    form = st.form(key = 'annotation')

    with form:
        submit = st.form_submit_button("Enter")

        if submit:

            bio = st.radio("Jump to", ['Tax Calculator','Settings'])

            if bio == "Settings":
                nImage = db.child(user['localId']).child("Image").get().val()
                if nImage is not None:
                    # We plan to store all our image under the child image
                    Image = db.child(user['localId']).child("Image").get()
                    for img in Image.each():
                        img_choice = img.val()
                        # st.write(img_choice)
                    st.image(img_choice)
                    exp = st.beta_expander('Change Bio and Image')
                    # User plan to change profile picture
                    with exp:
                        newImgPath = st.text_input('Enter full path of your profile imgae')
                        upload_new = st.button('Upload')
                        if upload_new:
                            uid = user['localId']
                            fireb_upload = storage.child(uid).put(newImgPath, user['idToken'])
                            a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens'])
                            db.child(user['localId']).child("Image").push(a_imgdata_url)
                            st.success('Success!')
                            # IF THERE IS NO IMAGE
                else:
                    st.info("No profile picture yet")
                    newImgPath = st.text_input('Enter full path of your profile image')
                    upload_new = st.checkbox('Upload')
                    if upload_new:
                        uid = user['localId']
                        # Stored Initated Bucket in Firebase
                        fireb_upload = storage.child(uid).put(newImgPath, user['idToken'])
                        # Get the url for easy access
                        a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens'])
                        # Put it in our real time database
                        db.child(user['localId']).child("Image").push(a_imgdata_url)


            if bio == "Tax Calculator":
                st.title('[Taxation App]')
                salary = st.number_input('Salary earned')
                investments = st.number_input('Investments made')
                loan_intrest = st.number_input('Enter the loan_intrest intereest paid yearly')
                rent_paid = st.number_input('Enter amount house rent paid')
                principal_loan_amount = st.number_input('Enter if investments made are less than 150k rupees')
                a = 24 / 100 * salary
                b = 50 / 100 * salary * 30 / 100
                c = rent_paid - (10 / 100 * salary * 30 / 100)
                with st.spinner('Please wait for a moment'):
                    time.sleep(1)
                st.success('Done!')
                if salary <= 250000:
                    st.write('Zero Tax to be paid')
                elif salary > 250000:
                    if investments > 0:
                        if investments < 150000:
                            i = salary - investments
                        else:
                            i = salary - 150000
                        if loan_intrest > 0:
                            if loan_intrest + principal_loan_amount < 200000:  # if loan intrest less than 2 lakh then principal amount can also be claimed
                                l = i - loan_intrest - principal_loan_amount
                            else:
                                l = i - 200000
                            if rent_paid > 0:
                                if a < b and a < c:
                                    r = l - a
                                elif b < a and b < c:
                                    r = l - b
                                else:
                                    r = l - c

                        if 500000 >= r > 250001:
                            t = (5 / 100 * r)
                            st.write('The tax amount that needs to be paid', t)

                        elif 1000000 >= r > 500001:
                            t = (20 / 100 * (r - 500001) + 12500)
                            st.write('The tax amount that needs to be paid', t)

                        elif 1000001 <= r:
                            t = (30 / 100 * (r - 1000001) + 112500)
                            st.header('The tax amount that needs to be paid', t)

                            st.write("The amounnt of money in hand after tax is ", salary - t)



                genre = st.radio("How would you rate our services out of five", ('1', '2', '3', '4', '5'))

                if genre == '1':
                    st.header('Abysmal')
                    st.caption("We will try to improve")
                if genre == '2':
                    st.header("Poor")
                    st.caption("We will try to improve")
                if genre == '3':
                    st.header("Average")
                    st.caption("We will try to improve")
                if genre == '4':
                    st.header("Good")
                    st.caption("We are happy that you liked our services")
                if genre == '5':
                    st.header("Excellent")
                    st.caption("We are happy that you liked our services")












st.header("Contact here for any help!")



contact_form = '''
<form action="https://formsubmit.co/clgdhanush232@gmail.com" method="POST">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your Email " required>
     <textarea name="message" placeholder="Details of your problem"></textarea>
     <button type="submit">Send</button>
</form>'''


st.markdown(contact_form, unsafe_allow_html=True) # we can inject any html using streamlit .markdown

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


































