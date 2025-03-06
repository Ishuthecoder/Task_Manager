import { initializeApp } from "firebase/app";
import { getMessaging, getToken } from "firebase/messaging";

const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT.appspot.com",
    messagingSenderId: "YOUR_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const messaging = getMessaging(app);

// Function to Get FCM Token
export function requestFCMToken() {
    return getToken(messaging)
        .then((token) => {
            if (token) {
                console.log("🔥 FCM Token:", token);
                return token;
            } else {
                console.log("No registration token available.");
            }
        })
        .catch((err) => {
            console.log("An error occurred while retrieving token.", err);
        });
}
