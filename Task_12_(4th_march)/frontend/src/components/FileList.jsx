import { useEffect, useState } from "react";
import { fetchFiles, downloadFile } from "../api/api";

const FileList = () => {
  const [files, setFiles] = useState([]);

  useEffect(() => {
    loadFiles();
  }, []);

  const loadFiles = async () => {
    const response = await fetchFiles();
    setFiles(response.data);
  };

  return (
    <div className="file-list">
      <h3>Uploaded Files</h3>
      <ul>
        {files.map((file) => (
          <li key={file.id}>
            {file.filename} 
            <button onClick={() => downloadFile(file.filename)}>Download</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FileList;
