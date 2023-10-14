#!/usr/bin/python3

#creating a class BaseModel that defines all common methods of classes
#id: unique identification, 
#created_at: when it was created (born) , 
#updated_at: when object is being updated
#public instance attributes
# public instance methods
#we have to import our date time
#kwargs key arguements : passes a variable number of keyword 
#arguements to a function
#then the arguements are accessible as a dictionary within a function

import uuid
from datetime import datetime
from models.engine.file_storage import storage
 class BaseModel:
     def __init__(self):  # creates id,created_at , updated_at

         def save(self):
             self.updated_at = datetime,now()
             storage.save()

         self.id = str(uuid.uuid4())
         self.created_at = datetime.now()
         self.updated_at = self.created_at

          if kwargs:
              '''
               if kwargs is not empty:
               we will create an instance from a dict
               check if the key is one of the timestamp 
               then convert to a datetime object 

              '''
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)  #set attributr of instance with key and value
                else:  # if kwarsg is empty go back to this instabce or create this instance
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = self.created_at
    

    def save(self): 
        self.updated_at = datetime.now()

    def to_dict(self):  # returns a dictionary of object
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):#definining how the method should be represented as a string
        return "[{}] ({}) {}".format(self.__class__.name__, self.id, self.__dict__)


my_model = BaseModel()
print(my_model)
print(my_model.to_dict())
my_model.save()
dict = my_model.to_dict()
print(dict)

#recreating an instance from my_dict

instance = BaseModel(**dict)
print(instance)
