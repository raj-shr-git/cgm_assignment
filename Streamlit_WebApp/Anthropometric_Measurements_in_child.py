#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 17:56:44 2022

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
    st.sidebar.image(Image.open(os.path.join(os.path.join(os.getcwd(), "App_Img_Vid"), "Sidebar_page1_3.png")), width=275)
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
    st.sidebar.info("##### **Author : Rajesh Sharma** :sunglasses: :pray: \n")


def page_display():
    """
    Description : This is function is created for displaying the project details.
    works?
    :return: None
    """
    display_pic = Image.open(os.path.join(os.path.join(os.getcwd(), "App_Img_Vid"), "Display_pic_page1.jpg"))
    st.image(display_pic, width=630)
    proj_desc_txt = """
    ❄ Malnutrition refers to deficiencies, excesses, or imbalances in a person’s 
    intake of energy and/or nutrients. 
    
    ❄ The term malnutrition addresses 3 broad groups of conditions:
        ❄ "Undernutrition" : It includes wasting (low weight-for-height), 
        stunting (low height-for-age) and underweight (low weight-for-age);
        
        ❄ "Micronutrient-related malnutrition" : It includes micronutrient 
        deficiencies (a lack of important vitamins and minerals) 
        or micronutrient excess; and
        
        ❄ Overweight, obesity and diet-related noncommunicable diseases 
        (such as heart disease, stroke, diabetes and some cancers).
    
    ❄ 1.9 billion adults are overweight or obese, while 462 million are underweight.
    
    ❄ Globally in 2020, 
        ❄ 149 MM children under 5 were estimated to be stunted (too short for age),
        ❄ 45 MM were estimated to be wasted (too thin for height), and 
        ❄ 38.9 MM were overweight or obese

    ❄ Around 45% of deaths among children under 5 years of age due to undernutrition. 
        ❄ These mostly occur in low- and middle-income countries. 
    """
    st.text("\n")
    st.markdown("#### **Project Objectives 🏹** \n")
    st.text(proj_desc_txt)

    proj_git_repo = '[Code Repository](https://github.com/raj-shr-git/cgm_assignment)'
    docker_image = '[Docker Image](https://hub.docker.com/r/87889942/anthropometric_measurements_in_child)'

    linked_profile = '[LinkedIn](https://www.linkedin.com/in/raj-shr)'
    github_profile = '[GitHub](http://github.com/raj-shr-git/)'
    kaggle_profile = '[Kaggle](https://www.kaggle.com/rajesh2609)'

    st.text("\n")
    st.markdown("#### **Project Code Repository ☁** \n")
    st.markdown(proj_git_repo, unsafe_allow_html=True)
    st.text("\n")

    st.markdown("#### **Project Docker Image ☁** \n")
    st.markdown(docker_image, unsafe_allow_html=True)
    st.text("\n")

    st.markdown("#### **My Public profiles 🪐** \n")
    st.markdown(linked_profile, unsafe_allow_html=True)
    st.markdown(github_profile, unsafe_allow_html=True)
    st.markdown(kaggle_profile, unsafe_allow_html=True)
    st.text("\n")


if __name__ == '__main__':
    # Displaying the Title
    st.markdown("# 'Anthropometric' Measurements in children 🧒🏼👧📏")
    st.text("\n")

    # Loading sidebar details
    sidebar()

    # Loading Main page content
    page_display()

    # Loading Snow
    st.sidebar.snow()
