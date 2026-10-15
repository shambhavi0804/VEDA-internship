import streamlit as st
from datetime import date, datetime, timedelta
st.set_page_config(
    page_title="Date & Time Utility",
    page_icon="📅",
    layout="centered"
)

st.title("📅 Date & Time Utility")
st.write(
    "A Python and Streamlit utility for calculating age, "
    "date differences, working days, and formatted date/time values."
)

st.divider()

def calculate_age(birth_date):
    """Calculate age from date of birth."""
    today = date.today()

    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


def calculate_date_difference(start_date, end_date):
    """Calculate number of days between two dates."""
    return abs((end_date - start_date).days)


def calculate_working_days(start_date, end_date):
    """Calculate weekdays between two dates."""
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    working_days = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() < 5:
            working_days += 1

        current_date += timedelta(days=1)

    return working_days


def add_days(input_date, number_of_days):
    """Add days to a given date."""
    return input_date + timedelta(days=number_of_days)


def format_datetime_value(input_datetime):
    """Return formatted date and time."""
    return input_datetime.strftime("%d %B %Y, %I:%M:%S %p")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎂 Age Calculator",
    "📆 Date Difference",
    "💼 Working Days",
    "➕ Add / Subtract Days",
    "🕐 Date & Time Formatter"
])

with tab1:
    st.header("🎂 Age Calculator")

    birth_date = st.date_input(
        "Select your date of birth",
        value=date(2000, 1, 1)
    )

    if st.button("Calculate Age", key="age_button"):
        today = date.today()

        if birth_date > today:
            st.error("Birth date cannot be in the future.")
        else:
            age = calculate_age(birth_date)

            st.success(f"Your age is **{age} years**.")

            st.info(
                f"Date of Birth: {birth_date.strftime('%d %B %Y')}\n\n"
                f"Today's Date: {today.strftime('%d %B %Y')}"
            )
with tab2:
    st.header("📆 Date Difference Calculator")

    start_date = st.date_input(
        "Start Date",
        value=date.today(),
        key="start_date"
    )

    end_date = st.date_input(
        "End Date",
        value=date.today(),
        key="end_date"
    )

    if st.button("Calculate Difference", key="difference_button"):

        difference = calculate_date_difference(
            start_date,
            end_date
        )

        st.success(
            f"Difference between the dates: **{difference} days**"
        )

        st.write(
            f"**Start Date:** {start_date.strftime('%d %B %Y')}"
        )

        st.write(
            f"**End Date:** {end_date.strftime('%d %B %Y')}"
        )
with tab3:
    st.header("💼 Working Days Calculator")

    work_start = st.date_input(
        "Starting Date",
        value=date.today(),
        key="work_start"
    )

    work_end = st.date_input(
        "Ending Date",
        value=date.today(),
        key="work_end"
    )

    if st.button("Calculate Working Days", key="working_button"):

        working_days = calculate_working_days(
            work_start,
            work_end
        )

        st.success(
            f"Total working days: **{working_days} days**"
        )

        st.caption(
            "Saturday and Sunday are excluded."
        )
with tab4:
    st.header("➕ Add / Subtract Days")

    selected_date = st.date_input(
        "Select Date",
        value=date.today(),
        key="selected_date"
    )

    number_of_days = st.number_input(
        "Number of Days",
        min_value=-10000,
        max_value=10000,
        value=7,
        step=1
    )

    if st.button("Calculate New Date", key="add_days_button"):

        new_date = add_days(
            selected_date,
            number_of_days
        )

        st.success(
            f"New Date: **{new_date.strftime('%d %B %Y')}**"
        )

        if number_of_days >= 0:
            st.write(
                f"{number_of_days} days were added."
            )
        else:
            st.write(
                f"{abs(number_of_days)} days were subtracted."
            )
with tab5:
    st.header("🕐 Date & Time Formatter")

    selected_datetime = st.datetime_input(
        "Select Date and Time",
        value=datetime.now()
    )

    if st.button("Format Date & Time", key="format_button"):

        formatted_value = format_datetime_value(
            selected_datetime
        )

        st.success("Formatted Date & Time")

        st.code(formatted_value)

        st.write(
            f"**ISO Format:** "
            f"{selected_datetime.isoformat()}"
        )
st.divider()

st.subheader("🕐 Current Date & Time")

current_datetime = datetime.now()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Current Date",
        current_datetime.strftime("%d %B %Y")
    )

with col2:
    st.metric(
        "Current Time",
        current_datetime.strftime("%I:%M:%S %p")
    )

st.caption(
    "Built using Python datetime, timedelta and Streamlit."
)