import streamlit as st

st.title("Grand Stay Hotel Management System - Prototype")

st.header("Login")
st.text_input("Username")
st.text_input("Password", type="password")
st.button("Login")

st.divider()

st.header("Make Reservation")
st.selectbox("Room Type", ["Single", "Double", "Suite", "Deluxe"])
st.date_input("Check-in Date")
st.date_input("Check-out Date")
st.button("Book Room")

st.divider()

st.header("Invoice & Payment")
st.write("Total Amount: RM 450")
st.button("Make Payment")
