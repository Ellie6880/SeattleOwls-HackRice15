import { useState } from "react";
import api from "../api/api";

export default function Login({ setToken }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const res = await api.post("/login", { email, password });
      setToken(res.data.access_token);
      localStorage.setItem("token", res.data.access_token);
      alert("Login successful!");
    } catch {
      alert("Invalid credentials");
    }
  };

  return (
    <form onSubmit = {handleSubmit}>
      <input placeholder = "Email" value = {email} onChange = {e => setEmail(e.target.value)} />
      <input type = "password" placeholder = "Password" value = {password} onChange = {e => setPassword(e.target.value)} />
      <button type = "submit">Login</button>
    </form>
  );
}
