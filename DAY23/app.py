import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# ---------------------------------------------------------
# File Configuration
# ---------------------------------------------------------

DATA_FILE = Path("expenses.csv")

CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Bills",
    "Entertainment",
    "Healthcare",
    "Education",
    "Rent",
    "Other"
]


# ---------------------------------------------------------
# Data Functions
# ---------------------------------------------------------

def load_expenses():
    """Load expense records from CSV file."""

    if DATA_FILE.exists():
        try:
            df = pd.read_csv(DATA_FILE)

            if not df.empty:
                df["Date"] = pd.to_datetime(
                    df["Date"],
                    errors="coerce"
                ).dt.date

                df["Amount"] = pd.to_numeric(
                    df["Amount"],
                    errors="coerce"
                ).fillna(0)

            return df

        except Exception:
            return pd.DataFrame(
                columns=["Date", "Category", "Description", "Amount"]
            )

    return pd.DataFrame(
        columns=["Date", "Category", "Description", "Amount"]
    )


def save_expenses(df):
    """Save expense records to CSV."""

    df.to_csv(DATA_FILE, index=False)


def add_expense(expense_date, category, description, amount):
    """Add a new expense."""

    df = load_expenses()

    new_expense = pd.DataFrame([
        {
            "Date": expense_date,
            "Category": category,
            "Description": description,
            "Amount": amount
        }
    ])

    df = pd.concat(
        [df, new_expense],
        ignore_index=True
    )

    save_expenses(df)


def calculate_total(df):
    """Calculate total spending."""

    if df.empty:
        return 0.0

    return float(df["Amount"].sum())


def category_summary(df):
    """Generate category-wise spending."""

    if df.empty:
        return pd.DataFrame(
            columns=["Category", "Amount"]
        )

    summary = (
        df.groupby("Category")["Amount"]
        .sum()
        .reset_index()
        .sort_values(
            by="Amount",
            ascending=False
        )
    )

    return summary


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("💰 Simple Expense Tracker")
st.write(
    "Track your daily expenses and understand "
    "where your money is going."
)

st.divider()

# ---------------------------------------------------------
# Load Data
# ---------------------------------------------------------

df = load_expenses()

# ---------------------------------------------------------
# Sidebar - Add Expense
# ---------------------------------------------------------

with st.sidebar:

    st.header("➕ Add Expense")

    expense_date = st.date_input(
        "Expense Date",
        value=date.today()
    )

    category = st.selectbox(
        "Category",
        CATEGORIES
    )

    description = st.text_input(
        "Description",
        placeholder="Example: Lunch at restaurant"
    )

    amount = st.number_input(
        "Amount (₹)",
        min_value=0.0,
        step=10.0,
        format="%.2f"
    )

    add_button = st.button(
        "Add Expense",
        use_container_width=True,
        type="primary"
    )

    if add_button:

        if amount <= 0:
            st.error("Expense amount must be greater than ₹0.")

        elif not description.strip():
            st.error("Please enter an expense description.")

        else:
            add_expense(
                expense_date,
                category,
                description.strip(),
                amount
            )

            st.success("Expense added successfully!")

            st.rerun()


# ---------------------------------------------------------
# Dashboard Metrics
# ---------------------------------------------------------

total_spending = calculate_total(df)

expense_count = len(df)

average_expense = (
    total_spending / expense_count
    if expense_count > 0
    else 0
)

highest_expense = (
    df["Amount"].max()
    if not df.empty
    else 0
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Spending",
        f"₹{total_spending:,.2f}"
    )

with col2:
    st.metric(
        "Total Expenses",
        expense_count
    )

with col3:
    st.metric(
        "Average Expense",
        f"₹{average_expense:,.2f}"
    )

with col4:
    st.metric(
        "Highest Expense",
        f"₹{highest_expense:,.2f}"
    )

st.divider()

# ---------------------------------------------------------
# Expense Records
# ---------------------------------------------------------

st.subheader("📋 Expense Records")

if df.empty:

    st.info(
        "No expenses recorded yet. "
        "Use the sidebar to add your first expense."
    )

else:

    display_df = df.copy()

    display_df["Date"] = pd.to_datetime(
        display_df["Date"]
    ).dt.strftime("%Y-%m-%d")

    display_df["Amount"] = display_df[
        "Amount"
    ].apply(
        lambda x: f"₹{x:,.2f}"
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

# ---------------------------------------------------------
# Category Summary
# ---------------------------------------------------------

st.divider()

st.subheader("📊 Category-wise Spending")

summary = category_summary(df)

if summary.empty:

    st.info("Category spending data will appear here.")

else:

    col1, col2 = st.columns(2)

    with col1:

        chart_data = summary.set_index("Category")

        st.bar_chart(
            chart_data["Amount"]
        )

    with col2:

        summary_display = summary.copy()

        summary_display["Amount"] = summary_display[
            "Amount"
        ].apply(
            lambda x: f"₹{x:,.2f}"
        )

        st.dataframe(
            summary_display,
            use_container_width=True,
            hide_index=True
        )

# ---------------------------------------------------------
# Category Filter
# ---------------------------------------------------------

st.divider()

st.subheader("🔎 Filter Expenses")

if not df.empty:

    selected_category = st.selectbox(
        "Select Category",
        ["All Categories"] + CATEGORIES
    )

    if selected_category == "All Categories":
        filtered_df = df
    else:
        filtered_df = df[
            df["Category"] == selected_category
        ]

    st.write(
        f"Showing **{len(filtered_df)}** expense record(s)"
    )

    filtered_display = filtered_df.copy()

    filtered_display["Date"] = pd.to_datetime(
        filtered_display["Date"]
    ).dt.strftime("%Y-%m-%d")

    filtered_display["Amount"] = filtered_display[
        "Amount"
    ].apply(
        lambda x: f"₹{x:,.2f}"
    )

    st.dataframe(
        filtered_display,
        use_container_width=True,
        hide_index=True
    )

# ---------------------------------------------------------
# Clear Data
# ---------------------------------------------------------

st.divider()

st.subheader("⚙️ Data Management")

if not df.empty:

    if st.button(
        "🗑️ Clear All Expenses",
        type="secondary"
    ):

        DATA_FILE.unlink(missing_ok=True)

        st.success(
            "All expense records have been deleted."
        )

        st.rerun()

else:

    st.caption("No data available to delete.")

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.caption(
    "Task 23 | Simple Expense Tracker | "
    "Python + Streamlit"
)