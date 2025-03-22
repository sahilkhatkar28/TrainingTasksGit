import axios from 'axios';

const API_URL = 'http://localhost:5000'; // Adjust if necessary

// Upload image
export const uploadImage = (formData) => {
  return axios.post(`${API_URL}/upload`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
};

// Get all images
export const fetchImages = async () => {
    try {
        const response = await fetch("http://localhost:5000/images");
        return await response.json();
    } catch (error) {
        console.error("Error fetching images:", error);
        return [];
    }
};

// Delete an image
export const deleteImage = (id) => {
  return axios.delete(`${API_URL}/delete/${id}`);
};
