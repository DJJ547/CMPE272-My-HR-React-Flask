export default function Logout(){
  const confirmLogout = window.confirm("Are you sure you want to logout?");

  if (confirmLogout) {
    localStorage.clear();
    window.location.href = "/auth/login";
  }
};
