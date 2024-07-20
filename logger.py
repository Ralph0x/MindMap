import logging
import os
from dotenv import load_dotenv

load_dotenv()

log_level = os.getenv("LOG_LEVEL", "INFO").upper()

# Setting up the logger
logger = logging.getLogger("MindMapBackend")
logger.setLevel(log_level)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(log_level)

# File Handler
log_file_path = os.getenv("LOG_FILE_PATH", "mindmapbackend.log")
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(log_level)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Applying formatter to handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Adding handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Example usage
logger.info("MindMap project has been successfully enhanced")