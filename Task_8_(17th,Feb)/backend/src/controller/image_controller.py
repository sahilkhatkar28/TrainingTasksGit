from flask import request, jsonify, send_from_directory
from src.services.services import ImageService
from src.config.config import Config

class ImageController:
    
    @staticmethod
    def upload_image():
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        image, error = ImageService.save_image(file)
        
        if error:
            return jsonify({'error': error}), 400
        
        return jsonify({'message': 'File uploaded successfully', 'id': image.id}), 201

    @staticmethod
    def get_images():
        return ImageService.get_images()
    
    @staticmethod
    def get_image(image_id):
        image = ImageService.get_image_by_id(image_id)
        if not image:
            return jsonify({'error': 'Image not found'}), 404
        return send_from_directory(Config.UPLOAD_FOLDER, image.filename) 
        

    @staticmethod
    def delete_image(image_id):
        image = ImageService.get_image_by_id(image_id)
        if not image:
            return jsonify({'error': 'Image not found'}), 404

        ImageService.delete_image(image)
        return jsonify({'message': 'Image deleted successfully'}), 200
