import React from "react";
import { useSelector } from "react-redux";

export default function Dashboard() {
  const currentUser = useSelector((state) => state.user.value)
 
  return (
    <div>
      <div className="min-h-screen">
        <h1>Hi! Alpha Team.</h1>
        {currentUser ? (
          <h2>Hi! {currentUser} welcome back.</h2>
        ) : (
          <h2>Loading...</h2>
        )}
      </div>
    </div>
  );
}
