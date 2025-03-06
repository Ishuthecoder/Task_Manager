import streamlit as st
import pandas as pd
from datetime import datetime

# Sample Task Data
tasks = [
    {"Task Name": "Prepare AI Model Report", "Assignee": "ID", "FCM Token": "", "Starting Date": "2025-03-01", "Due Date": "2025-03-05", "Priority": "Urgent", "Status": "TO DO"},
    {"Task Name": "Review BioGPT Fine-Tuning Results", "Assignee": "ID", "FCM Token": "", "Starting Date": "2025-03-05", "Due Date": "2025-03-10", "Priority": "Normal", "Status": "TO DO"},
    {"Task Name": "Test Human Disease Detection Model", "Assignee": "ID", "FCM Token": "", "Starting Date": "2025-03-10", "Due Date": "2025-03-15", "Priority": "Low", "Status": "TO DO"},
    {"Task Name": "Final Project Presentation Preparation", "Assignee": "ID", "FCM Token": "", "Starting Date": "2025-03-15", "Due Date": "2025-03-20", "Priority": "Low", "Status": "TO DO"},
    {"Task Name": "Integrate Model with Web Interface", "Assignee": "ID", "FCM Token": "", "Starting Date": "2025-03-20", "Due Date": "2025-03-28", "Priority": "Normal", "Status": "TO DO"},
]

# Convert to DataFrame
df = pd.DataFrame(tasks)
df["Starting Date"] = pd.to_datetime(df["Starting Date"])
df["Due Date"] = pd.to_datetime(df["Due Date"])

# Store task data in session state
if "task_data" not in st.session_state:
    st.session_state.task_data = df

if "fcm_token" not in st.session_state:
    st.session_state.fcm_token = ""

def main():
    st.set_page_config(layout="wide")
    st.title("📋 Task Manager - PerformX")

    # 🔥 Inject Firebase Script for FCM Token Generation
    firebase_script = """
    <script src="https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.6.1/firebase-messaging.js"></script>

    <script>
        const firebaseConfig = {
            apiKey: "AIzaSyBeZW5TaCNd5vQ0wahxSTjSmBcYhSp6PiY",
            authDomain: "performx-task-manager.firebaseapp.com",
            projectId: "performx-task-manager",
            storageBucket: "performx-task-manager.firebasestorage.app",
            messagingSenderId: "585404219769",
            appId: "1:585404219769:web:150032cbdb4160ddf7efa8",
            measurementId: "G-JQ8H07SLQG"
        };

        firebase.initializeApp(firebaseConfig);
        const messaging = firebase.messaging();

        async function requestFCMToken() {
            const permission = await Notification.requestPermission();
            if (permission === "granted") {
                try {
                    const token = await messaging.getToken();
                    window.parent.postMessage(token, "*");
                } catch (error) {
                    console.error("FCM Token Error:", error);
                }
            } else {
                alert("You must allow notifications to get the FCM token.");
            }
        }

        window.addEventListener("message", (event) => {
            if (event.data) {
                document.getElementById("fcm_token_input").value = event.data;
            }
        });
    </script>

    <button onclick="requestFCMToken()">Generate FCM Token</button>
    <input type="text" id="fcm_token_input" style="width:100%;" placeholder="FCM Token will appear here">
    """
    
    st.components.v1.html(firebase_script, height=150)

    # 🔥 Store Generated FCM Token in Streamlit
    fcm_token = st.text_input("FCM Token", value=st.session_state.fcm_token)
    st.session_state.fcm_token = fcm_token

    if st.button("Save FCM Token"):
        st.success(f"✅ Token Saved: {fcm_token}")

    # 🔥 Editable Task Table
    st.write("### 📝 Task List (Editable)")
    edited_df = st.data_editor(st.session_state.task_data, num_rows="dynamic", height=300)

    if not edited_df.equals(st.session_state.task_data):
        st.session_state.task_data = edited_df
        st.success("✅ Changes Saved Successfully!")

    # 🔥 Add New Task Section
    st.write("### ➕ Add a New Task")
    with st.form("new_task_form"):
        task_name = st.text_input("Task Name", placeholder="Enter task name")
        assignee = st.text_input("Assignee", placeholder="Enter assignee name")
        fcm_token = st.text_input("FCM Token", placeholder="Enter FCM Token for Notifications")
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

if __name__ == "__main__":
    main()
