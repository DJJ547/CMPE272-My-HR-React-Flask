import React, { useEffect, useState } from "react";
import Chart from "react-apexcharts";

export default function AssignShift() {
  const employee_information = JSON.parse(localStorage.getItem("employee_information"));
  console.log(employee_information);

  // const title = employee_information.title;

  const [chartData, setChartData] = useState({
    options: {
      chart: {id: "basic-bar"},
      xaxis: {categories: [] }
    },
    series: [
      {name: "Salary",data: []}]
  });

  useEffect(() => {
    fetch('http://localhost:5000/dashboard/manager/schedule')
      .then(response => response.json())
      .then(data => {
      });
  }, []);

  return (


  <div className="min-h-screen bg-gray-100 flex justify-center ">
      
    </div>

);

}