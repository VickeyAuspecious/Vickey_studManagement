import streamlit as st
import openpyxl as px

# Load the Excel file
wb = px.load_workbook('users.xlsx')
sheet = wb.active

# Function to check if user exists
def user_exists(username, password):
    for row in sheet.iter_rows(values_only=True):
        if row[0] == username and row[1] == password:
            return True
    return False

# Function to add new user
def add_user(username, password):
    sheet.append([username, password])
    wb.save('users.xlsx')

# Login page
def login_page():
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login', key='login_button'):
        if user_exists(username, password):
            st.success('Logged in successfully')
        else:
            st.error('Invalid username or password')

# Signup page
def signup_page():
    st.title('Signup')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    re_password = st.text_input('Re-enter Password', type='password')
    if st.button('Signup', key='signup_button'):
        if not username or not password or not re_password:
            st.error('Please fill in all fields')
            st.sidebar.subheader('Please fill in all fields')
        elif password!= re_password:
            st.error('Passwords do not match')
        elif user_exists(username, password):
            st.error('Username already exists')
        else:
            add_user(username, password)
            st.success('Account created successfully')
            st.write('Navigate back to login page')

# Navigation
def navigation():
    if st.sidebar.button('Login', key='login_button_nav'):
        login_page()
    elif st.sidebar.button('Signup', key='signup_button_nav'):
        signup_page()

# Show navigation
navigation()