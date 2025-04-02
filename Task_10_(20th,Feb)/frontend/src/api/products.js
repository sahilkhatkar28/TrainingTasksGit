import { apiClient } from "./axiosClient";

export const getProducts = async () => {
  const response = await apiClient.get("/products/");
  return response.data;
};
