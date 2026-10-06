import streamlit as st
st.set_page_config(
    page_title="Bank Account Simulator",
    page_icon="🏦",
    layout="centered"
)

if "balance" not in st.session_state:
    st.session_state.balance = 0.0

if "transactions" not in st.session_state:
    st.session_state.transactions = []

def deposit(amount):
    """Add money to the bank account."""
    if amount <= 0:
        return False, "Deposit amount must be greater than ₹0."

    st.session_state.balance += amount

    st.session_state.transactions.append({
        "type": "Deposit",
        "amount": amount,
        "balance": st.session_state.balance
    })

    return True, f"₹{amount:,.2f} deposited successfully."


def withdraw(amount):
    """Withdraw money if sufficient balance is available."""
    if amount <= 0:
        return False, "Withdrawal amount must be greater than ₹0."

    if amount > st.session_state.balance:
        return False, "Insufficient balance. Withdrawal rejected."

    st.session_state.balance -= amount

    st.session_state.transactions.append({
        "type": "Withdrawal",
        "amount": amount,
        "balance": st.session_state.balance
    })

    return True, f"₹{amount:,.2f} withdrawn successfully."


def get_balance():
    """Return current account balance."""
    return st.session_state.balance

st.title("🏦 Bank Account Simulator")

st.write(
    "A simple menu-driven banking application for "
    "deposit, withdrawal, balance inquiry, and transaction history."
)

st.divider()

# Current balance
st.metric(
    "Current Balance",
    f"₹{get_balance():,.2f}"
)

st.sidebar.title("🏦 Banking Menu")

menu = st.sidebar.radio(
    "Select an operation:",
    [
        "Balance Inquiry",
        "Deposit Money",
        "Withdraw Money",
        "Transaction History"
    ]
)

if menu == "Balance Inquiry":

    st.header("💰 Balance Inquiry")

    st.success(
        f"Your current account balance is "
        f"₹{get_balance():,.2f}"
    )

elif menu == "Deposit Money":

    st.header("💵 Deposit Money")

    amount = st.number_input(
        "Enter deposit amount",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    if st.button("Deposit", type="primary"):

        success, message = deposit(amount)

        if success:
            st.success(message)
            st.info(
                f"New Balance: ₹{get_balance():,.2f}"
            )
        else:
            st.error(message)

elif menu == "Withdraw Money":

    st.header("💸 Withdraw Money")

    amount = st.number_input(
        "Enter withdrawal amount",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    if st.button("Withdraw", type="primary"):

        success, message = withdraw(amount)

        if success:
            st.success(message)
            st.info(
                f"Remaining Balance: "
                f"₹{get_balance():,.2f}"
            )
        else:
            st.error(message)

elif menu == "Transaction History":

    st.header("📜 Transaction History")

    if not st.session_state.transactions:

        st.info("No transactions available yet.")

    else:

        for index, transaction in enumerate(
            st.session_state.transactions,
            start=1
        ):

            st.write(
                f"**{index}. {transaction['type']}**"
            )

            st.write(
                f"Amount: ₹{transaction['amount']:,.2f}"
            )

            st.write(
                f"Balance After Transaction: "
                f"₹{transaction['balance']:,.2f}"
            )

            st.divider()

st.sidebar.divider()

if st.sidebar.button("🔄 Reset Account"):

    st.session_state.balance = 0.0
    st.session_state.transactions = []

    st.rerun()