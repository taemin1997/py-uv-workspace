

import streamlit as st
import csv
import pandas as pd

if "show" not in st.session_state:
    st.session_state.show = False

with st.form("form", clear_on_submit = True):
    num = st.text_input("학번")
    name = st.text_input("이름")
    major = st.text_input("전공")

    submit = st.form_submit_button("확인")
    button = st.form_submit_button("보여주기/숨기기")

if submit:
    with open("../source/records.csv", "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([num, name, major])

if button:
    st.session_state.show = not st.session_state.show

if st.session_state.show:
    try:
        df = pd.read_csv("../source/records.csv",
                         names=["학번", "이름", "전공"])
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.write("no data")
