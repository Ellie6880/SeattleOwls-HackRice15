import React from "react";
import SignUpForm from "./components/signupform";
import DrugForm from "./components/drugform";

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-2xl mx-auto bg-white p-6 rounded shadow">
        <h1 className="text-2xl font-bold mb-4">Medication Scheduler</h1>
        <SignUpForm />
        <hr className="my-6" />
        <DrugForm />
      </div>
    </div>
  );
}

export default App;
