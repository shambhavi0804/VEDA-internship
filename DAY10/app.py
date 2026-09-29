import streamlit as st

st.set_page_config(
    page_title="Contact Book",
    page_icon="📱",
    layout="centered"
)
if "contacts" not in st.session_state:
    st.session_state.contacts = {
        "9876543210": {
            "name": "Rahul",
            "email": "rahul@example.com"
        },
        "9123456780": {
            "name": "Priya",
            "email": "priya@example.com"
        }
    }

def add_contact(phone, name, email):
    """Add a new contact."""

    if phone in st.session_state.contacts:
        return False, "A contact with this phone number already exists."

    st.session_state.contacts[phone] = {
        "name": name,
        "email": email
    }

    return True, "Contact added successfully."


def search_contact(phone):
    """Search for a contact using phone number."""

    return st.session_state.contacts.get(phone)


def update_contact(phone, name, email):
    """Update an existing contact."""

    if phone not in st.session_state.contacts:
        return False

    st.session_state.contacts[phone] = {
        "name": name,
        "email": email
    }

    return True


def delete_contact(phone):
    """Delete an existing contact."""

    if phone not in st.session_state.contacts:
        return False

    del st.session_state.contacts[phone]
    return True
st.markdown("""
<style>
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .contact-card {
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        border: 1px solid #dddddd;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">📱 Contact Book</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Manage your contacts using Python dictionaries'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

st.sidebar.title("📋 Contact Menu")

operation = st.sidebar.radio(
    "Choose an operation:",
    [
        "📋 View Contacts",
        "➕ Add Contact",
        "🔍 Search Contact",
        "✏️ Update Contact",
        "🗑️ Delete Contact"
    ]
)
if operation == "📋 View Contacts":

    st.header("📋 All Contacts")

    if not st.session_state.contacts:

        st.info("📭 No contacts available.")

    else:

        st.write(
            f"**Total Contacts: "
            f"{len(st.session_state.contacts)}**"
        )

        for phone, details in st.session_state.contacts.items():

            st.markdown(
                f"""
                <div class="contact-card">
                    <b>👤 {details["name"]}</b><br>
                    📞 {phone}<br>
                    📧 {details["email"]}
                </div>
                """,
                unsafe_allow_html=True
            )

elif operation == "➕ Add Contact":

    st.header("➕ Add New Contact")

    name = st.text_input(
        "Contact Name",
        placeholder="Enter contact name"
    )

    phone = st.text_input(
        "Phone Number",
        placeholder="Enter phone number"
    )

    email = st.text_input(
        "Email Address",
        placeholder="Enter email address"
    )

    if st.button(
        "Add Contact",
        use_container_width=True
    ):

        if not name.strip() or not phone.strip():

            st.error(
                "❌ Name and phone number are required."
            )

        elif not phone.isdigit():

            st.error(
                "❌ Phone number should contain only digits."
            )

        else:

            success, message = add_contact(
                phone.strip(),
                name.strip(),
                email.strip()
            )

            if success:
                st.success("✅ " + message)
            else:
                st.error("❌ " + message)

elif operation == "🔍 Search Contact":

    st.header("🔍 Search Contact")

    phone = st.text_input(
        "Enter phone number:",
        placeholder="Example: 9876543210"
    )

    if st.button(
        "Search",
        use_container_width=True
    ):

        if not phone.strip():

            st.warning("Please enter a phone number.")

        else:

            contact = search_contact(phone.strip())

            if contact:

                st.success("✅ Contact found!")

                st.write(
                    f"**Name:** {contact['name']}"
                )

                st.write(
                    f"**Phone:** {phone}"
                )

                st.write(
                    f"**Email:** {contact['email']}"
                )

            else:

                st.error(
                    "❌ Contact not found."
                )

elif operation == "✏️ Update Contact":

    st.header("✏️ Update Contact")

    phone = st.text_input(
        "Enter phone number of contact:",
        placeholder="Example: 9876543210"
    )

    if phone.strip():

        contact = search_contact(phone.strip())

        if contact:

            st.success("Contact found.")

            new_name = st.text_input(
                "New Name",
                value=contact["name"]
            )

            new_email = st.text_input(
                "New Email",
                value=contact["email"]
            )

            if st.button(
                "Update Contact",
                use_container_width=True
            ):

                update_contact(
                    phone.strip(),
                    new_name.strip(),
                    new_email.strip()
                )

                st.success(
                    "✅ Contact updated successfully!"
                )
                st.rerun()

        else:

            st.warning(
                "No contact found with this phone number."
            )
elif operation == "🗑️ Delete Contact":

    st.header("🗑️ Delete Contact")

    phone = st.text_input(
        "Enter phone number:",
        placeholder="Example: 9876543210"
    )

    if st.button(
        "Delete Contact",
        use_container_width=True
    ):

        if delete_contact(phone.strip()):

            st.success(
                "🗑️ Contact deleted successfully!"
            )
            st.rerun()

        else:

            st.error(
                "❌ Contact not found."
            )
st.divider()

st.markdown(
    """
    <div style="text-align:center;">
        🐍 VEDA Internship | Python Programming Track | Day 10<br>
        Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)