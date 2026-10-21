import streamlit as st
import json
from pathlib import Path

st.set_page_config(
    page_title="Student Result & Grade Management",
    page_icon="🎓",
    layout="wide"
)

DATA_FILE = Path("students.json")

def load_students():
    """Load student records from JSON file."""

    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_students(students):
    """Save student records to JSON file."""

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def calculate_grade(percentage):
    """Calculate grade based on percentage."""

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def calculate_result(marks):
    """Calculate total, percentage and grade."""

    total = sum(marks.values())
    maximum = len(marks) * 100

    percentage = (total / maximum) * 100

    grade = calculate_grade(percentage)

    result = "Pass" if percentage >= 40 else "Fail"

    return total, percentage, grade, result

students = load_students()

st.title("🎓 Student Result & Grade Management System")

st.write(
    "Manage student details, subject marks, grades and "
    "academic performance using Python and Streamlit."
)

st.divider()

st.sidebar.title("📚 Navigation")

menu = st.sidebar.radio(
    "Select Operation",
    [
        "Dashboard",
        "Add Student",
        "Search Student",
        "View All Students",
        "Performance Summary"
    ]
)

if menu == "Dashboard":

    st.header("📊 Dashboard")

    total_students = len(students)

    if total_students > 0:

        percentages = [
            student["percentage"]
            for student in students
        ]

        average_percentage = sum(percentages) / len(percentages)

        highest_percentage = max(percentages)

        passed_students = sum(
            1 for student in students
            if student["result"] == "Pass"
        )

        failed_students = total_students - passed_students

    else:

        average_percentage = 0
        highest_percentage = 0
        passed_students = 0
        failed_students = 0

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Students",
        total_students
    )

    col2.metric(
        "Average Percentage",
        f"{average_percentage:.2f}%"
    )

    col3.metric(
        "Highest Percentage",
        f"{highest_percentage:.2f}%"
    )

    col4.metric(
        "Passed Students",
        passed_students
    )

    st.divider()

    st.subheader("📌 System Features")

    st.markdown("""
    - Add student records
    - Enter subject-wise marks
    - Automatically calculate total marks
    - Automatically calculate percentage
    - Automatically assign grades
    - Search students
    - View all student records
    - Generate performance summaries
    - Store records using JSON
    """)

elif menu == "Add Student":

    st.header("➕ Add Student")

    with st.form("student_form"):

        student_id = st.text_input(
            "Student ID",
            placeholder="Example: STU001"
        )

        student_name = st.text_input(
            "Student Name",
            placeholder="Enter student name"
        )

        st.subheader("📚 Subject Marks")

        col1, col2 = st.columns(2)

        with col1:

            python_marks = st.number_input(
                "Python",
                min_value=0,
                max_value=100,
                value=0
            )

            mathematics_marks = st.number_input(
                "Mathematics",
                min_value=0,
                max_value=100,
                value=0
            )

            database_marks = st.number_input(
                "Database",
                min_value=0,
                max_value=100,
                value=0
            )

        with col2:

            computer_networks_marks = st.number_input(
                "Computer Networks",
                min_value=0,
                max_value=100,
                value=0
            )

            web_technology_marks = st.number_input(
                "Web Technology",
                min_value=0,
                max_value=100,
                value=0
            )

            submit = st.form_submit_button(
                "💾 Save Student",
                use_container_width=True
            )

    if submit:

        student_id = student_id.strip()
        student_name = student_name.strip()

        if not student_id or not student_name:

            st.error(
                "Please enter both Student ID and Student Name."
            )

        elif any(
            student["student_id"] == student_id
            for student in students
        ):

            st.error(
                "Student ID already exists."
            )

        else:

            marks = {
                "Python": python_marks,
                "Mathematics": mathematics_marks,
                "Database": database_marks,
                "Computer Networks": computer_networks_marks,
                "Web Technology": web_technology_marks
            }

            total, percentage, grade, result = calculate_result(
                marks
            )

            student = {
                "student_id": student_id,
                "name": student_name,
                "marks": marks,
                "total": total,
                "percentage": percentage,
                "grade": grade,
                "result": result
            }

            students.append(student)

            save_students(students)

            st.success(
                f"Student {student_name} added successfully!"
            )

            st.info(
                f"Total: {total}/500 | "
                f"Percentage: {percentage:.2f}% | "
                f"Grade: {grade} | "
                f"Result: {result}"
            )


elif menu == "Search Student":

    st.header("🔍 Search Student")

    search_id = st.text_input(
        "Enter Student ID",
        placeholder="Example: STU001"
    )

    if st.button(
        "🔎 Search",
        use_container_width=True
    ):

        search_id = search_id.strip()

        student = next(
            (
                student
                for student in students
                if student["student_id"].lower()
                == search_id.lower()
            ),
            None
        )

        if student:

            st.success(
                f"Student found: {student['name']}"
            )

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Student ID",
                student["student_id"]
            )

            col2.metric(
                "Total",
                f"{student['total']}/500"
            )

            col3.metric(
                "Percentage",
                f"{student['percentage']:.2f}%"
            )

            col4.metric(
                "Grade",
                student["grade"]
            )

            st.subheader("📚 Subject-wise Marks")

            for subject, marks in student["marks"].items():

                st.write(
                    f"**{subject}:** {marks}/100"
                )

            st.info(
                f"Final Result: {student['result']}"
            )

        else:

            st.error(
                "Student not found."
            )

elif menu == "View All Students":

    st.header("👨‍🎓 All Student Records")

    if not students:

        st.warning(
            "No student records available."
        )

    else:

        table_data = []

        for student in students:

            table_data.append({
                "Student ID": student["student_id"],
                "Name": student["name"],
                "Total": student["total"],
                "Percentage": f"{student['percentage']:.2f}%",
                "Grade": student["grade"],
                "Result": student["result"]
            })

        st.dataframe(
            table_data,
            use_container_width=True,
            hide_index=True
        )

elif menu == "Performance Summary":

    st.header("📈 Performance Summary")

    if not students:

        st.warning(
            "No student data available."
        )

    else:

        percentages = [
            student["percentage"]
            for student in students
        ]

        average = sum(percentages) / len(percentages)

        highest = max(percentages)

        lowest = min(percentages)

        passed = sum(
            1
            for student in students
            if student["result"] == "Pass"
        )

        failed = len(students) - passed

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric(
            "Students",
            len(students)
        )

        col2.metric(
            "Average",
            f"{average:.2f}%"
        )

        col3.metric(
            "Highest",
            f"{highest:.2f}%"
        )

        col4.metric(
            "Passed",
            passed
        )

        col5.metric(
            "Failed",
            failed
        )

        st.divider()

        st.subheader("🏆 Top Performing Students")

        sorted_students = sorted(
            students,
            key=lambda student: student["percentage"],
            reverse=True
        )

        top_students = sorted_students[:5]

        ranking = []

        for index, student in enumerate(
            top_students,
            start=1
        ):

            ranking.append({
                "Rank": index,
                "Student ID": student["student_id"],
                "Name": student["name"],
                "Percentage":
                    f"{student['percentage']:.2f}%",
                "Grade": student["grade"]
            })

        st.dataframe(
            ranking,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("📊 Grade Distribution")

        grade_counts = {}

        for student in students:

            grade = student["grade"]

            grade_counts[grade] = (
                grade_counts.get(grade, 0) + 1
            )

        st.bar_chart(grade_counts)