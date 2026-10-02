import streamlit as st
import math

st.set_page_config(
    page_title="Prime Number Analyzer",
    page_icon="🔢",
    layout="centered"
)

st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .prime-result {
        padding: 18px;
        border-radius: 10px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
    }

    .section-title {
        font-size: 24px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="main-title">🔢 Prime Number Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Check prime numbers and generate primes within a range'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

def is_prime(number):
    """
    Returns True if the number is prime,
    otherwise returns False.
    """

    # Numbers less than 2 are not prime
    if number < 2:
        return False

    # 2 is the only even prime number
    if number == 2:
        return True

    # Other even numbers are not prime
    if number % 2 == 0:
        return False

    # Check only odd divisors up to square root
    limit = math.isqrt(number)

    for divisor in range(3, limit + 1, 2):
        if number % divisor == 0:
            return False

    return True
st.markdown(
    '<div class="section-title">🔍 Prime Number Checker</div>',
    unsafe_allow_html=True
)

number = st.number_input(
    "Enter a number:",
    min_value=0,
    step=1,
    value=17
)

if st.button("Check Prime", use_container_width=True):

    number = int(number)

    if is_prime(number):
        st.success(f"🎉 {number} is a PRIME number.")

        st.markdown(
            f'<div class="prime-result">✅ {number} is PRIME</div>',
            unsafe_allow_html=True
        )

    else:
        st.error(f"❌ {number} is not a prime number.")

        st.markdown(
            f'<div class="prime-result">❌ {number} is NOT PRIME</div>',
            unsafe_allow_html=True
        )

st.divider()

st.markdown(
    '<div class="section-title">📊 Prime Number Range Generator</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    start = st.number_input(
        "Starting number:",
        min_value=0,
        step=1,
        value=1
    )

with col2:
    end = st.number_input(
        "Ending number:",
        min_value=0,
        step=1,
        value=50
    )

if st.button("Generate Prime Numbers", use_container_width=True):

    start = int(start)
    end = int(end)

    if start > end:
        st.warning(
            "⚠️ Starting number must be less than or equal to ending number."
        )

    else:
        prime_numbers = []

        for number in range(start, end + 1):
            if is_prime(number):
                prime_numbers.append(number)

        if prime_numbers:
            st.success(
                f"✅ Found {len(prime_numbers)} prime number(s)."
            )

            st.subheader("Prime Numbers")

            st.write(prime_numbers)

            st.divider()

            st.subheader("📋 Prime Number Details")

            for prime in prime_numbers:
                st.write(f"• {prime}")

        else:
            st.info(
                "ℹ️ No prime numbers were found in this range."
            )

st.divider()

st.subheader("💡 Examples")

st.write("✅ **2** → Prime")
st.write("✅ **7** → Prime")
st.write("✅ **13** → Prime")
st.write("❌ **1** → Not Prime")
st.write("❌ **10** → Not Prime")
st.write("❌ **0** → Not Prime")

st.divider()


st.subheader("🧠 Algorithm")

st.write("""
A number is prime if it is greater than 1 and has no divisors
other than 1 and itself. The program first handles values below
2 and the special case of 2. It then eliminates other even
numbers and checks only odd divisors up to the square root of
the number. This avoids unnecessary divisibility checks and
makes the prime-checking process more efficient.
""")

st.divider()

st.markdown(
    """
    <div style="text-align:center;">
        🐍 VEDA Internship | Python Programming Track | Day 13<br>
        Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)