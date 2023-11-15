# Importing packages
import streamlit as st
from admin import main1
from security import main2
import base64

# Function to set background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/gif;base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image
add_bg_from_local('car.gif')

# Main function for user login and navigation
def main():
    st.title("ParkEase")
    navigate = ["Admin Login", "Security Guard Login"]
    choice = st.sidebar.radio("User Login", navigate)

    if choice == "Admin Login":
        form = st.form(key='my_form')
        username = form.text_input(label='Enter Admin Username')
        password = form.text_input('Enter Admin Password', type='password')
        submit_button = form.form_submit_button(label='Submit')
        if username == 'admin' and password == 'admin123':
            main1()
        else:
            st.error('Please enter a valid input', icon='🚨')

    elif choice == "Security Guard Login":
        form = st.form(key='my_form')
        username = form.text_input(label='Enter Username')
        password = form.text_input(label='Enter Password', type='password')
        submit_button = form.form_submit_button(label='Submit')
        if username == 'security' and password == 'guard123':
            main2()
        else:
            st.error('Please enter a valid input', icon='🚨')

if __name__ == '__main__':
    main()
