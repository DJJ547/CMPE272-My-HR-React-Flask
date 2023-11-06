import React from "react";

export default function Dashboard() {
  const employee_information = JSON.parse(localStorage.getItem("employee_information"));

  return (
    <div>
      <div className="min-h-screen">
        <h1>Hi! Alpha Team.</h1>
        {employee_information? (
          <h2>Hi! {employee_information.full_name} welcome back.</h2>
        ) : (
          <h2>error...</h2>
        )}
      </div>
    </div>
  );
}
