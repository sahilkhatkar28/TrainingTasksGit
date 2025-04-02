import { useState } from "react";
import { registerUser } from "../api/authApi";

const RegisterForm = () => {
  const [formData, setFormData] = useState({ username: "", email: "" });
  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value.trim(), // Trim to prevent unnecessary spaces
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("Submitting form data:", formData); // Debugging statement

    try {
      const response = await registerUser(formData);
      console.log("Server response:", response); // Debugging statement
      setMessage(response.message);
    } catch (error) {
      console.error("Error:", error);
      setMessage(error.message || "Registration failed");
    }
  };

  return (
    <div>
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <button type="submit">Register</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default RegisterForm;
