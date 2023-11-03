import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import "./App.css";

//components
import PageLayout from "./components/PageLayout";

//pages
import Dashboard from "./pages/Dashboard";
import Test from "./pages/Test";
import Login from "./pages/auth/Login";
import Signup from "./pages/auth/Signup";

export default function App() {
  return (
    <div>
      {/* <Header /> */}
      <Routes>
        <Route path="/test" element={<Test />} />
      </Routes>

      <Routes>
        <Route path="/auth/login" element={<Login />} />
        {/* <Route path="/auth/signup" element={<Signup />} /> */}
        <Route path="/" element={<Navigate to="/auth/login" replace />} />
      </Routes>

      <Routes>
        <Route path="/dashboard" element={<PageLayout><Dashboard /></PageLayout>} />
      </Routes>
    </div>
  );
}
