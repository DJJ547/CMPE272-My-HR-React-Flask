export default function Logout() {
  const confirmLogout = window.confirm("Are you sure you want to logout?");

  if (confirmLogout) {
    const options = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };
    fetch("http://127.0.0.1:5000/auth/logout", options)
      .then((response) => response.json())
      .then((data) => {
        alert(data.message);
      })
      .catch((error) => console.error(error));
    localStorage.clear();
    window.location.href = "/auth/login";
  }
}
