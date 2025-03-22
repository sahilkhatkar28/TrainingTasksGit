import React from 'react';

import { useState } from 'react';
import { uploadImage } from '../services/api';

const UploadForm = ({ onUploadSuccess }) => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const onFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const onFileUpload = async () => {
    if (!file) {
      setMessage('No file selected');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await uploadImage(formData);
      setMessage(response.data.message);
      onUploadSuccess(); // Refresh the image list
    } catch (error) {
      setMessage('Failed to upload file');
    }
    setTimeout(() => {
        window.location.reload();
    }, 500);
  };

  return (
    <div>
      <h2>Upload Image</h2>
      <input type="file" onChange={onFileChange} />
      <button onClick={onFileUpload}>Upload</button>
      <p>{message}</p>
    </div>
  );
};

export default UploadForm;
