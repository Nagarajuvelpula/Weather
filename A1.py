import streamlit as st
import mysql.connector
import re

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


def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[!@#$%^&*]", password):
        return False
    return True


def validate_name(name):
    if not re.match(r"^[A-Za-z]+$", name):
        return False
    return True


def validate_phone_number(ph_number):
    if len(ph_number) != 10:
        return False
    if not ph_number.isdigit():
        return False
    return True


def register():
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    user_name = st.text_input("User Name")
    ph_number = st.text_input("Phone Number")
    password = st.text_input("Password", type="password")
    conform_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if not all([first_name, last_name, user_name, ph_number, password, conform_password]):
            st.error("Please fill all the fields")
            return
        if not validate_name(first_name):
            st.error("Invalid first name. Please enter characters only")
            return
        if not validate_name(last_name):
            st.error("Invalid last name. Please enter characters only")
            return
        if password != conform_password:
            st.error("Passwords don't match")
            return
        if not validate_password(password):
            st.error("Invalid password. It should have at least 8 characters, one special character, and one uppercase letter")
            return
        if not validate_phone_number(ph_number):
            st.error("Invalid phone number. Please enter 10 digits")
            return

        query = "SELECT * FROM users_1 WHERE user_name = %s"
        values = (user_name,)
        cursor.execute(query, values)
        existing_user = cursor.fetchone()
        if existing_user:
            st.error("User already exists")
            return

        query = "INSERT INTO users_1 (first_name, last_name, user_name, ph_number, password, conform_password) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, user_name, ph_number, password, conform_password)

        if execute_query(query, values):
            st.success("Registered successfully")
            st.text_input("First Name", value="")
            st.text_input("Last Name", value="")
            st.text_input("User Name", value="")
            st.text_input("Phone Number", value="")
            st.text_input("Password", type="password", value="")
            st.text_input("Confirm Password", type="password", value="")
        else:
            st.error("Registration failure")


if __name__ == "__main__":
    st.title("Registration Page")
    register()
