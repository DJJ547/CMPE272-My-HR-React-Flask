import axios from "axios";
export default function Setting() {
    const handleChangePassword = (e) => {
        e.preventDefault();
        const emp_no = JSON.parse(localStorage.getItem("employee_information")).employee_no;
        const currentPassword = e.target.currentPassword.value;
        const newPassword = e.target.NewPassword.value;
        const data = {
          currentPassword: currentPassword,
          newPassword: newPassword,
            emp_no: emp_no
        };
        axios.post("http://localhost:5000/auth/changePassword", data).then((res) => {
            alert(res.data.message);
            }).catch((err) => {
            console.log(err);
            });
      };
  return (
    <div>
      <div class="flex flex-col items-center justify-center h-screen light">
        <div class="w-full max-w-md bg-white rounded-lg shadow-md p-6">
          <h2 class="text-2xl font-bold text-gray-800 mb-4">
            Change password
          </h2>

          <form class="flex flex-col" onSubmit={handleChangePassword}>
            <input
              placeholder="Enter your current password"
              class="bg-gray-100 text-gray-800 border-0 rounded-md p-2 mb-4 focus:bg-gray-200 focus:outline-none focus:ring-1 focus:ring-blue-500 transition ease-in-out duration-150"
              name="currentPassword"
            />
            <input
              placeholder="Enter New password"
              class="bg-gray-100 text-gray-800 border-0 rounded-md p-2 mb-4 focus:bg-gray-200 focus:outline-none focus:ring-1 focus:ring-blue-500 transition ease-in-out duration-150"
              name="NewPassword"
            />

            <button
              class="bg-gradient-to-r from-indigo-500 to-blue-500 text-white font-bold py-2 px-4 rounded-md mt-4 hover:bg-indigo-600 hover:to-blue-600 transition ease-in-out duration-150"
              type="submit"
            >
              Submit
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
