import { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Register from "./components/register";
import Login from "./components/login";
import Dashboard from "./components/dashboard";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [userId, setUserId] = useState(1); // replace with dynamic after login

  return (
    <Router>
      <Routes>
        <Route path = "/register" element = {<Register />} />
        <Route path = "/login" element = {<Login setToken = {setToken} />} />
        <Route path = "/dashboard" element = {<Dashboard userId = {userId} />} />
      </Routes>
    </Router>
  );
}

export default App;
