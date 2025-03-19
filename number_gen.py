import streamlit as st
import random

st.header("This is Number Guessing Game on Streamlit 🏆")

st.title("Rules Of This Game")
st.subheader("1. Guess Between 1 to 5 number.")
st.subheader(" 2. Not Guess 0 number this number is not allowed to guess.")

generate_random_number=(int(random.randint(1,5)))
user_guess=st.number_input("Guess your Number")


if st.button("Check your Guess number"):
        if(user_guess !=0):
            if(user_guess==generate_random_number):
               st.subheader("Congratulation you guess the right number  😍")
            else:
               st.subheader("You Are Not Guess the Right Number try Again 😪")
else:
    st.header("Zero is Not Allow")
   