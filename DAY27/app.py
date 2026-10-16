import streamlit as st
import requests
st.set_page_config(
    page_title="Simple API Client",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 Simple API Client")
st.write(
    "A Python and Streamlit application that consumes a "
    "public REST API and displays selected JSON data."
)

st.divider()

BASE_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_user(user_id):
    """
    Fetch user information from the REST API.

    Parameters:
        user_id: ID of the user to retrieve.

    Returns:
        JSON response if successful, otherwise None.
    """

    url = f"{BASE_URL}/{user_id}"

    try:
        response = requests.get(url, timeout=10)

        # Check HTTP status code
        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        st.error("⏱️ Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        st.error(
            "🔌 Could not connect to the API. "
            "Please check your internet connection."
        )

    except requests.exceptions.HTTPError as error:
        st.error(
            f"❌ HTTP error occurred: {error}"
        )

    except requests.exceptions.RequestException as error:
        st.error(
            f"❌ API request failed: {error}"
        )

    except ValueError:
        st.error("❌ The API returned invalid JSON data.")

    return None


st.sidebar.header("⚙️ API Settings")

user_id = st.sidebar.number_input(
    "Enter User ID",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)

fetch_button = st.sidebar.button(
    "🔍 Fetch User",
    use_container_width=True
)

st.subheader("📡 API Information")

st.write(
    "**API:** JSONPlaceholder"
)

st.write(
    "**Endpoint:**"
)

st.code(
    f"{BASE_URL}/{user_id}"
)

if fetch_button:

    with st.spinner("Fetching data from API..."):

        user_data = fetch_user(user_id)

    if user_data:

        st.success("✅ API request successful!")

        st.subheader("👤 User Information")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "User ID",
                user_data.get("id", "N/A")
            )

            st.write("**Name**")
            st.write(user_data.get("name", "N/A"))

            st.write("**Username**")
            st.write(user_data.get("username", "N/A"))

            st.write("**Email**")
            st.write(user_data.get("email", "N/A"))

        with col2:
            st.write("**Phone**")
            st.write(user_data.get("phone", "N/A"))

            st.write("**Website**")
            st.write(user_data.get("website", "N/A"))

            address = user_data.get("address", {})

            st.write("**City**")
            st.write(address.get("city", "N/A"))

            st.write("**Street**")
            st.write(address.get("street", "N/A"))
        company = user_data.get("company", {})

        st.subheader("🏢 Company Information")

        st.write(
            f"**Company:** {company.get('name', 'N/A')}"
        )

        st.write(
            f"**Catch Phrase:** "
            f"{company.get('catchPhrase', 'N/A')}"
        )

        with st.expander("📄 View Raw JSON Response"):

            st.json(user_data)
else:

    st.info(
        "👈 Enter a User ID and click **Fetch User** "
        "to retrieve information from the REST API."
    )
st.divider()

st.subheader("📚 HTTP Status Codes")

st.markdown(
    """
    - **200 OK** → Request was successful
    - **400 Bad Request** → Invalid request
    - **401 Unauthorized** → Authentication required
    - **403 Forbidden** → Access denied
    - **404 Not Found** → Resource does not exist
    - **500 Internal Server Error** → Server-side problem
    """
)
st.divider()

st.caption(
    "Built with Python, Requests, REST API and Streamlit."
)