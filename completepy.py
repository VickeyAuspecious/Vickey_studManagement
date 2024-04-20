import streamlit as st

# Navigation bar
def navigation():
    st.sidebar.title('Navigation')
    if st.sidebar.button('Nav1', key='nav1_button'):
        nav1_page()
    elif st.sidebar.button('Nav2', key='nav2_button'):
        nav2_page()

# Login page
def login_page():
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login', key='login_button'):
        if username == 'test' and password == 'test@123':
            st.success('Logged in successfully')
            
            st.title('Dashboard')
            navigation()
        else:
            st.error('Invalid username or password')

# Nav1 page
def nav1_page():
    st.title('Nav1')
    st.write('Welcome to Nav1!')

# Nav2 page
def nav2_page():
    st.title('Nav2')
    st.write('Welcome to Nav2!')

# Show navigation
navigation()
login_page()