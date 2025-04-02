import { apiClient } from "./axiosClient";

export const getCategories = async () => {
  const response = await apiClient.get("/categories/");
  return response.data;
};
