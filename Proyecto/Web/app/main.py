import streamlit as st
from classes.components.login import Login
from classes.components.navigation import Navigation


class App:
    def show_page(self):

        obj_navigation = Navigation()
        obj_navigation.render_menu()

    def run(self):

        if "logged_in" not in st.session_state:
            st.session_state["logged_in"] = False

        if st.session_state.logged_in:
            self.show_page()
        else:

            st.title("Sistema De Login")

            username = st.text_input("Nombre de usuario")
            password = st.text_input("Contraseña", type="password")

            if st.button("Iniciar sesión"):

                obj_login = Login(username, password)

                if obj_login.validation_credentials():

                    st.session_state["logged_in"] = True
                    st.experimental_rerun()

                else:
                    st.error("Nombre de usuario o contraseña incorrectos.")


app = App()
app.run()
