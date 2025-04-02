import os
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {"pdf", "jpg", "png", "jpeg","html","zip"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
