import os
from dotenv import load_dotenv
import json

load_dotenv()

FILE_PATH = os.getenv('MIND_MAP_FILE_PATH', 'mind_maps.json')

class MindMap:

    @staticmethod
    def _read_or_create_file():
        """Internal method to read mind map data or create file if it doesn't exist."""
        try:
            with open(FILE_PATH, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            with open(FILE_PATH, 'w') as file:
                json.dump({}, file)
            return {}
        except json.JSONDecodeError:
            return {}

    @staticmethod
    def _write_data(mind_maps):
        """Internal method to write data to the file."""
        with open(FILE_PATH, 'w') as file:
            json.dump(mind_maps, file, indent=4)

    @classmethod
    def create_mind_map(cls, map_id, mind_map):
        mind_maps = cls._read_or_create_file()

        if map_id in mind_maps:
            raise ValueError('MindMap with the given ID already exists.')

        mind_maps[map_id] = mind___map
        cls._write_data(mind_maps)

    @classmethod
    def update_mind_map(cls, map_id, mind_map):
        mind_maps = cls._read_or_create_file()

        if map_id not in mind_maps:
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
            raise ValueError('MindMap does not exist and cannot be deleted.')

    @classmethod
    def get_mind_map(cls, map_id):
        mind_maps = cls._read_or_create_file()

        if map_id in mind_maps:
            return mind_maps[map_id]
        else:
            raise ValueError('MindMap does not exist.')

    @classmethod
    def list_mind_maps(cls):
        return cls._read_or_create_file()