#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects

        cls_objects = {}
        for key, obj in self.__objects.items():
            if type(obj) == cls:
                cls_objects[key] = obj
        return cls_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def delete(self, obj=None):
        """Deletes an object from __objects if it exists"""
        if obj is None:
            return

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]

    def save(self):
        """Saves storage dictionary to file"""
        temp_dict = {}
        for key, obj in self.__objects.items():
            temp_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(temp_dict, file)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as file:
                temp_dict = json.load(file)
                for key, value in temp_dict.items():
                    cls_name, obj_id = key.split('.')
                    class_obj = models.classes[cls_name]
                    obj_instance = class_obj(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
