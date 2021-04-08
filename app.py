import os
import pytz
import pyowm
import streamlit as st
from matplotlib import dates
from datetime import datetime
from matplotlib import pyplot as plt

#Get the api key from the OpenWeatherMap website and use it as follows:
owm=pyowm.OWM('32f0cccaae2161e1f887ce03c9b4fc29')
mgr=owm.weather_manager()

#For the streamlit frontend we will need a title and a placeholder text:
st.title("5 Day Weather Forecast")
st.write("### Write the name of a City and select the Temperature Unit and Graph Type from the sidebar")

#Now we will input the city name and using store it in a variable called place
place=st.text_input("NAME OF THE CITY :", "")

if place == None:
    st.write("Input a CITY!")

unit=st.selectbox("Select Temperature Unit",("Celsius","Fahrenheit"))

g_type=st.selectbox("Select Graph Type",("Line Graph","Bar Graph"))
