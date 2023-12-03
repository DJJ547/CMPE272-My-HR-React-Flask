import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
// ... other imports
import "./App.css";

//utilities
import ProtectedRoute from "./utilitiies/ProtectedRoute";

//components
import PageLayout from "./components/PageLayout";

//pages
import Test from "./pages/Test";
import Login from "./pages/auth/Login";
import Signup from "./pages/auth/Signup";

import Dashboard from "./pages/Dashboard";
import Clock from "./pages/Clock";
import Message from "./pages/Message";
import Pay from "./pages/Pay";
import Scheduling from "./pages/Scheduling";
import Setting from "./pages/Setting";

export default function App() {
  return (
    <div>
      <Routes>
        <>
          <Route path="/test" element={<Test />} />
        </>

        <Route>
          <Route path="/auth/login" element={<Login />} />
          {/* <Route path="/auth/signup" element={<Signup />} /> */}
          <Route path="/" element={<Navigate to="/auth/login" replace />} />
        </Route>

        <Route>
          <Route path="/dashboard" element={<ProtectedRoute><PageLayout><Dashboard /></PageLayout></ProtectedRoute>} />
          <Route path="/dashboard/clock" element={<ProtectedRoute><PageLayout><Clock /></PageLayout></ProtectedRoute>} />
          <Route path="/dashboard/message" element={<ProtectedRoute><PageLayout><Message /></PageLayout></ProtectedRoute>} />
          <Route path="/dashboard/pay" element={<ProtectedRoute><PageLayout><Pay /></PageLayout></ProtectedRoute>} />
          <Route path="/dashboard/scheduling" element={<ProtectedRoute><PageLayout><Scheduling /></PageLayout></ProtectedRoute>} />
          <Route path="/dashboard/setting" element={<ProtectedRoute><PageLayout><Setting /></PageLayout></ProtectedRoute>} />
        </Route>
      </Routes>
    </div>
  );
}
