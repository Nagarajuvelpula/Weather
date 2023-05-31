import streamlit as st
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nagaraju@123",
    database="register_1"
)
cursor = db.cursor()


def execute_query(query, values=None):
    try:
        cursor.execute(query, values)
        db.commit()
        return True
    except mysql.connector.Error as error:
        print("Error:", error)
        db.rollback()
        return False


def login():
    user_name = st.text_input("User Name", key="user_name")
    password = st.text_input("Password", type="password", key="password")

    if st.button("Login"):
        if not all([user_name, password]):
            st.error("Please enter correct username or password")
            return

        query = "SELECT * FROM users_1 WHERE user_name = %s AND password = %s"
        values = (user_name, password)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            st.success("Login successful")
            st.write("User ID:", result[0])
            st.write("First Name:", result[1])
            st.write("Last Name:", result[2])

            # Clear the input fields
            st.session_state.user_name = ""
            st.session_state.password = ""
        else:
            st.warning("Invalid username or password")


st.title("Login Page")
login()


