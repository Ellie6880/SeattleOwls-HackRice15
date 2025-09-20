import Prescriptions from "./prescriptions";
import Drugs from "./drugs";

export default function Dashboard({ userId }) {
  return (
    <div>
      <h1>Dashboard</h1>
      <Prescriptions userId = {userId} />
      <Drugs />
    </div>
  );
}
