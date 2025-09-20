import React, { useState } from "react";
import axios from "axios";

export default function DrugForm() {
  const [formData, setFormData] = useState({
    drug_id: "",
    task_label: "",
    dosage: "",
    time_of_day: "",
    start_date: "",
    end_date: "",
    user_id: 1, // Replace with logged-in user ID
  });

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await axios.post("http://localhost:8000/prescriptions", formData);
      alert("Prescription added!");
      setFormData({
        drug_id: "",
        task_label: "",
        dosage: "",
        time_of_day: "",
        start_date: "",
        end_date: "",
        user_id: 1,
      });
    } catch (err) {
      console.error(err);
      alert("Error adding prescription");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <h2 className = "text-xl font-semibold">Add Drug</h2>
      <input
        name = "drug_id"
        value = {formData.drug_id}
        onChange = {handleChange}
        placeholder = "Drug ID"
        className = "w-full p-2 border rounded"
        required
      />
      <input
        name = "task_label"
        value = {formData.task_label}
        onChange = {handleChange}
        placeholder = "Task Label"
        className = "w-full p-2 border rounded"
      />
      <input
        name = "dosage"
        value = {formData.dosage}
        onChange = {handleChange}
        placeholder = "Dosage"
        className = "w-full p-2 border rounded"
      />
      <input
        type = "time"
        name = "time_of_day"
        value = {formData.time_of_day}
        onChange = {handleChange}
        className = "w-full p-2 border rounded"
        required
      />
      <input
        type = "date"
        name = "start_date"
        value = {formData.start_date}
        onChange = {handleChange}
        className = "w-full p-2 border rounded"
      />
      <input
        type = "date"
        name = "end_date"
        value = {formData.end_date}
        onChange = {handleChange}
        className = "w-full p-2 border rounded"
      />
      <button
        type = "submit"
        className = "bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
      >
        Add Prescription
      </button>
    </form>
  );
}
