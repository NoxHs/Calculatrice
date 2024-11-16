import streamlit as st
import re
import pandas as pd
import numpy as np
st.title("Ma calculette")
st.title("Une calculette __:red[simple]__ et :blue[efficace] :sunglasses:")
st.sidebar.image("https://media1.tenor.com/m/5vo_w_jDfwgAAAAC/calculation-math.gif", caption="this is math", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


if 'ecran' not in st.session_state:
    st.session_state['ecran'] = ''


txt = st.text_area(label="Resultat", value=st.session_state["ecran"], disabled=True, placeholder="0")


def reset():
    st.session_state['ecran'] = ''
def calcul():
    st.session_state["ecran"] = re.sub(r'\b0+(\d+)', r'\1', st.session_state["ecran"])
    st.session_state["ecran"] = str(eval(st.session_state["ecran"]))
def add0():
    st.session_state["ecran"] += str(0)
def add1():
    st.session_state["ecran"] += str(1)
def add2():
    st.session_state["ecran"] += str(2)
def add3():
    st.session_state["ecran"] += str(3)
def add4():
    st.session_state["ecran"] += str(4)
def add5():
    st.session_state["ecran"] += str(5)
def add6():
    st.session_state["ecran"] += str(6)
def add7():
    st.session_state["ecran"] += str(7)
def add8():
    st.session_state["ecran"] += str(8)
def add9():
    st.session_state["ecran"] += str(9)
def add_addition():
    st.session_state["ecran"] += ("+")
def add_moins():
    st.session_state["ecran"] += ("-")
def add_division():
    st.session_state["ecran"] += ("/")
def add_multiplication():
    st.session_state["ecran"] += ("*")
button0 ,button1, button2, button3 = st.columns([1,1,1,1])


button0.button("0", on_click=add0)
button1.button("7", on_click=add7)
button2.button("8", on_click=add8)
button3.button("9", on_click=add9)


addition, button4, button5, button6 = st.columns([1,1,1,1])

addition.button("+", on_click=add_addition)
button4.button("4", on_click=add4)
button5.button("5", on_click=add5)
button6.button("6", on_click=add6)


soustraction, button7, button8, button9 = st.columns([1,1,1,1])

soustraction.button(" -- ", on_click=add_moins)
button7.button("1", on_click=add1)
button8.button("2", on_click=add2)
button9.button("3", on_click=add3)

    
multiplication, division, egal = st.columns([1,1,2])

multiplication.button("x", on_click=add_multiplication)
division.button("/", on_click=add_division)
egal.button("=", use_container_width=True, on_click=calcul)

st.button("AC", on_click=reset)



#matplotlib

#plotly
# = st.columns(1,1,1)

