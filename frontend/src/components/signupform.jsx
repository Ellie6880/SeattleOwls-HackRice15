import React, { useState } from "react";
import axios from "axios";

export default function SignUpForm() {
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
    phone_number: "",
    address: "",
  });

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await axios.post("http://localhost:8000/users", formData);
      alert("User registered successfully!");
      setFormData({
        first_name: "",
        last_name: "",
        email: "",
        password: "",
        phone_number: "",
        address: "",
      });
    } catch (err) {
      console.error(err);
      alert("Error registering user");
    }
  };

  return (
    <form onSubmit={handleSubmit} className = "space-y-4">
      <h2 className="text-xl font-semibold">Sign Up</h2>
      {["first_name", "last_name", "email", "password", "phone_number", "address"].map((field) => (
        <input
          key = {field}
          type = {field === "password" ? "password" : "text"}
          name = {field}
          value = {formData[field]}
          onChange = {handleChange}
          placeholder = {field.replace("_", " ")}
          className = "w-full p-2 border rounded"
          required
        />
      ))}
      <button type = "submit" className = "bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
        Register
      </button>
    </form>
  );
}
