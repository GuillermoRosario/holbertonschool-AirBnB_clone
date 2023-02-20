#!/usr/bin/python3
"""
Base Class Module 
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base Class Model that defines
    all common atributes/ methods
    """

    def __init__ (self, *args, **kwargs):
        """Constructor"""
        if kwargs:
            for keys, value in kwargs.items():
                if keys in ['created_at', 'updated_at']:
                    self.__dict__[keys] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif keys != '__class__':
                    self.__dict__[keys] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Return String Rep of Instance
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
    
    def save(self):
        """
        Change the time of instance attr change
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary with all 
        keys and values of __dict__ including new attrs
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
