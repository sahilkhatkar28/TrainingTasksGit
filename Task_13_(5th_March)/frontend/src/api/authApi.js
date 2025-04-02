export const registerUser = async (userData) => {
  console.log("Sending Data:", userData); // Debugging statement

  try {
    const response = await fetch("http://localhost:5000/api/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(userData),
    });

    const data = await response.json();
    console.log("Server Response:", data); // Debugging statement

    if (!response.ok) throw new Error(data.message || "Registration failed");
    return data;
  } catch (error) {
    console.error("Error in API call:", error);
    throw error.message;
  }
};
