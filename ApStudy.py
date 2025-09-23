import streamlit as st
import random
import pdfplumber
import re

#Load pdf files

def getFrq3():
    with pdfplumber.open('/Users/solo/Desktop/AP Lit Open Prompts.pdf') as litFRQ3:
        pages = litFRQ3.pages
        page = random.choice(pages)
        text = page.extract_text()
        prompts = re.split(r'^\d+[\.\)]\s+', text, flags=re.MULTILINE)
        prompt = random.choice(prompts)
        
        if len(prompts) > 1:
            prompts = prompts[1:]
            

        
        return prompt

def 

st.header("Welcome to your AP Study Library!")

subject = st.selectbox("What AP class do you need to study for?", ["Calc BC", "Calc AB", "CSA", "CSP","Precalc","Stats", "Lit","Lang", "APUSH", "APES"])

if subject == "Lit":
    st.header("AP Lit FRQ3 prompt")
    if st.button("Generate random prompt"):
        st.write(getFrq3())

