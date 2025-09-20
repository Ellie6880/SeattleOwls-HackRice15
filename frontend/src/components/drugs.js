import { useEffect, useState } from "react";
import api from "../api/api";

export default function Drugs() {
  const [drugs, setDrugs] = useState([]);

  useEffect(() => {
    api.get("/drugs")
       .then(res => setDrugs(res.data))
       .catch(console.error);
  }, []);

  return (
    <div>
      <h2>Drugs Info</h2>
      <ul>
        {drugs.map(d => (
          <li key = {d.id}>
            <strong>{d.name}</strong>: {d.description || "No description"} | Side Effects: {d.side_effects || "None"}
          </li>
        ))}
      </ul>
    </div>
  );
}
