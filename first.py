import streamlit as st 

import pandas as pd

st.title(" HELLO EVERYONE WELLCOME TO MY WEBPAGE LOYING BHAI PROJECTS OF I.T ")
# header 
st.header(" Hello firnds i am jitu loying now i studied at national institued of information technology $ electronics gov.india")
# sub header 
st.subheader(" now we going to discuse about of information technology .........and the programing language  Html, Java,python , css,php,javascript, and designing of website and prectical projects with this webpage ")

# set a image 
from PIL import Image
img=Image.open('jituloying1.jpg')
st.image(img,width=700,caption="its a random photo")
st.write(" please contact on this number for more information ph: 7896220943-whatsapp//email: jituloying1947@gmail.com")



#   SIDEBAR 

st.sidebar.header("WELLCOM TO LOYING PROGRAMING LERANING POINT.")
st.sidebar.header(" About.")
st.sidebar.text(''' Hey firnds now we going to learn about of it website 
and webapplication designing''')
if st.sidebar.checkbox("show/hide"):  
 st.sidebar.write(" if you like my page and if you realyse that its a good website then sheare it with your programing lover frinds")
 # radio button
 status=st.sidebar.radio('What is your status with my page are you active ',('Active','Inactive'))
 if status is "Inactive":
   st.warning("You are Inactive please Active with this page ")
 else:
   st.success("You are Active with this page ")
   
   
   # text input 
   Name=st.sidebar.text_input("Enter your name :")
   Father_Name=st.sidebar.text_input("Enter your father Name :")
   Mother_Name=st.sidebar.text_input("Enter your Mother Name :")
   # age 
   Age=st.sidebar.slider("What is your age ",12,70)
   gmail=st.sidebar.text_input("Enter your Email id;")
   if '@gmail.com'in gmail:
     st.sidebar.write(f'confirm your gamil id{gmail}')
   # location 
   location=st.sidebar.text_input(" Enter your location Where did you live")
   st.sidebar.write('you entered that you live in ',(location),"location")
   
   
   