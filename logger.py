import logging
import os
from dotenv import load_dotenv

load_dotenv()

log_level_env = os.getenv("LOG_LEVEL", "INFO").upper()

mindmap_logger = logging.getLogger("MindMapBackend")
mindmap_logger.setLevel(log_level_env)

console_log_handler = logging.StreamHandler()
console_log_handler.setLevel(log_level_env)

log_file_path_env = os.getenv("LOG_FILE_PATH", "mindmapbackend.log")
file_log_handler = logging.FileHandler(log_file_path_env)
file_log_handler.setLevel(log_level_env)

log_message_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

log_formatter = logging.Formatter(log_message_format)

console_log_handler.setFormatter(log_formatter)
file_log_handler.setFormatter(log_formatter)

mindmap_logger.addHandler(console_log_handler)
mindmap_logger.addHandler(file_log_handler)

mindmap_logger.info("MindMap project has been successfully enhanced")