#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import subprocess
import os

st.title("AI Decision Intelligence Dashboard")

uploaded_file = st.file_uploader(
    "Upload your dataset (.xlsx)", type=["xlsx"]
)

if uploaded_file:
    with open("input.xlsx", "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Generate Dashboard"):
        st.write("Processing...")

        # run your pipeline
        subprocess.run(["python", "ai_decision_pipeline.py"])

        st.success("Dashboard Generated!")

        with open("AI_Decision_Intelligence_Report.xlsx", "rb") as file:
            st.download_button(
                label="Download Dashboard",
                data=file,
                file_name="AI_Decision_Intelligence_Report.xlsx"
            )

