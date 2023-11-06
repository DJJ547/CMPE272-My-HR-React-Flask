import { BrowserRouter as Router, Route, Navigate } from "react-router-dom";

const useAuth = {
  isAuthenticated: () => {
    // Check if the token exists and is valid
    const token = localStorage.getItem("token");
    // Add your logic to check the validity of the token here
    return token !== null && token !== undefined;
  },
};

const ProtectedRoute = ({children}) => {
  const auth = useAuth.isAuthenticated();
  
  return auth ? children : <Navigate to="/auth/login" />;  
};

export default ProtectedRoute;
