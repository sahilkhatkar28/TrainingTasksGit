import { apiClient } from "./axiosClient";



export const addToCart = async (productId, quantity) => {
  const response = await apiClient.post("/cart/", { product_id: productId, quantity });
  return response.data;
};

export const getCart = async () => {
  const response = await apiClient.get("/cart/");
  return response.data;
};
export const checkout = async () => {
    const response = await fetch("http://127.0.0.1:8000/api/checkout/", {
      method: "POST",
    });
  
    if (!response.ok) {
      throw new Error("Checkout failed");
    }
  
    // ✅ Handle cases where the response body is empty
    const text = await response.text();
    return text ? JSON.parse(text) : {};  
  };

export const removeFromCart = async (itemId) => {
    const response = await fetch(`http://127.0.0.1:8000/api/cart/${itemId}/`, {
      method: "DELETE",
    });
  
    if (!response.ok) {
      throw new Error("Failed to remove item from cart");
    }
  
    return response.json();
  };
  