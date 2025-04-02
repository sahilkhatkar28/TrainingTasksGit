import { useState } from "react";
import { uploadFile } from "../api/api";

const FileUpload = ({ refreshFiles }) => {
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleUpload = async () => {
    if (!file) {
      setUploadStatus("Please select a file.");
      return;
    }

    try {
      await uploadFile(file);
      setUploadStatus("Upload successful!");
      refreshFiles();
    } catch (error) {
      setUploadStatus("Upload failed!");
    }
  };

  return (
    <div className="upload-container">
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      <p>{uploadStatus}</p>
    </div>
  );
};

export default FileUpload;
