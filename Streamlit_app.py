import streamlit as st

# Set page title
st.set_page_config(page_title="Science Website")

# Add header
st.title("Welcome to our Science Website")

# Add sidebar with options
menu = ["Home", "About Us", "Contact Us"]
choice = st.sidebar.selectbox("Select an option", menu)

# Display content based on user's choice
if choice == "Home":
    st.write("This is the homepage of our science website.")
elif choice == "About Us":
    st.write("We are a team of scientists dedicated to advancing the field of science.")
else:
    st.write("Please fill out the contact form on our website to get in touch with us.")

# Add footer
st.text("")
st.text("")
st.text("")
st.text("Created by [Your Name]")
