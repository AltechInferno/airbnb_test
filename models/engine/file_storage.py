#!/usr/bin/python3
"""This initiates the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Constitutes an abstracted storage engine.
    Attributes:
        __file_path: name given to the file to save objects to.
        __objects: dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}


    def reload(self):
        """This deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as fs:
                objDict = json.load(fs)
                for o in objDict.values():
                    clsName = o["__class__"]
                    del o["__class__"]
                    self.new(eval(clsName)(**o))
        except FileNotFoundError:
            return

    def all(self, cls=None):  
        """ the dictionary __objects."""
        if cls is None:
            return FileStorage.__objects
        objects = {}    
        for obj in FileStorage.__objects.values():  
            if type(obj) == eval(cls):   
                objects[obj.id] = obj
        return objects


    def save(self):
        """this serializes __objects to the JSON file __file_path."""
        oDict = FileStorage.__objects
        objDict = {obj: oDict[obj].to_dict() for obj in oDict.keys()}
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as fs:
            json.dump(objDict, fs)


    def new(self, obj):
        """Sets __objects obj with key <obj_class_name>.id"""
        oclassName = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(oclassName, obj.id)] = obj

