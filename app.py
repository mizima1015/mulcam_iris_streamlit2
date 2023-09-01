# -*- coding:utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import plotly as plt
import sklearn as skl
import matplotlib.pyplot as plt

def main():

    st.markdown("# Hello World")
    
    menu = ["Home","탐색적 자료 분석", "머신러닝", "About"]
    choice = st.sidebar.selectbox("메뉴",menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "탐색적 자료 분석":
        st.subheader("탐색석 자료 분석")
    elif choice == "머신러닝":
        st.subheader("머신러닝")
    elif choice == "About":
        st.subheader("About")
    else:
        pass
    

if __name__ == "__main__":
    main()