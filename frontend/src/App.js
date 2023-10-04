import React from "react";
import { Routes, Route } from "react-router-dom";
import "./App.css";

import Header from "./components/header";
import Home from "./pages/Home";
import Test from "./pages/Test";


export default function App() {
  return (
    <div>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/test" element={<Test />} />
      </Routes>
    </div>
  );
}
