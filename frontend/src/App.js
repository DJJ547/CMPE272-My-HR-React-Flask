import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import "./App.css";

//components
import PageLayout from "./components/PageLayout";

//pages
import Dashboard from "./pages/Dashboard";
import Clock from "./pages/Clock";
import Scheduling from "./pages/Scheduling";
import Test from "./pages/Test";
import Login from "./pages/auth/Login";
import Signup from "./pages/auth/Signup";

export default function App() {
  return (
    <div>
      {/* <Header /> */}
      <Routes>
        <Route path="/test" element={<Test />} />

        <Route>
          <Route path="/auth/login" element={<Login />} />
          <Route path="/auth/signup" element={<Signup />} />
          <Route path="/" element={<Navigate to="/auth/login" replace />} />
        </Route>

        <Route>
          <Route path="/dashboard" element={<PageLayout><Dashboard /></PageLayout>} />
          <Route path="/clock" element={<PageLayout><Clock /></PageLayout>} />
          <Route path="/schedule" element={<PageLayout><Scheduling /></PageLayout>} />
        </Route>
      </Routes>
    </div>
  );
}
