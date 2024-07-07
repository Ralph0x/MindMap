import os
from dotenv import load_dotenv
import json
import logging

load_dotenv()

FILE_PATH = os.getenv('MIND_MAP_FILE_PATH', 'mind_maps.json')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MindMap:

    @staticmethod
    def _read_or_create_file():
        try:
            with open(FILE_PATH, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.warning(f"{FILE_PATH} not found. A new file will be created.")
            try:
                with open(FILE_PATH, 'w') as file:
                    json.dump({}, file)
                return {}
            except Exception as e:
                logging.error(f"Error creating {FILE_PATH}: {e}")
                raise
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from {FILE_PATH}: {e}")
            return {}
        except Exception as e:
            logging.error(f"Unexpected error reading {FILE_PATH}: {e}")
            raise

    @staticmethod
    def _write_data(mind_maps):
        try:
            with open(FILE_PATH, 'w') as file:
                json.dump(mind_maps, file, indent=4)
        except Exception as e:
            logging.error(f"Failed to write to {FILE_NAME}: {e}")
            raise

    @classmethod
    def create_mind_map(cls, map_id, mind_map):
        mind_maps = cls._read_or_create_file()

        if map_id in mind_maps:
            logging.warning(f"MindMap with the given ID {map_id} already exists.")
            raise ValueError('MindMap with the given ID already exists.')

        mind_maps[map_id] = mind_map
        cls._write_data(mind_maps)

    @classmethod
    def update_mind_map(cls, map_id, mind_map):
        mind_maps = cls._read_or_create_file()

        if map_id not in mind_maps:
            logging.warning(f"MindMap with ID {map_id} does not exist and cannot be updated.")
            raise ValueError('MindMap does not exist and cannot be updated.')

        mind_maps[map_id] = mind_map
        cls._write_data(mind_maps)

    @classmethod
    def delete_mind_map(cls, map_id):
        mind_maps = cls._read_or_create_file()

        if map_id in mind_maps:
            del mind_maps[map_id]
            cls._write_data(mind_maps)
        else:
            logging.warning(f"MindMap with ID {map_id} does not exist and cannot be deleted.")
            raise ValueError('MindMap does not exist and cannot be deleted.')

    @classmethod
    def get_mind_map(cls, map_id):
        mind_maps = cls._read_or_create_file()

        if map_id in mind_maps:
            return mind_maps[map_id]
        else:
            logging.info(f"MindMap with ID {map_id} does not exist.")
            raise ValueError('MindMap does not exist.')

    @classmethod
    def list_mind_maps(cls):
        return cls._read_or_create_version to the Shader Compiler.