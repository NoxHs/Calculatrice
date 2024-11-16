import streamlit as st

st.write("Calculatrice ")

nb1, choix, nb2 = st.columns([2,6,2])

nb1 = nb1.number_input("Nombre 1")
nb2 = nb2.number_input("Nombre 2")

option = choix.selectbox(
    "Opération",
    ("Addition", "Soustraction", "Multiplication", "Division"),
    index=None,
    placeholder="Selectionnez...",
)



if st.button("Résultat"):
    result = 0
    if option =="Addition":
        result = (f"Résultat : {int(nb1) + int(nb2)}")
    elif option =="Soustraction":
        result = (f"Résultat : {int(nb1) - int(nb2)}")
    elif option =="Multiplication":
        result = (f"Résultat : {int(nb1) * int(nb2)}")
    elif option =="Division":
        result = (f"Résultat : {int(nb1) / int(nb2)}")
    resultat =st.empty()
    resultat.text_area(label="Résultat :", value =result,disabled=True )