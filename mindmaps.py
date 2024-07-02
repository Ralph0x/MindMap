import os
from dotenv import load_dotenv
import json

load_dotenv()

FILE_PATH = os.getenv('MIND_MAP_FILE_PATH', 'mind_maps.json')

def load_mind_maps():
    try:
        with open(FILE_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_mind_maps(mind_maps):
    with open(FILE_PATH, 'w') as file:
        json.dump(mind_maps, file, indent=4)

def create_mind_map(map_id, mind_map):
    mind_maps = load_mind_maps()
    
    if map_id in mind_maps:
        raise ValueError('MindMap with the given ID already exists.')
    
    mind_maps[map_id] = mind_map
    save_mind_maps(mind_maps)

def update_mind_map(map_id, mind_map):
    mind_maps = load_mind_maps()
    
    if map_id not in mind_maps:
        raise ValueError('MindMap does not exist and cannot be updated.')
    
    mind_maps[map_id] = mind_map
    save_mind_maps(mind_maps)

def delete_mind_map(map_id):
    mind_maps = load_mind_maps()
    
    if map_id in mind_maps:
        del mind_maps[map_id]
        save_mind_maps(mind_maps)
    else:
        raise ValueError('MindMap does not exist and cannot be deleted.')

def get_mind_map(map_id):
    mind_maps = load_mind_maps()
    
    if map_id in mind_maps:
        return mind_maps[map_id]
    else:
        raise ValueError('MindMap does not exist.')

def list_mind_maps():
    return load_mind_maps()