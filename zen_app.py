import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import os, urllib
import is_cat 
from PIL import Image
@st.cache
def load_image(img_file):
    img=Image.open(img_file)
    return img

def main():

    st.markdown("# Welcome to Find your soul cat!")
    img_file = st.file_uploader("plik",type=["png","jpg","jpeg"])
    if img_file is not None:
        st.image(load_image(img_file))
        st.write(is_cat.is_cat(load_image(img_file)))
        st.write(is_cat.what_is(load_image(img_file)))

if __name__ == '__main__':
    main()
