import streamlit as st 
import time 

st.set_page_config(page_title = "Para mi princesita bonita", page_icon = "💖", layout = "centered")

st.markdown("""
    <style>
    .main {
        background-color: #ffe4e1;
    }
    .letter-box {
        background-color: #fffafa;
        padding: 40px;
        border-radius: 15px;
        border: 2px solid #ffb6c1;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        font-family: 'Georgia', serif;
        color: #4a4a4a;
        line-height: 1.6;
    }
    .heart {
        color: #ff4b4b;
        font-size: 50px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

if "opened" not in st.session_state:
    st.session_state.opened = False

st.write("# 💌 Solo por bonita 💖")

if not st.session_state.opened: 
    st.write("### Toca el corazón para abrir amor")
    if st.button("💖"):
        st.session_state.opened = True 
        st.balloons()
        st.rerun()
else: 
    with st.container():
        st.markdown('<div class = "letter-box"', unsafe_allow_html=True)

        st.subheader("Mi mujer linda y mi mundo entero, ")

        texto_carta = """
        Simplemente amor mío me gusta recordarte cuanto te amo, puede que sea un día normal,
        pero eso no quita que todos los días tu los haces especiales porque te tengo a ti en mi vida amor.

        Quiero expresarte que a pesar de que muchas veces que nos vemos el tiempo es muy corto tu me lo puedes
        solucionar todo con una sonrisa amor, jamás me imaginé que tan pronto se halla podido tener algo tan 
        bonito entre los dos amor, que con el poquito tiempo que llevamos ya te llevaste todo mi corazón 
        y espero que te lo quedes, te lo regalo con la condición de que nos amemos mucho incondicionalmente 
        e infinitamente. 
        
        Amor siempre estas en mi mente así no te escriba, así me sienta mal, así no te pueda ir a ver; 
        siempre anhelando el momento en que pueda volver a abrazarte, volver a tenerte y besarte. Eres mi mayor anhelo
        y mi bonito presente, eres mi orgullo y eres una respuesta de Dios. No lo pensaba pero te necesitaba y te necesito
        y ahora no puedo sin ti amor. 
        
        Espero sepas que doy todo por ti y por tu amor siempre, sin importar que y que voy a estar para ti pase lo que pase
        y sientas como te sientas, porque te amo y estoy dispuesto a todo por tu amor.

        Te amo con todo mi corazón,
        **Tomás**
        """

        placeholder = st.empty()
        full_text = ""
        for char in texto_carta:
            full_text += char
            placeholder.markdown(full_text + "▌")
            time.sleep(0.02) # Velocidad de escritura
        placeholder.markdown(full_text)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("Cerrar carta"):
            st.session_state.opened = False
            st.rerun()
