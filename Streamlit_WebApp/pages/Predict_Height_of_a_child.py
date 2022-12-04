#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 15:50:17 2022

@author: Rajesh Sharma
"""
import os
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


def sidebar():
    """
    Description : This function is creating for displaying the details on the web page sidebar.
    :return: None
    """
    st.sidebar.text("\n")
    st.sidebar.image(Image.open(os.path.join(os.path.join(os.getcwd(), "App_Img_Vid"), "Sidebar_page1_3.png")), width=290)
    st.sidebar.markdown("#### **Enter your credentials 📜**")
    st.markdown("# **Predict Height of a Child 🛉📏🛊**")
    st.text("\n")
    display_pic = Image.open(os.path.join(os.path.join(os.getcwd(), "App_Img_Vid"), "Display_pic_page3.jpg"))
    st.image(display_pic, width=640)
    st.text("\n")


def investigator_inputs():
    """
    Description : This function is creating for collecting the basic details of the person using the app.
    :return: `dataframe`
            investigator_data
    """
    unq_id = st.sidebar.text_input(label="Unique ID", max_chars=15, value="INVST_784456",
                                   help="This field is case sensitive.")
    full_name = st.sidebar.text_input(label="Full Name", max_chars=25, value="Sonal Jain")
    identity = st.sidebar.selectbox(label='Who are you?',
                                    options=('Medicare Provider', 'Trained Prof.', 'Volunteer'),
                                    index=0)
    exp = st.sidebar.slider("Do you have any experience in Child care or nursing?", min_value=0, max_value=40,
                            step=1, value=6)

    investigator_data = pd.DataFrame({'Unique ID               ': unq_id,
                                      'Full Name                      ': full_name,
                                      'Profession              ': identity,
                                      'Experience in Child Care (years)': exp}, index=[''])

    return investigator_data


def highlight_cols(x):
    """
    Description : This function is created for highlighting the dataframe cells.
    :param x: input dataframe that we want to highlight
    :return: highlighted dataframe
    """
    # copy df to new - original data is not changed
    df = x.copy()

    # select all values to no-background color
    df.loc[:, :] = 'background-color: none'

    # return color df
    return df


def display_investigator_info():
    """
    Description : This function is created for displaying the entered investigator details.
    :return: None
    """
    st.markdown("#### User Details 👩‍⚕️")
    inp_investigator_info = investigator_inputs()
    st.dataframe(pd.DataFrame(inp_investigator_info).style.apply(highlight_cols, axis=None))
    st.text("\n")


def upload_new_child_image_flg():
    """
    Description : This function is created for getting the newly uploaded image from the user.
    :return: 'string'
        - upload_flg
    """
    st.markdown("##### Do you want to upload a child depth image❓")
    upload_flg = st.selectbox(label='Upload new image?', options=('Yes', 'No'), index=1)
    return upload_flg


def select_uploaded_images():
    """
    Description : This function is created for selecting the already uploaded image for predictions.
    :return: 'string'
        - upload_flg
    """
    st.markdown("##### Which image you want to select for measuring the height❓")
    all_images_name = ("Image - 1", "Image - 2", "Image - 3", "Image - 4", "Image - 5",
                       "Image - 6", "Image - 7", "Image - 8", "Image - 9")
    img_selection = st.selectbox("Select an image", all_images_name)
    img_index = int(img_selection.split(" - ")[-1])
    return img_index-1

def display_the_image(img_index=0):
    """
    Description : This function is created for displaying the image.
    :param img_index:
    :return:
    """
    # Writing the index of selected image
    st.write("You selected : ", img_index+1)

    # Generating the columns names
    cols = ["f" + str(i) for i in range(1, 2049)]
    cols.insert(0, 'Img_name')
    cols.insert(len(cols), 'Height')

    # Loading the DL features of the provided images
    all_imgs_feats_file = np.load(os.path.join(os.path.join(os.getcwd(), "Unseen_Datafiles"), "all_imgs_df_feats.npz"),
                                  allow_pickle=True)
    all_imgs_feats = all_imgs_feats_file.f.arr_0

    # Assigning the columns some names
    data_df = pd.DataFrame(all_imgs_feats, columns=cols)

    # Name of the image that is selected from the drop-down
    img_name = data_df['Img_name'].iloc[img_index]

    # Displaying the selected image
    img = Image.open(os.path.join(os.path.join(os.getcwd(), "Unseen_Datafiles"), img_name))

    # Tooltip of Generate Prediction button
    gen_pred_tooltip = "Click here to generate the model's predictions on selected image!!"

    # What happens if Generate Predictions button gets clicked
    img_d = st.button("Generate Predictions", key=st.image(img, width=400), help=gen_pred_tooltip)
    if img_d:
        # Loading the Model's predictions
        loaded_preds = pd.read_csv(os.path.join(os.path.join(os.getcwd(), "Unseen_Datafiles"), "Pred_Heights.csv"),
                                   index_col="Unnamed: 0")

        # Printing the results
        st.markdown("###### The possible height of this child is {} cm!!".format(loaded_preds.iloc[img_index].values))
    else:
        st.text(" ")


if __name__ == '__main__':
    # Loading sidebar details
    sidebar()

    # Displaying user/investigator details
    display_investigator_info()

    # Displaying the selected file and showing the predicted height
    img_idx = select_uploaded_images()
    display_the_image(img_idx)
