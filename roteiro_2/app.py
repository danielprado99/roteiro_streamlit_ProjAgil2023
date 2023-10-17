import streamlit as st

st.title("Roteiro 2: Widgets Interativos")

on = st.toggle('Mostrar opções')

if on:
    st.write('Opções mostradas!')


    value = st.slider("Escolha um valor", 0, 100)
    agree = st.checkbox('Eu concordo')
    times = st.radio(
        "Qual seu time favorito?",
        [":rainbow[fluminense]", "***VASCO***", "flamengo"],
        index=None,
    )

    opções = st.selectbox(
        'Qual time é o melhor?',
        ('Vasco', 'Flamengo', 'Fluminense'))



    if st.button("Mostrar valores"):
        st.write(f"Valor escolhido: {value}")

        if agree:
            st.write('Ótimo!')

        st.write("Seu time é:", times)

        st.write('o melhor time é:', opções)