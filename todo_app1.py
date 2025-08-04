import streamlit as st
import os

# File where tasks will be stored
TASK_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Streamlit app setup
st.set_page_config(page_title="To-Do List App", page_icon="📝")
st.title("📝 To-Do List App (Streamlit)")

# Load current tasks
tasks = load_tasks()

# Section: Add New Task
st.subheader("➕ Add New Task")
new_task = st.text_input("Enter a task:")
if st.button("Add Task"):
    if new_task.strip() != "":
        tasks.append(new_task.strip())
        save_tasks(tasks)
        st.success(f"✅ Task added: {new_task}")
        st.rerun()  # Refresh the app
    else:
        st.warning("⚠️ Please enter a valid task.")

# Section: View Tasks
st.subheader("📋 Your Tasks")
if tasks:
    for i, task in enumerate(tasks, start=1):
        st.markdown(f"{i}. {task}")
else:
    st.info("No tasks yet. Add one above!")

# Section: Remove Task
st.subheader("🗑️ Remove a Task")
if tasks:
    task_to_remove = st.selectbox("Select a task to remove", [""] + tasks)
    if st.button("Remove Task"):
        if task_to_remove:
            tasks.remove(task_to_remove)
            save_tasks(tasks)
            st.success(f"🗑️ Removed task: {task_to_remove}")
            st.rerun()  # Refresh the app
        else:
            st.warning("⚠️ Please select a task to remove.")
else:
    st.info("No tasks available to delete.")
