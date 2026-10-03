"""Run this app with: streamlit run grade_app.py"""

import streamlit as st


def get_grade(mark):
    """Return a letter grade using the agreed grading scale."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    return "F"


st.set_page_config(page_title="Grade manager")
st.title("Grade manager")
st.caption("A: 90–100 · B: 80–89 · C: 70–79 · D: 60–69 · F: below 60")

# A plain students = [] here would reset on every script rerun.
# Initialize once per session so earlier students survive form submissions.
if "students" not in st.session_state:
    st.session_state.students = []

with st.form("add_student"):
    st.subheader("Add a student")
    name = st.text_input("Name")
    mark = st.number_input("Mark", min_value=0, max_value=100, step=1)
    submitted = st.form_submit_button("Add student")

if submitted:
    name = name.strip()
    if not name:
        st.error("Enter a student name.")
    elif not 0 <= mark <= 100:
        st.error("Mark must be between 0 and 100.")
    else:
        st.session_state.students.append(
            {"Name": name, "Mark": mark, "Grade": get_grade(mark)}
        )
        st.success("Student added.")

st.subheader("Student results")
students = st.session_state.students
if students:
    st.table(students, alt="Student names, marks, and letter grades")
else:
    st.info("Add your first student to see the results.")

st.subheader("Class figures")
marks = [student["Mark"] for student in students]
average, highest, lowest = st.columns(3)
average.metric("Class average", f"{sum(marks) / len(marks):.2f}" if marks else "—")
highest.metric("Highest mark", max(marks) if marks else "—")
lowest.metric("Lowest mark", min(marks) if marks else "—")
