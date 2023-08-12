#!/usr/bin/python3

"""We define the class for BaseModel """

from uuid import uuid4
import models
from datetime import datetime


class BaseModel:
        """This stands for the BaseModel of the project. """


        def __init__(self, *args, **kwargs):
            """We Init a new basemodel
            Arg:
                *args: this is unused.
                **kwargs: the key/value pairs of attributes
            """

            td = "%Y-%m-%dT%H:%M:%S.%f"
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

            if len(kwargs) != 0:

                for i, j in kwargs.items():

                    if i == "created_at" or i == "updated_at":

                        self.__dict__[i] = datetime.strptime(j, td)

                    else:

                        self.__dict__[i] = j

            else:

                models.storage.new(self)


        def save(self):
            """We update updated_at with the current date and time value"""

            self.updated_at = datetime.today()

            models.storage.save()


        def to_dict(self):
            """We return the dic of the basemodel which
            includes the key and value pair __class__ representing
            our class name of the obj.
            """

            rDictionary = self.__dict__.copy()
            rDictionary['__class__'] = self.__class__.__name__
            rDictionary['created_at'] = self.created_at.isoformat()
            rDictionary['updated_at'] = self.updated_at.isoformat()
            return rDictionary


        def __str__(self):
            """We revert the print / str rep of the basemodel """

            class_name = self.__class__.__name__
            return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

