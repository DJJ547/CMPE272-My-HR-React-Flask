import React, { useState } from 'react';

const Settings = () => {
  const employee_information = JSON.parse(localStorage.getItem("employee_information"));
  const [newMotto, setNewMotto] = useState(employee_information.motto);
  const [newProfilePicUrl, setNewProfilePicUrl] = useState(employee_information.profile_pic);
  const handleSubmit = (e) => {
    e.preventDefault();
    const employee_no = employee_information.employee_no;
    const token = JSON.parse(localStorage.getItem("token"));
    fetch("http://localhost:5000/setting/updateprofile", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify({ newMotto, newProfilePicUrl }),
    })
    .then((response) => response.json())
    .then((data) => {
      console.log(data)
      if(data.message === "Profile updated successfully"){
        console.log(newMotto, newProfilePicUrl);
        localStorage.setItem('employee_information', JSON.stringify({
          ...employee_information,
          motto: newMotto,
          profile_pic: newProfilePicUrl,
        }));
        window.location.href = "/dashboard";
      }
      else{
        alert(data.message);
      }
    }
    )
  }
  const handleMottoChange = (e) => {
    setNewMotto(e.target.value);

  }
  const handleProfilePicUrlChange = (e) => {
    setNewProfilePicUrl(e.target.value);
  }
  // Handlers...

  return (
    <div className="min-h-screen bg-gray-100 flex justify-center items-center p-4">
      <div className="w-full max-w-md bg-white rounded-lg shadow-md p-6">
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="profilePicUrl" className="block text-sm font-semibold text-gray-700">Profile Picture URL</label>
            <input
              type="text"
              id="profilePicUrl"
              className="mt-1 w-full border border-gray-300 rounded-md shadow-sm p-2"
              value={newProfilePicUrl}
              onChange={handleProfilePicUrlChange}
              placeholder="http://example.com/pic.jpg"
            />
          </div>
          <div>
            <label htmlFor="motto" className="block text-sm font-semibold text-gray-700">Motto</label>
            <input
              type="text"
              id="motto"
              className="mt-1 w-full border border-gray-300 rounded-md shadow-sm p-2"
              value={newMotto}
              onChange={handleMottoChange}
              placeholder="Enter your new motto"
            />
          </div>
          <button type="submit" className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
            Update Info
          </button>
        </form>
      </div>
    </div>
  );
};

export default Settings;
