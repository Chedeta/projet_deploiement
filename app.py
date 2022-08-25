import page1
import page2
import streamlit as st
PAGES = {
    "Dashboard": page1,
    "Prédiction": page2,
}
st.sidebar.title('Navigation : ')
selection = st.sidebar.selectbox("Aller :", PAGES.keys())
page = PAGES[selection]
page.app()
