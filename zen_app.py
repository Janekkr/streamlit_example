import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import os
import front.is_cat as is_cat 
from PIL import Image
@st.cache
def load_image(img_file):
    img=Image.open(img_file)
    return img
@st.cache
def find_similar(img_file):
    files=[Image.open(f) for f in os.listdir("Korat")]
    return files
def main():

    st.markdown("# Welcome to Find your soul cat!")
    img_file = st.file_uploader("plik",type=["png","jpg","jpeg"])
    if img_file is not None:
        st.image(load_image(img_file))
        st.write(is_cat.is_cat(load_image(img_file)))
        st.write(is_cat.what_is(load_image(img_file)))
        for f in find_similar(img_file):
            st.image(load_image(f))

    st.markdown("# End of site bye bye!")

if __name__ == '__main__':
    main()
