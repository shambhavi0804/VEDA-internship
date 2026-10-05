import streamlit as st
st.set_page_config(
    page_title="Employee Salary Calculator",
    page_icon="💼",
    layout="centered"
)

# Title
st.title("💼 Employee Salary Calculator")
st.write("Calculate gross salary, deductions, and net salary based on configurable salary rules.")

st.divider()

# Salary rules
BASIC_PERCENTAGE = 50
HRA_PERCENTAGE = 20
TA_PERCENTAGE = 10
PF_PERCENTAGE = 12
TAX_PERCENTAGE = 5

def calculate_salary(basic_salary):
    hra = basic_salary * HRA_PERCENTAGE / 100
    ta = basic_salary * TA_PERCENTAGE / 100

    gross_salary = basic_salary + hra + ta

    pf = basic_salary * PF_PERCENTAGE / 100
    tax = gross_salary * TAX_PERCENTAGE / 100

    total_deductions = pf + tax
    net_salary = gross_salary - total_deductions

    return {
        "Basic Salary": basic_salary,
        "HRA": hra,
        "Travel Allowance": ta,
        "Gross Salary": gross_salary,
        "PF": pf,
        "Tax": tax,
        "Total Deductions": total_deductions,
        "Net Salary": net_salary
    }
st.subheader("👤 Employee Details")

employee_name = st.text_input("Employee Name")

basic_salary = st.number_input(
    "Basic Salary (₹)",
    min_value=0.0,
    step=1000.0,
    format="%.2f"
)

# Calculate button
if st.button("Calculate Salary", type="primary"):

    if not employee_name.strip():
        st.warning("Please enter the employee name.")

    elif basic_salary <= 0:
        st.warning("Please enter a valid basic salary greater than 0.")

    else:
        result = calculate_salary(basic_salary)

        st.success(f"Salary calculated successfully for {employee_name}!")

        st.divider()

        # Salary breakdown
        st.subheader("📊 Salary Breakdown")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Basic Salary", f"₹{result['Basic Salary']:,.2f}")
            st.metric("HRA", f"₹{result['HRA']:,.2f}")
            st.metric("Travel Allowance", f"₹{result['Travel Allowance']:,.2f}")
            st.metric("Gross Salary", f"₹{result['Gross Salary']:,.2f}")

        with col2:
            st.metric("PF Deduction", f"₹{result['PF']:,.2f}")
            st.metric("Tax Deduction", f"₹{result['Tax']:,.2f}")
            st.metric("Total Deductions", f"₹{result['Total Deductions']:,.2f}")
            st.metric("Net Salary", f"₹{result['Net Salary']:,.2f}")

        st.divider()

        st.subheader("💰 Final Salary")

        st.success(
            f"Net Salary of {employee_name}: "
            f"₹{result['Net Salary']:,.2f}"
        )

with st.expander("📋 View Salary Rules"):
    st.write(f"**HRA:** {HRA_PERCENTAGE}% of Basic Salary")
    st.write(f"**Travel Allowance:** {TA_PERCENTAGE}% of Basic Salary")
    st.write(f"**PF:** {PF_PERCENTAGE}% of Basic Salary")
    st.write(f"**Tax:** {TAX_PERCENTAGE}% of Gross Salary")