import { useState } from "react";
import api from "../api/api";

export default function Register() {
  const [form, setForm] = useState({
    username: "",
    email: "",
    password: "",
    first_name: "",
    last_name: "",
    home_address: "",
    phone_number: ""
  });

  const handleChange = e => setForm({...form, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await api.post("/register", form);
      alert("Registration successful!");
    } catch (err) {
      alert(err.response?.data?.detail || "Error registering user");
    }
  };

  return (
    <form onSubmit = {handleSubmit}>
      {Object.keys(form).map(key => (
        <input
          key = {key}
          name = {key}
          placeholder = {key}
          value = {form[key]}
          onChange = {handleChange}
          required
        />
      ))}
      <button type="submit">Register</button>
    </form>
  );
}
