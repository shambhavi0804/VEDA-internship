import streamlit as st
import secrets
import string

st.set_page_config(
    page_title="Secure Password Generator",
    page_icon="🔐",
    layout="centered"
)

def generate_password(length, use_uppercase, use_lowercase,
                      use_numbers, use_special):

    character_sets = []

    if use_lowercase:
        character_sets.append(string.ascii_lowercase)

    if use_uppercase:
        character_sets.append(string.ascii_uppercase)

    if use_numbers:
        character_sets.append(string.digits)

    if use_special:
        character_sets.append(string.punctuation)

    if not character_sets:
        return None

    # Combine all selected character sets
    all_characters = "".join(character_sets)

    # Guarantee at least one character from each selected type
    password_characters = [
        secrets.choice(character_set)
        for character_set in character_sets
    ]

    # Fill the remaining positions securely
    remaining_length = length - len(password_characters)

    password_characters.extend(
        secrets.choice(all_characters)
        for _ in range(remaining_length)
    )

    # Securely shuffle the password
    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)

st.title("🔐 Secure Password Generator")

st.write(
    "Generate strong and configurable passwords using Python's "
    "`secrets` module."
)

st.divider()

st.subheader("⚙️ Password Configuration")

length = st.slider(
    "Password Length",
    min_value=8,
    max_value=64,
    value=16,
    step=1
)

st.write("Select the character types to include:")

use_lowercase = st.checkbox(
    "Lowercase letters (a-z)",
    value=True
)

use_uppercase = st.checkbox(
    "Uppercase letters (A-Z)",
    value=True
)

use_numbers = st.checkbox(
    "Numbers (0-9)",
    value=True
)

use_special = st.checkbox(
    "Special characters (!@#$...)",
    value=True
)

if st.button("🔑 Generate Password", use_container_width=True):

    selected_types = sum([
        use_lowercase,
        use_uppercase,
        use_numbers,
        use_special
    ])

    if selected_types == 0:

        st.error(
            "Please select at least one character type."
        )

    elif length < selected_types:

        st.error(
            f"Password length must be at least "
            f"{selected_types} characters."
        )

    else:

        password = generate_password(
            length,
            use_uppercase,
            use_lowercase,
            use_numbers,
            use_special
        )

        st.success("Password generated successfully!")

        st.code(
            password,
            language=None
        )

        st.info(
            "For security, this application does not store or "
            "automatically log generated passwords."
        )

st.divider()

st.subheader("🛡️ Security Information")

st.markdown("""
- Uses Python's **`secrets` module** for security-sensitive randomness.
- Does not automatically save generated passwords.
- Does not log generated passwords.
- Supports multiple character types.
- Avoids predictable password patterns.
- Users should store passwords using a trusted password manager.
""")

st.caption(
    "Day 31 — VEDA Python Programming Track"
)