import React, { useEffect, useState } from "react";
import Chart from "react-apexcharts";

export default function Dashboard() {
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
    fetch('http://localhost:5000/dashboard')
      .then(response => response.json())
      .then(data => {
        setChartData({
          ...chartData,
          options: { ...chartData.options, xaxis: { categories: data.years } },
          series: [{ ...chartData.series[0], data: data.salaries }]
        });
      });
  }, []);

  return (


  <div className="min-h-screen bg-gray-100 flex justify-center ">
      {employee_information ? (
        <div className="space-y-6">

          {/* User Information Card */}
          <div className="max-w-xl mx-auto p-6 shadow-md rounded-xl bg-white">
            <img src="https://source.unsplash.com/150x150/?portrait?3" alt="" className="w-32 h-32 mx-auto rounded-full" />
            <div className="space-y-4 text-center divide-y">
              <div className="my-2 space-y-1">
                <h2 className="text-xl font-semibold">{employee_information.full_name}</h2>
                <p className="text-sm text-gray-500">Department Name</p>
                <p className="text-sm text-gray-500">title</p>
              </div>
              <div className="pt-2">
                <span className="text-gray-500">Employee No. {employee_information.employee_no}</span>
                <p className="text-sm text-gray-500">Motto: When life hands you lemons, make lemonade.</p>
              </div>
            </div>
          </div>
          <div>
            <p>Salary History
            </p>
          </div>
          {/* Chart */}
          <div className="max-w-xl mx-auto">
            <Chart
              options={chartData.options}
              series={chartData.series}
              type="area"
              width="600"
            />
          </div>
        </div>
      ) : (
        <h2 className="text-center text-xl text-red-500">Error...</h2>
      )}
    </div>

);

}
