import streamlit as st

st.set_page_config(
    page_title="Student Grade Calculator",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Grade Calculator")
st.write("Enter the student's marks for each subject to calculate the total, percentage, and grade.")

st.divider()

# Student details
student_name = st.text_input("Student Name", placeholder="Enter student name")

st.subheader("📚 Enter Subject Marks")

# Five subjects
subject1 = st.number_input("Subject 1", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
subject2 = st.number_input("Subject 2", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
subject3 = st.number_input("Subject 3", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
subject4 = st.number_input("Subject 4", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
subject5 = st.number_input("Subject 5", min_value=0.0, max_value=100.0, value=0.0, step=1.0)

if st.button("Calculate Grade", type="primary"):

    marks = [
        subject1,
        subject2,
        subject3,
        subject4,
        subject5
    ]

    # Calculate total and percentage
    total = sum(marks)
    maximum_marks = 500
    percentage = (total / maximum_marks) * 100

    # Assign grade
    if percentage >= 90:
        grade = "A+"
        description = "Excellent"
    elif percentage >= 80:
        grade = "A"
        description = "Very Good"
    elif percentage >= 70:
        grade = "B"
        description = "Good"
    elif percentage >= 60:
        grade = "C"
        description = "Average"
    elif percentage >= 50:
        grade = "D"
        description = "Pass"
    elif percentage >= 40:
        grade = "E"
        description = "Pass"
    else:
        grade = "F"
        description = "Fail"

    st.divider()

    st.subheader("📊 Student Result")

    if student_name:
        st.write(f"**Student Name:** {student_name}")

    st.write(f"**Total Marks:** {total:.0f} / {maximum_marks}")
    st.write(f"**Percentage:** {percentage:.2f}%")
    st.write(f"**Grade:** {grade}")
    st.write(f"**Performance:** {description}")

    # Result message
    if grade == "F":
        st.error("❌ Student has failed.")
    else:
        st.success(f"✅ Student has passed with Grade {grade}.")

    # Subject-wise marks
    st.subheader("📋 Subject-wise Marks")

    result_data = {
        "Subject": [
            "Subject 1",
            "Subject 2",
            "Subject 3",
            "Subject 4",
            "Subject 5"
        ],
        "Marks": marks
    }

    st.table(result_data)

st.divider()

st.subheader("📌 Grade Criteria")

st.write("""
- **A+** → 90% and above
- **A** → 80% – 89%
- **B** → 70% – 79%
- **C** → 60% – 69%
- **D** → 50% – 59%
- **E** → 40% – 49%
- **F** → Below 40%
""")