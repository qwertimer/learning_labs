import streamlit as st

with st.form(key="hahaha"):
    text_input = st.text_input(label='Enter some text')
    submit_button = st.form_submit_button(label='Submit')

