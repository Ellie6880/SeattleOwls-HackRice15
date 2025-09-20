import React, { useEffect, useState } from "react";
import axios from "axios";

export default function DrugList() {
  const [drugs, setDrugs] = useState([]);

  useEffect(() => {
    const fetchDrugs = async () => {
      const res = await axios.get("http://localhost:8000/prescriptions");
      setDrugs(res.data);
    };
    fetchDrugs();
  }, []);

  return (
    <div className="mt-6">
      <h2 className = "text-xl font-semibold mb-2">My Prescriptions</h2>
      <ul className = "space-y-2">
        {drugs.map(d => (
          <li key = {d.prescription_id} className="p-2 border rounded bg-gray-50">
            {d.task_label} – {d.dosage} at {d.time_of_day} from {d.start_date} to {d.end_date}
          </li>
        ))}
      </ul>
    </div>
  );
}
