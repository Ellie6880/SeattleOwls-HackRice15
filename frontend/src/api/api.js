import axios from "axios";

// Create a reusable Axios instance pointing to your FastAPI backend
const api = axios.create({
  baseURL: "https://api.medicine.tracker.com", // FastAPI backend URL
  headers: {
    "Content-Type": "application/json",
  },
});

// Optional: Add interceptors if you want to handle auth tokens
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token"); // assuming you store JWT after login
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
