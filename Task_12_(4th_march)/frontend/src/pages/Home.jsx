import FileUpload from "../components/FileUpload";
import FileList from "../components/FileList";
import { useState } from "react";

const Home = () => {
  const [refresh, setRefresh] = useState(false);

  return (
    <div>
      <h1>FastAPI File Service</h1>
      <FileUpload refreshFiles={() => setRefresh(!refresh)} />
      <FileList key={refresh} />
    </div>
  );
};

export default Home;
