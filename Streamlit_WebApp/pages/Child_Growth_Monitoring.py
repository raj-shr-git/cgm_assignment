#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 19:08:17 2022

@author: Rajesh Sharma
"""
import os
import streamlit as st
from PIL import Image

def sidebar():
    """
    Description : This function is creating for displaying the details on the web page sidebar.
    :return: None
    """
    st.sidebar.text("\n")
    st.sidebar.text("\n")
    st.sidebar.image(Image.open(os.path.join(os.path.join(os.getcwd(), "App_Img_Vid"), "Sidebar_page2.png")), width=290)
    st.sidebar.text("\n")
    st.sidebar.text("\n")
    st.sidebar.text("\n")
    st.sidebar.text("\n")
    st.sidebar.text("\n")
    st.sidebar.text("\n")
    st.sidebar.text("\n")
    st.sidebar.text("\n")
    st.sidebar.text("\n")
    st.sidebar.text("\n")
    st.sidebar.text("\n")
    st.sidebar.text("\n")
    st.sidebar.info("##### **Author : Rajesh Sharma** :sunglasses: :pray:\n")


def display_deep_learning_cgm():
    """
    Description : This is function is created for displaying the helpful videos for better explanation of the
    using Deep Learning for CGM.
    :return: None
    """
    st.markdown("# Deep Learning to solve world hunger & malnutrition 🍲😋")
    st.text("\n")
    display_data = """
❄ Measuring malnutrition accurately is challenging. Early detection and 
intervention require regular anthropometric measurements, measuring weight,
height, and middle-upper arm circumference of children under 5. 

❄ Anthropometric measurements are a non invasive, inexpensive, and suitable method 
for evaluating the nutritional status in the samples.

❄ However, anthropometric techniques are prone to errors that could arise, 
for example, from the inadequate training of personnel and/or 
poor data management.

❄ Therefore, using a CNN-based deep learning model can certainly help in faster,
easier and more precised collection of such measurements.
   """
    st.text(display_data)
    st.text("\n")

    st.subheader("Video-1 🛉📲")
    st.caption("**This video describing the best practices of growth monitoring, how it's done and why it's important.**")
    st.video(data="https://www.youtube.com/watch?v=wwr9fHoOvEQ", format="video/mp4", start_time=0)

    st.text("\n")
    st.text("\n")
    # st.text("\n")

    st.subheader("Video-2 🛊📲")
    st.caption("**Welthungerhilfe relies on AI to fight hunger. The app developed by Welthungerhilfe is run on the Microsoft Azure cloud platform.**")
    st.video(data="https://www.youtube.com/watch?v=FfYxIkp_vw4", format="video/mp4", start_time=0)

    st.text("\n")
    st.text("\n")
    # st.text("\n")

    st.subheader("Video-3 🛊📲")
    st.caption("**Welthungerhilfe provides a game-changer in measurement and data processing for malnourished children under the age of 5 years.**")
    st.video(data="https://www.youtube.com/watch?v=f2doV43jdwg", format="video/mp4", start_time=0)

    st.text("\n")
    st.text("\n")


def display_cycle_of_stunting():
    """
    Description : This is function is created for displaying the flowchart for showing the stages of Stunting
    life cycle.
    :return: None
    """
    st.subheader('**The Life Cycle of Stunting 👧📏**')
    stunting_flowchart = Image.open(os.path.join(os.path.join(os.getcwd(), "App_Img_Vid"), "Page_2_life_cycle.png"))
    st.text("""❄ The below diagram is showing the different stages of Stunting Life Cycle.""")
    st.image(stunting_flowchart, width=550, caption='Stunting Life Cycle')


if __name__ == '__main__':
    # Loading sidebar details
    sidebar()

    # Loading the videos of Deep Learning in CGM
    display_deep_learning_cgm()

    # Loading the Stunting cycle flowchart
    display_cycle_of_stunting()
