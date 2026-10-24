import streamlit as st
import json
import os
from datetime import date
import pandas as pd

st.set_page_config(
    page_title="Veda Technology Business Management",
    page_icon="💻",
    layout="wide"
)

DATA_DIR = "data"

SERVICES_FILE = os.path.join(DATA_DIR, "services.json")
PROGRAMS_FILE = os.path.join(DATA_DIR, "programs.json")
INTERNSHIPS_FILE = os.path.join(DATA_DIR, "internships.json")
INQUIRIES_FILE = os.path.join(DATA_DIR, "inquiries.json")
REQUESTS_FILE = os.path.join(DATA_DIR, "requests.json")

def ensure_data_directory():
    """Create data directory if it does not exist."""
    os.makedirs(DATA_DIR, exist_ok=True)


def load_data(filename, default=None):
    """Load data from JSON file."""
    if default is None:
        default = []

    if not os.path.exists(filename):
        return default

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return default


def save_data(filename, data):
    """Save data to JSON file."""
    ensure_data_directory()

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def generate_id(records, prefix):
    """Generate a simple unique ID."""
    return f"{prefix}{len(records) + 1:03d}"


ensure_data_directory()

services = load_data(SERVICES_FILE)
programs = load_data(PROGRAMS_FILE)
internships = load_data(INTERNSHIPS_FILE)
inquiries = load_data(INQUIRIES_FILE)
requests = load_data(REQUESTS_FILE)

st.title("💻 Veda Technology")
st.subheader("Business & Service Management System")

st.markdown(
    """
    Manage digital services, technology programs, training programs,
    internships, customer inquiries and service requests from one
    centralized application.
    """
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Dashboard",
        "💻 Services",
        "🎓 Programs",
        "👨‍💻 Internships",
        "📩 Customer Inquiries",
        "🛠️ Service Requests",
        "📊 Reports"
    ]
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.header("📊 Business Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Digital Services",
        len(services)
    )

    col2.metric(
        "Technology Programs",
        len(programs)
    )

    col3.metric(
        "Internship Programs",
        len(internships)
    )

    col4.metric(
        "Customer Inquiries",
        len(inquiries)
    )

    st.divider()

    col5, col6 = st.columns(2)

    col5.metric(
        "Service Requests",
        len(requests)
    )

    active_services = len(
        [s for s in services if s.get("status") == "Active"]
    )

    col6.metric(
        "Active Services",
        active_services
    )

    st.divider()

    st.subheader("🏢 About Veda Technology")

    st.write(
        """
        Veda Technology is represented in this project as a technology
        and digital-services organization. The system provides a simple
        way to manage services, programs, training, internships,
        customer inquiries and service requests.
        """
    )

    st.info(
        "Use the navigation menu on the left to manage different business modules."
    )


# ============================================================
# SERVICES
# ============================================================

elif page == "💻 Services":

    st.header("💻 Digital Service Management")

    tab1, tab2 = st.tabs(
        ["➕ Add Service", "📋 View Services"]
    )

    with tab1:

        with st.form("service_form"):

            service_name = st.text_input(
                "Service Name"
            )

            category = st.selectbox(
                "Category",
                [
                    "Web Development",
                    "Software Development",
                    "AI & Machine Learning",
                    "Cloud Services",
                    "Data Analytics",
                    "Cybersecurity",
                    "Digital Marketing",
                    "Other"
                ]
            )

            description = st.text_area(
                "Service Description"
            )

            price = st.number_input(
                "Service Price (₹)",
                min_value=0.0,
                step=500.0
            )

            status = st.selectbox(
                "Status",
                ["Active", "Inactive"]
            )

            submitted = st.form_submit_button(
                "Add Service"
            )

            if submitted:

                if not service_name.strip():
                    st.error("Please enter a service name.")

                elif not description.strip():
                    st.error("Please enter a service description.")

                else:

                    service = {
                        "id": generate_id(services, "SER"),
                        "name": service_name,
                        "category": category,
                        "description": description,
                        "price": price,
                        "status": status,
                        "created_date": str(date.today())
                    }

                    services.append(service)

                    save_data(
                        SERVICES_FILE,
                        services
                    )

                    st.success(
                        "Service added successfully!"
                    )

    with tab2:

        st.subheader("Available Services")

        if services:

            search = st.text_input(
                "🔎 Search Services"
            )

            filtered_services = services

            if search:

                search = search.lower()

                filtered_services = [
                    service
                    for service in services
                    if search in service["name"].lower()
                    or search in service["category"].lower()
                ]

            df = pd.DataFrame(filtered_services)

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.info(
                "No services available. Add your first service."
            )


# ============================================================
# PROGRAMS
# ============================================================

elif page == "🎓 Programs":

    st.header("🎓 Technology & Training Programs")

    with st.form("program_form"):

        program_name = st.text_input(
            "Program Name"
        )

        program_type = st.selectbox(
            "Program Type",
            [
                "Technology Program",
                "Training Program",
                "Certification Program",
                "Workshop"
            ]
        )

        duration = st.text_input(
            "Duration",
            placeholder="Example: 3 Months"
        )

        mode = st.selectbox(
            "Mode",
            ["Online", "Offline", "Hybrid"]
        )

        description = st.text_area(
            "Program Description"
        )

        status = st.selectbox(
            "Program Status",
            ["Active", "Upcoming", "Completed"]
        )

        submitted = st.form_submit_button(
            "Add Program"
        )

        if submitted:

            if not program_name.strip():
                st.error("Program name is required.")

            elif not duration.strip():
                st.error("Duration is required.")

            else:

                program = {
                    "id": generate_id(programs, "PRO"),
                    "name": program_name,
                    "type": program_type,
                    "duration": duration,
                    "mode": mode,
                    "description": description,
                    "status": status,
                    "created_date": str(date.today())
                }

                programs.append(program)

                save_data(
                    PROGRAMS_FILE,
                    programs
                )

                st.success(
                    "Program added successfully!"
                )

    st.divider()

    if programs:

        df = pd.DataFrame(programs)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No programs available."
        )


# ============================================================
# INTERNSHIPS
# ============================================================

elif page == "👨‍💻 Internships":

    st.header("👨‍💻 Internship Management")

    with st.form("internship_form"):

        title = st.text_input(
            "Internship Title"
        )

        domain = st.selectbox(
            "Domain",
            [
                "Python",
                "Web Development",
                "AI & ML",
                "Data Science",
                "Data Analytics",
                "Cloud Computing",
                "Cybersecurity"
            ]
        )

        duration = st.text_input(
            "Duration",
            placeholder="Example: 2 Months"
        )

        mode = st.selectbox(
            "Mode",
            ["Online", "Offline", "Hybrid"]
        )

        seats = st.number_input(
            "Available Seats",
            min_value=1,
            step=1
        )

        status = st.selectbox(
            "Status",
            ["Open", "Closed", "Upcoming"]
        )

        submitted = st.form_submit_button(
            "Add Internship"
        )

        if submitted:

            if not title.strip():
                st.error("Internship title is required.")

            else:

                internship = {
                    "id": generate_id(internships, "INT"),
                    "title": title,
                    "domain": domain,
                    "duration": duration,
                    "mode": mode,
                    "seats": seats,
                    "status": status,
                    "created_date": str(date.today())
                }

                internships.append(internship)

                save_data(
                    INTERNSHIPS_FILE,
                    internships
                )

                st.success(
                    "Internship added successfully!"
                )

    st.divider()

    if internships:

        df = pd.DataFrame(internships)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No internship records available."
        )


# ============================================================
# CUSTOMER INQUIRIES
# ============================================================

elif page == "📩 Customer Inquiries":

    st.header("📩 Customer Inquiry Management")

    with st.form("inquiry_form"):

        customer_name = st.text_input(
            "Customer Name"
        )

        email = st.text_input(
            "Email Address"
        )

        inquiry_type = st.selectbox(
            "Inquiry Type",
            [
                "Service Inquiry",
                "Training Inquiry",
                "Internship Inquiry",
                "Technical Support",
                "General Inquiry"
            ]
        )

        message = st.text_area(
            "Inquiry Description"
        )

        priority = st.selectbox(
            "Priority",
            ["Low", "Medium", "High"]
        )

        status = st.selectbox(
            "Status",
            ["New", "In Progress", "Resolved"]
        )

        submitted = st.form_submit_button(
            "Save Inquiry"
        )

        if submitted:

            if not customer_name.strip():
                st.error("Customer name is required.")

            elif not message.strip():
                st.error("Inquiry description is required.")

            else:

                inquiry = {
                    "id": generate_id(inquiries, "INQ"),
                    "customer": customer_name,
                    "email": email,
                    "type": inquiry_type,
                    "message": message,
                    "priority": priority,
                    "status": status,
                    "date": str(date.today())
                }

                inquiries.append(inquiry)

                save_data(
                    INQUIRIES_FILE,
                    inquiries
                )

                st.success(
                    "Customer inquiry saved successfully!"
                )

    st.divider()

    if inquiries:

        df = pd.DataFrame(inquiries)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No customer inquiries available."
        )


# ============================================================
# SERVICE REQUESTS
# ============================================================

elif page == "🛠️ Service Requests":

    st.header("🛠️ Service Request Management")

    with st.form("request_form"):

        customer = st.text_input(
            "Customer Name"
        )

        service = st.text_input(
            "Requested Service"
        )

        description = st.text_area(
            "Request Description"
        )

        priority = st.selectbox(
            "Priority",
            ["Low", "Medium", "High", "Critical"]
        )

        status = st.selectbox(
            "Request Status",
            ["Pending", "In Progress", "Completed", "Cancelled"]
        )

        submitted = st.form_submit_button(
            "Create Service Request"
        )

        if submitted:

            if not customer.strip():
                st.error("Customer name is required.")

            elif not service.strip():
                st.error("Service name is required.")

            else:

                request = {
                    "id": generate_id(requests, "REQ"),
                    "customer": customer,
                    "service": service,
                    "description": description,
                    "priority": priority,
                    "status": status,
                    "date": str(date.today())
                }

                requests.append(request)

                save_data(
                    REQUESTS_FILE,
                    requests
                )

                st.success(
                    "Service request created successfully!"
                )

    st.divider()

    if requests:

        df = pd.DataFrame(requests)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No service requests available."
        )

elif page == "📊 Reports":

    st.header("📊 Business Reports")

    st.subheader("Service Report")

    if services:

        service_df = pd.DataFrame(services)

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Services",
            len(service_df)
        )

        col2.metric(
            "Active Services",
            len(
                service_df[
                    service_df["status"] == "Active"
                ]
            )
        )

        col3.metric(
            "Average Service Price",
            f"₹{service_df['price'].mean():,.2f}"
        )

        st.dataframe(
            service_df,
            use_container_width=True
        )

    else:

        st.info("No service data available.")

    st.divider()

    st.subheader("Program Report")

    if programs:

        program_df = pd.DataFrame(programs)

        st.write(
            "Programs by type"
        )

        program_count = (
            program_df["type"]
            .value_counts()
            .reset_index()
        )

        program_count.columns = [
            "Program Type",
            "Count"
        ]

        st.dataframe(
            program_count,
            use_container_width=True
        )

    else:

        st.info("No program data available.")

    st.divider()

    st.subheader("Internship Report")

    if internships:

        internship_df = pd.DataFrame(
            internships
        )

        st.dataframe(
            internship_df,
            use_container_width=True
        )

    else:

        st.info("No internship data available.")

    st.divider()

    st.subheader("Customer Inquiry Report")

    if inquiries:

        inquiry_df = pd.DataFrame(
            inquiries
        )

        inquiry_count = (
            inquiry_df["status"]
            .value_counts()
            .reset_index()
        )

        inquiry_count.columns = [
            "Status",
            "Count"
        ]

        st.dataframe(
            inquiry_count,
            use_container_width=True
        )

    else:

        st.info("No inquiry data available.")

    st.divider()

    st.subheader("Service Request Report")

    if requests:

        request_df = pd.DataFrame(
            requests
        )

        request_count = (
            request_df["status"]
            .value_counts()
            .reset_index()
        )

        request_count.columns = [
            "Status",
            "Count"
        ]

        st.dataframe(
            request_count,
            use_container_width=True
        )

    else:

        st.info("No service request data available.")


st.divider()

st.caption(
    "Veda Technology Business & Service Management System | "
    "Python + Streamlit"
)