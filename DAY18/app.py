import streamlit as st

st.set_page_config(
    page_title="Exception Handling Practice",
    page_icon="⚠️",
    layout="centered"
)

st.title("⚠️ Exception Handling Practice")
st.write("Practice handling common Python exceptions using Streamlit.")

st.divider()

st.subheader("1. Numeric Input Validation")

number_input = st.text_input(
    "Enter a number:",
    placeholder="Example: 25"
)

if st.button("Check Number"):
    try:
        number = int(number_input)

        if number < 0:
            raise ValueError("Negative numbers are not allowed.")

    except ValueError as e:
        st.error(f"❌ Value Error: {e}")

    else:
        st.success(f"✅ Valid number: {number}")

    finally:
        st.info("Operation completed.")


st.divider()

st.subheader("2. Division Calculator")

col1, col2 = st.columns(2)

with col1:
    first_number = st.number_input(
        "First Number",
        value=10.0
    )

with col2:
    second_number = st.number_input(
        "Second Number",
        value=2.0
    )

if st.button("Divide"):
    try:
        result = first_number / second_number

    except ZeroDivisionError:
        st.error("❌ Cannot divide by zero.")

    except TypeError:
        st.error("❌ Invalid data type.")

    else:
        st.success(f"✅ Result: {result:.2f}")

    finally:
        st.info("Division operation completed.")


st.divider()

st.subheader("3. List Access")

items = ["Python", "Streamlit", "Git", "GitHub"]

index = st.number_input(
    "Enter an index (0-3):",
    min_value=0,
    max_value=10,
    value=0,
    step=1
)

if st.button("Access Item"):
    try:
        item = items[index]
        st.success(f"✅ Item: {item}")

    except IndexError:
        st.error("❌ Index Error: Index is outside the list range.")

    finally:
        st.info("List access operation completed.")


st.divider()

st.subheader("4. Dictionary Key Handling")

student = {
    "name": "Shambhavi",
    "course": "Computer Science",
    "skill": "Python"
}

key = st.text_input(
    "Enter a key:",
    placeholder="Example: name"
)

if st.button("Find Key"):
    try:
        value = student[key]

    except KeyError:
        st.error(f"❌ Key Error: '{key}' does not exist.")

    else:
        st.success(f"✅ Value: {value}")

    finally:
        st.info("Dictionary operation completed.")


st.divider()

st.subheader("Exceptions Covered")

st.markdown("""
- **ValueError** – Invalid numeric or value input
- **ZeroDivisionError** – Division by zero
- **IndexError** – Accessing an invalid list index
- **KeyError** – Accessing a missing dictionary key
- **TypeError** – Invalid data type operation
- **finally** – Executes whether an exception occurs or not
- **else** – Executes when no exception occurs
""")

st.success("🎯 Exception handling practice completed!")