import { useEffect, useState } from "react";
import api from "../api/api";

export default function Prescriptions({ userId }) {
  const [prescriptions, setPrescriptions] = useState([]);

  useEffect(() => {
    api.get(`/prescriptions/${userId}`)
       .then(res => setPrescriptions(res.data))
       .catch(console.error);
  }, [userId]);

  return (
    <div>
      <h2>Your Prescriptions</h2>
      <ul>
        {prescriptions.map(p => (
          <li key = {p.id}>{p.task_label} - {p.dosage} ({p.time_of_day})</li>
        ))}
      </ul>
    </div>
  );
}
