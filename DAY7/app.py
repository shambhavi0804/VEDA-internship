import streamlit as st
import string
st.set_page_config(
    page_title="Password Validator",
    page_icon="🔐",
    layout="centered"
)
st.markdown("""
<style>
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .result {
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
    }

    .requirement {
        padding: 8px;
        margin: 5px 0;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🔐 Password Validator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Check whether your password satisfies the required rules'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

password = st.text_input(
    "Enter your password",
    type="password",
    placeholder="Enter password..."
)

st.subheader("📋 Password Requirements")

st.write("Your password should contain:")

st.write("• At least 8 characters")
st.write("• At least one uppercase letter")
st.write("• At least one lowercase letter")
st.write("• At least one number")
st.write("• At least one special character")

if st.button("🔍 Validate Password", use_container_width=True):

    # Conditions
    length_valid = len(password) >= 8
    uppercase_valid = any(char.isupper() for char in password)
    lowercase_valid = any(char.islower() for char in password)
    digit_valid = any(char.isdigit() for char in password)

    special_valid = any(
        char in string.punctuation for char in password
    )

    # Count valid conditions
    valid_conditions = sum([
        length_valid,
        uppercase_valid,
        lowercase_valid,
        digit_valid,
        special_valid
    ])

    st.divider()

    st.subheader("📊 Validation Result")

    if length_valid:
        st.success("✅ Minimum length requirement satisfied")
    else:
        st.error("❌ Password must contain at least 8 characters")

    if uppercase_valid:
        st.success("✅ Contains an uppercase letter")
    else:
        st.error("❌ Add at least one uppercase letter")

    if lowercase_valid:
        st.success("✅ Contains a lowercase letter")
    else:
        st.error("❌ Add at least one lowercase letter")

    if digit_valid:
        st.success("✅ Contains a number")
    else:
        st.error("❌ Add at least one number")

    if special_valid:
        st.success("✅ Contains a special character")
    else:
        st.error("❌ Add at least one special character")

    st.divider()

    if valid_conditions == 5:

        st.success("🎉 Password is VALID!")

        st.markdown(
            """
            <div class="result">
                <h3>✅ Strong Password</h3>
                <p>Your password satisfies all the required validation rules.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.warning(
            f"⚠️ Password is INVALID. "
            f"{valid_conditions}/5 requirements satisfied."
        )

st.divider()

st.info(
    "🔒 For security, the password is entered using a hidden "
    "password field and is not displayed on the screen."
)

st.markdown(
    """
    <div style="text-align:center; margin-top:30px;">
        🐍 VEDA Internship | Python Programming Track | Day 7
    </div>
    """,
    unsafe_allow_html=True
)