import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:5000/api"; // Change if needed

export const getProducts = async (page = 1, perPage = 5, category = "", search = "") => {
    const params = { page, per_page: perPage };
    if (category) params.category = category;
    if (search) params.search = search;

    const response = await axios.get(`${API_BASE_URL}/products`, { params });
    return response.data;
};
