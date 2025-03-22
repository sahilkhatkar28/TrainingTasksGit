import React from 'react';

import { useState } from 'react';

import UploadForm from './components/UploadForm';
import ImageList from './components/ImageList';
import './App.css';

function App() {
  const [refresh, setRefresh] = useState(false);

  const handleUploadSuccess = () => {
    setRefresh(!refresh);
  };

  const handleDeleteSuccess = () => {
    setRefresh(!refresh);
  };

  return (
    <div className="App">
      <h1>Image Upload App</h1>
      <UploadForm onUploadSuccess={handleUploadSuccess} />
      <ImageList onDeleteSuccess={handleDeleteSuccess} />
    </div>
  );
}

export default App;
