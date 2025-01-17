#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, unique=True, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    """def __init__(self, *args, **kwargs):
        \"\"\"Instatntiates a new model\"\"\"
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)
        else:
            if kwargs.get("updated_at"):
                kwargs['updated_at'] = (
                        datetime.strptime(
                            kwargs['updated_at'],
                            '%Y-%m-%dT%H:%M:%S.%f')
                        )
            else:
                self.updated_at = datetime.now()
            if kwargs.get("created_at"):
                kwargs['created_at'] = (
                        datetime.strptime(
                            kwargs['created_at'],
                            '%Y-%m-%dT%H:%M:%S.%f')
                        )
            else:
                self.created_at = datetime.now()
            if kwargs.get("__class__"):
                del kwargs['__class__']
            if not kwargs.get("id"):
                self.id = str(uuid.uuid4())
            self.__dict__.update(kwargs)"""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id: str = str(uuid.uuid4())
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = self.created_at
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        # delete _sa_instance_state from the object if exists
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        print(self.updated_at)
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        # print(self.__dict__)
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        if self.created_at:
            dictionary['created_at'] = self.created_at.isoformat()
        if self.updated_at:
            dictionary['updated_at'] = self.updated_at.isoformat()
        if dictionary.get("_sa_instance_state"):
            # print("-------------------------dict----------------------------")
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """to delete the current instance from the storage"""
        from models import storage
        storage.delete()
