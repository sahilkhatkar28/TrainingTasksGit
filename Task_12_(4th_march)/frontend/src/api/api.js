import axios from "axios";

const API_URL = "http://127.0.0.1:8000"; // Backend URL

// Upload file
export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return await axios.post(`${API_URL}/upload/`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
};

// Fetch file list
export const fetchFiles = async () => {
  return await axios.get(`${API_URL}/files/`);
};

// Download file
export const downloadFile = async (filename) => {
  window.location.href = `${API_URL}/download/${filename}`;
};
