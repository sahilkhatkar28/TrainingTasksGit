import React, { useEffect, useState } from "react";
import { fetchImages } from "../services/api";
import { deleteImage } from "../services/api";

const ImageList = () => {
    const [images, setImages] = useState([]);
    const [message, setMessage] = useState("");
    useEffect(() => {
        const loadImages = async () => {
            try {
                const data = await fetchImages();
                setImages(data);
            } catch (error) {
                console.error("Error fetching images:", error);
            }
        };
        loadImages();
    }, []);
    const handleDelete = async (id) => {
        try {
          await deleteImage(id);
          onDeleteSuccess(); // Refresh the image list
        } catch (error) {
          setMessage('Failed to delete image');
        }
        setTimeout(() => {
            window.location.reload();
        }, 500);
      };

   

    return (
        <div style={{ padding: "20px", maxWidth: "800px", margin: "auto" }}>
            <h2 style={{ textAlign: "center" }}>Uploaded Images</h2>
            <div style={{ display: "flex", flexWrap: "wrap", gap: "15px", justifyContent: "center" }}>
                {images.length > 0 ? (
                    images.map((image) => (
                        <div key={image.id} style={{ textAlign: "center", border: "1px solid #ddd", padding: "10px", borderRadius: "10px" }}>
                            <img 
                                src={`http://localhost:5000/images/${image.id}`} 
                                alt={image.filename || "Uploaded image"} 
                                style={{ width: "150px", height: "auto", borderRadius: "8px", objectFit: "cover" }} 
                            />
                            <button 
                                style={{ 
                                    display: "block", 
                                    marginTop: "10px", 
                                    backgroundColor: "#ff4d4d", 
                                    color: "white", 
                                    border: "none", 
                                    padding: "8px 12px", 
                                    cursor: "pointer", 
                                    borderRadius: "5px",
                                    fontSize: "14px"
                                }}
                                onClick={() => handleDelete(image.id)}
                            >
                                Delete
                            </button>
                        </div>
                    ))
                ) : (
                    <p style={{ textAlign: "center", color: "gray" }}>No images found</p>
                )}
            </div>
        </div>
    );
};

export default ImageList;
