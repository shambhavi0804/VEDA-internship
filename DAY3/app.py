import streamlit as st

st.set_page_config(
    page_title="Even or Odd Checker",
    page_icon="🔢"
)

st.title("🔢 Even and Odd Number Checker")
st.write("Enter a number to check whether it is even or odd.")

number = st.number_input(
    "Enter a number:",
    value=0,
    step=1
)

if st.button("Check Number"):
    if number % 2 == 0:
        st.success(f"✅ {int(number)} is an Even Number.")
    else:
        st.warning(f"🔸 {int(number)} is an Odd Number.")

st.divider()

st.subheader("Examples")

col1, col2 = st.columns(2)

with col1:
    st.info("Even Number Example")
    st.write("Input: **10**")
    st.success("10 is an Even Number.")

with col2:
    st.info("Odd Number Example")
    st.write("Input: **7**")
    st.warning("7 is an Odd Number.")