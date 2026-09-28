import streamlit as st
st.set_page_config(
    page_title="Student Records",
    page_icon="🎓",
    layout="centered"
)

if "student_names" not in st.session_state:
    st.session_state.student_names = [
        "Rahul",
        "Priya",
        "Arjun",
        "Sneha",
        "Kiran"
    ]

if "student_marks" not in st.session_state:
    st.session_state.student_marks = [
        85,
        92,
        76,
        88,
        95
    ]

def add_student(name, marks):
    """Add a student name and marks to the lists."""
    if name.strip() and 0 <= marks <= 100:
        st.session_state.student_names.append(name.strip())
        st.session_state.student_marks.append(marks)
        return True
    return False


def search_student(name):
    """Search for a student by name."""
    for i, student in enumerate(st.session_state.student_names):
        if student.lower() == name.lower():
            return i
    return -1


def sort_students():
    """Sort students according to their marks."""
    records = list(
        zip(
            st.session_state.student_names,
            st.session_state.student_marks
        )
    )

    records.sort(key=lambda x: x[1], reverse=True)

    st.session_state.student_names = [
        record[0] for record in records
    ]

    st.session_state.student_marks = [
        record[1] for record in records
    ]


# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown("""
<style>
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .student-card {
        padding: 12px;
        margin: 7px 0;
        border-radius: 10px;
        border: 1px solid #dddddd;
        font-size: 17px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🎓 Student Records</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Practice Python lists with student names and marks'
    '</div>',
    unsafe_allow_html=True
)

st.divider()
st.sidebar.title("📋 Operations")

operation = st.sidebar.radio(
    "Select an operation:",
    [
        "📊 View Records",
        "➕ Add Student",
        "🔍 Search Student",
        "↕️ Sort by Marks",
        "🏆 Highest & Lowest Score"
    ]
)
if operation == "📊 View Records":

    st.header("📊 Student Records")

    if len(st.session_state.student_names) == 0:

        st.info("No student records available.")

    else:

        st.write(
            f"**Total Students: "
            f"{len(st.session_state.student_names)}**"
        )

        for i in range(len(st.session_state.student_names)):

            name = st.session_state.student_names[i]
            marks = st.session_state.student_marks[i]

            st.markdown(
                f"""
                <div class="student-card">
                    <b>{i + 1}. {name}</b>
                    &nbsp;&nbsp; | &nbsp;&nbsp;
                    Marks: <b>{marks}/100</b>
                </div>
                """,
                unsafe_allow_html=True
            )
elif operation == "➕ Add Student":

    st.header("➕ Add Student Record")

    name = st.text_input(
        "Student Name",
        placeholder="Enter student name"
    )

    marks = st.number_input(
        "Marks",
        min_value=0,
        max_value=100,
        value=50,
        step=1
    )

    if st.button(
        "Add Student",
        use_container_width=True
    ):

        if add_student(name, marks):

            st.success(
                f"✅ {name} added successfully with {marks} marks."
            )

        else:

            st.error(
                "❌ Please enter a valid student name and marks."
            )
elif operation == "🔍 Search Student":

    st.header("🔍 Search Student")

    search_name = st.text_input(
        "Enter student name:",
        placeholder="Example: Rahul"
    )

    if st.button(
        "Search",
        use_container_width=True
    ):

        if not search_name.strip():

            st.warning("Please enter a student name.")

        else:

            index = search_student(search_name)

            if index != -1:

                name = st.session_state.student_names[index]
                marks = st.session_state.student_marks[index]

                st.success("✅ Student found!")

                st.write(f"**Name:** {name}")
                st.write(f"**Marks:** {marks}/100")

            else:

                st.error(
                    f"❌ No record found for '{search_name}'."
                )
elif operation == "↕️ Sort by Marks":

    st.header("↕️ Sort Students by Marks")

    st.write(
        "Students will be arranged from highest marks "
        "to lowest marks."
    )

    if st.button(
        "Sort Students",
        use_container_width=True
    ):

        sort_students()

        st.success("✅ Students sorted successfully!")

    st.divider()

    for i in range(len(st.session_state.student_names)):

        name = st.session_state.student_names[i]
        marks = st.session_state.student_marks[i]

        st.write(
            f"**{i + 1}. {name} — {marks}/100**"
        )
elif operation == "🏆 Highest & Lowest Score":

    st.header("🏆 Score Analysis")

    if len(st.session_state.student_marks) == 0:

        st.info("No student records available.")

    else:

        highest_marks = max(
            st.session_state.student_marks
        )

        lowest_marks = min(
            st.session_state.student_marks
        )

        highest_index = (
            st.session_state.student_marks.index(
                highest_marks
            )
        )

        lowest_index = (
            st.session_state.student_marks.index(
                lowest_marks
            )
        )

        highest_name = (
            st.session_state.student_names[highest_index]
        )

        lowest_name = (
            st.session_state.student_names[lowest_index]
        )

        col1, col2 = st.columns(2)

        with col1:
            st.success(
                f"""
                🏆 Highest Score

                **{highest_name}**

                **{highest_marks}/100**
                """
            )

        with col2:
            st.warning(
                f"""
                📉 Lowest Score

                **{lowest_name}**

                **{lowest_marks}/100**
                """
            )
st.divider()

st.markdown(
    """
    <div style="text-align:center;">
        🐍 VEDA Internship | Python Programming Track | Day 9<br>
        Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)