import firebase_admin
from firebase_admin import credentials, messaging
import pandas as pd
from datetime import datetime, timedelta

# Load Firebase Admin SDK
cred = credentials.Certificate("firebase/firebase-adminsdk.json")  # Add your Firebase Admin JSON file
firebase_admin.initialize_app(cred)

def send_fcm_notification():
    if "task_data" not in st.session_state:
        return

    df = st.session_state.task_data
    today = datetime.today().date()

    for _, row in df.iterrows():
        due_date = row["Due Date"].date()
        fcm_token = row["FCM Token"]

        if fcm_token and (due_date == today + timedelta(days=1) or due_date < today):
            message = messaging.Message(
                notification=messaging.Notification(
                    title="📌 Task Reminder!",
                    body=f"Task '{row['Task Name']}' is Due on {due_date}."
                ),
                token=fcm_token
            )
            response = messaging.send(message)
            print(f"🔔 Notification Sent: {response}")
