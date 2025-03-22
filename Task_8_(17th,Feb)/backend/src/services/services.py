import os
from werkzeug.utils import secure_filename
from src.config.config import Config
from src.models.models import db, Image
from flask import request, jsonify, send_from_directory

class ImageService:
    
    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

    @staticmethod
    def save_image(file):
        if not file or file.filename == '':
            return None, 'No selected file'

        if not ImageService.allowed_file(file.filename):
            return None, 'Invalid file type'

        filename = secure_filename(file.filename)
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
        
        file.save(filepath)

        new_image = Image(
            filename=filename,
            filepath=filepath,
            file_size=os.path.getsize(filepath),
            file_type=file.mimetype
        )
        
        db.session.add(new_image)
        db.session.commit()
        return new_image, None

    @staticmethod
    def get_images():
        """Retrieve all images from the database and return as JSON."""
        images = Image.query.all()
    
        if not images:
            return jsonify({'error': 'No images found'}), 404

    # Convert Image objects into a JSON serializable format
        image_list = [{
            'id': image.id,
            'filename': image.filename,
            'filepath': image.filepath,
            'file_size': image.file_size,
            'file_type': image.file_type
        } for image in images]

        return jsonify(image_list), 200
     
    @staticmethod
    def get_image_by_id(image_id):
        return Image.query.get(image_id)

    @staticmethod
    def delete_image(image):
        if os.path.exists(image.filepath):
            os.remove(image.filepath)
        db.session.delete(image)
        db.session.commit()
