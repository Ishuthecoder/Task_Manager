📋 PerformX Task Manager

A task management system built with Streamlit and Firebase Cloud Messaging (FCM) to manage tasks, send notifications, and track deadlines efficiently.

🚀 Features

✅ Add, Edit, and Delete Tasks

✅ Assign Due Dates & Priorities

✅ Generate & Store Firebase Cloud Messaging (FCM) Tokens

✅ Send Notifications for Upcoming & Overdue Tasks

✅ Save Task Data in Session State
✅ User-Friendly Interface with Streamlit

🛠 Installation Guide
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/your-username/performx-task-manager.git
cd performx-task-manager
2️⃣ Install Dependencies
Ensure Python is installed, then run:

sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Streamlit App
sh
Copy
Edit
streamlit run app/main.py
🔥 Firebase Setup
1️⃣ Set Up Firebase Cloud Messaging (FCM)
Go to Firebase Console
Create a new project and enable Cloud Messaging
Download your Admin SDK JSON file and place it in the firebase/ directory
2️⃣ Configure Firebase in Your App
Open firebase/firebase-config.js
Replace with your Firebase project details:
javascript
Copy
Edit
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT.appspot.com",
    messagingSenderId: "YOUR_SENDER_ID",
    appId: "YOUR_APP_ID"
};
📌 Project Structure
graphql
Copy
Edit
📂 performx-task-manager/
│── 📂 firebase/  
│   ├── firebase-config.js  # Firebase Web SDK Config  
│── 📂 app/  
│   ├── main.py             # Streamlit App  
│   ├── fcm.py              # FCM Notification Logic  
│── .gitignore              # Ignore unnecessary files  
│── requirements.txt        # Python Dependencies  
│── README.md               # Project Documentation  
│── Procfile                # (Optional) For Deployment  
🔔 Sending Notifications
The system will send automatic push notifications using FCM for:
✅ Tasks due tomorrow
✅ Overdue tasks
📝 License
This project is open-source under the MIT License. Feel free to modify and use it!

👤 Author
👩‍💻 Your Name
🔗 GitHub: your-username
🔗 LinkedIn: your-linkedin

