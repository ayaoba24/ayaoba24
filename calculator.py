import streamlit as st

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal

st.title("Interest Calculator")
st.write("Welcome to the Interest Calculator! This app helps you calculate simple and compound interest based on your inputs.")

st.header("Input Parameters")
principal = st.number_input("Enter the principal amount:", min_value=0.0, format="%.2f")
rate = st.number_input("Enter the annual interest rate (in %):", min_value=0.0, format="%.2f")
time = st.number_input("Enter the time (in years):", min_value=0.0, format="%.2f")

st.header("Calculation Type")
choice = st.radio("Choose the type of interest:", ("Simple", "Compound"))

if st.button("Calculate"):
    st.header("Results")
    if choice == "Simple":
        si = simple_interest(principal, rate, time)
        st.success(f"Simple Interest = ${si:.2f}")
        st.info(f"Total Amount = ${principal + si:.2f}")
    elif choice == "Compound":
        ci = compound_interest(principal, rate, time)
        st.success(f"Compound Interest = ${ci:.2f}")
        st.info(f"Total Amount = ${principal + ci:.2f}")
