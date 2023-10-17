import streamlit as st

st.title("Roteiro 1: Primeiros Passos com Streamlit")

title = st.text_input('my team')
if st.button("Clique-me"):
    st.write('my team is', title)


    