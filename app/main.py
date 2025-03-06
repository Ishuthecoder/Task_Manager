import streamlit as st
import pandas as pd
from datetime import datetime
from app.fcm import send_fcm_notification

# Load Task Data
tasks = [
    {"Task Name": "Prepare AI Model Report", "Assignee": "ID", "FCM Token": "", "Starting Date": "2025-03-01", "Due Date": "2025-03-05", "Priority": "Urgent", "Status": "TO DO"},
    {"Task Name": "Review BioGPT Fine-Tuning Results", "Assignee": "ID", "FCM Token": "", "Starting Date": "2025-03-05", "Due Date": "2025-03-10", "Priority": "Normal", "Status": "TO DO"},
]

df = pd.DataFrame(tasks)
df["Starting Date"] = pd.to_datetime(df["Starting Date"])
df["Due Date"] = pd.to_datetime(df["Due Date"])

if "task_data" not in st.session_state:
    st.session_state.task_data = df

st.set_page_config(layout="wide")
st.title("📋 Task Manager - PerformX")

# Editable Task Table
st.write("### 📝 Task List (Editable)")
edited_df = st.data_editor(st.session_state.task_data, num_rows="dynamic", height=300)

if not edited_df.equals(st.session_state.task_data):
    st.session_state.task_data = edited_df
    st.success("✅ Changes Saved Successfully!")

# Add New Task Section
st.write("### ➕ Add a New Task")
with st.form("new_task_form"):
    task_name = st.text_input("Task Name")
    assignee = st.text_input("Assignee")
    fcm_token = st.text_input("FCM Token")
    starting_date = st.date_input("Starting Date", datetime.today())
    due_date = st.date_input("Due Date", datetime.today())
    priority = st.selectbox("Priority", ["Urgent", "Normal", "Low"])
    status = st.selectbox("Status", ["TO DO", "In Progress", "Completed"])
    submitted = st.form_submit_button("Add Task")

    if submitted and task_name:
        new_task = {
            "Task Name": task_name,
            "Assignee": assignee,
            "FCM Token": fcm_token,
            "Starting Date": starting_date,
            "Due Date": due_date,
            "Priority": priority,
            "Status": status
        }
        st.session_state.task_data = pd.concat([st.session_state.task_data, pd.DataFrame([new_task])], ignore_index=True)
        st.success("✅ Task Added Successfully!")
        st.experimental_rerun()

# Send Notification for Due Tasks
send_fcm_notification()
