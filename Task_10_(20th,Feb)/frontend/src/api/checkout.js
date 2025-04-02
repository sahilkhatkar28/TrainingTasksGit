import { apiClient } from "./axiosClient";

export const checkout = async () => {
  const response = await apiClient.post("/checkout/");
  return response.data;
};
