// Import the functions you need from the SDKs you need
// import firebase from "firebase";
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

import firebase from "firebase/compat/app";
import "firebase/compat/auth";
import "firebase/compat/firestore";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCkelnno1wTUgG9UJudO6I2tWUPf8X3NMA",
  authDomain: "clone-36ab3.firebaseapp.com",
  projectId: "clone-36ab3",
  storageBucket: "clone-36ab3.appspot.com",
  messagingSenderId: "643253747084",
  appId: "1:643253747084:web:4b07c381697d8d10332aa9",
  measurementId: "G-0P65WL0R4K",
};

// Initialize Firebase
const firebaseApp = firebase.initializeApp(firebaseConfig);
const db = firebaseApp.firestore();
const auth = firebase.auth();

// const analytics = firebase.getAnalytics(app);

export { db, auth };
