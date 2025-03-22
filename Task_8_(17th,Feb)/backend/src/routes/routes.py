from flask import Blueprint
from src.controller.image_controller import ImageController

routes = Blueprint('routes', __name__)

routes.route('/upload', methods=['POST'])(ImageController.upload_image)
routes.route('/images', methods=['GET'])(ImageController.get_images)
routes.route('/images/<int:image_id>', methods=['GET'])(ImageController.get_image)
routes.route('/delete/<int:image_id>', methods=['DELETE'])(ImageController.delete_image)
