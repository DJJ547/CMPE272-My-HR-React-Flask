export default function Logout(){
  const confirmLogout = window.confirm("Are you sure you want to logout?");

  if (confirmLogout) {
    localStorage.removeItem("token");
    localStorage.removeItem("employee_information");
    window.location.href = "/auth/login";
  }
};
