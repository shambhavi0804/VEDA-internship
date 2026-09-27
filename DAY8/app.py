import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Simple To-Do List",
    page_icon="✅",
    layout="centered"
)

# --------------------------------------------------
# Initialize Task List
# --------------------------------------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []


# --------------------------------------------------
# CRUD Functions
# --------------------------------------------------

def add_task(task):
    """Add a new task to the list."""
    if task.strip():
        st.session_state.tasks.append(task.strip())
        return True
    return False


def update_task(task_number, new_task):
    """Update an existing task."""
    index = task_number - 1

    if 0 <= index < len(st.session_state.tasks):
        if new_task.strip():
            st.session_state.tasks[index] = new_task.strip()
            return True

    return False


def remove_task(task_number):
    """Remove a task from the list."""
    index = task_number - 1

    if 0 <= index < len(st.session_state.tasks):
        st.session_state.tasks.pop(index)
        return True

    return False


# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
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
        margin-bottom: 30px;
    }

    .task-card {
        padding: 12px 18px;
        margin: 8px 0;
        border-radius: 10px;
        border: 1px solid #ddd;
        font-size: 17px;
    }

    .footer {
        text-align: center;
        margin-top: 35px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown(
    '<div class="title">✅ Simple To-Do List</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Organize your tasks using a simple task manager'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# --------------------------------------------------
# Sidebar Menu
# --------------------------------------------------
st.sidebar.title("📋 Menu")

operation = st.sidebar.radio(
    "Choose an operation:",
    [
        "➕ Add Task",
        "👀 View Tasks",
        "✏️ Update Task",
        "🗑️ Remove Task"
    ]
)


# --------------------------------------------------
# ADD TASK
# --------------------------------------------------
if operation == "➕ Add Task":

    st.header("➕ Add a New Task")

    task = st.text_input(
        "Enter your task:",
        placeholder="Example: Complete Python assignment"
    )

    if st.button("Add Task", use_container_width=True):

        if add_task(task):
            st.success("✅ Task added successfully!")
        else:
            st.error("❌ Please enter a valid task.")


# --------------------------------------------------
# VIEW TASKS
# --------------------------------------------------
elif operation == "👀 View Tasks":

    st.header("👀 Your Tasks")

    if len(st.session_state.tasks) == 0:

        st.info("📭 No tasks available. Add a task to get started.")

    else:

        st.write(
            f"**Total Tasks: {len(st.session_state.tasks)}**"
        )

        for index, task in enumerate(
            st.session_state.tasks,
            start=1
        ):

            st.markdown(
                f"""
                <div class="task-card">
                    <b>{index}.</b> {task}
                </div>
                """,
                unsafe_allow_html=True
            )


# --------------------------------------------------
# UPDATE TASK
# --------------------------------------------------
elif operation == "✏️ Update Task":

    st.header("✏️ Update a Task")

    if len(st.session_state.tasks) == 0:

        st.info("📭 No tasks available to update.")

    else:

        # Display existing tasks
        for index, task in enumerate(
            st.session_state.tasks,
            start=1
        ):
            st.write(f"**{index}.** {task}")

        st.divider()

        task_number = st.number_input(
            "Enter task number to update:",
            min_value=1,
            max_value=len(st.session_state.tasks),
            step=1
        )

        new_task = st.text_input(
            "Enter the new task:"
        )

        if st.button(
            "Update Task",
            use_container_width=True
        ):

            if update_task(task_number, new_task):
                st.success("Task updated successfully!")
                st.rerun()
            else:
                st.error("Please enter a valid task.")


# --------------------------------------------------
# REMOVE TASK
# --------------------------------------------------
elif operation == "🗑️ Remove Task":

    st.header("🗑️ Remove a Task")

    if len(st.session_state.tasks) == 0:

        st.info("📭 No tasks available to remove.")

    else:

        # Display existing tasks
        for index, task in enumerate(
            st.session_state.tasks,
            start=1
        ):
            st.write(f"**{index}.** {task}")

        st.divider()

        task_number = st.number_input(
            "Enter task number to remove:",
            min_value=1,
            max_value=len(st.session_state.tasks),
            step=1
        )

        if st.button(
            "Remove Task",
            use_container_width=True
        ):

            if remove_task(task_number):
                st.success("🗑️ Task removed successfully!")
                st.rerun()
            else:
                st.error("❌ Invalid task number.")


# --------------------------------------------------
# Footer
# --------------------------------------------------
st.divider()

st.markdown(
    """
    <div class="footer">
        🐍 VEDA Internship | Python Programming Track | Day 8<br>
        Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)