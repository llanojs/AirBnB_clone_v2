
#!/usr/bin/python3
"""Start link class to table in database
"""
from models.base_model import BaseModel, Base
from os import getenv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

    Base.metadata.create_all(engine)


    class DBStorage:
        """ DBs class """
        __engine = None
        __session = None
        

        def __init__(self):
            """Variables to DBStorage"""
            username = getenv('HBNB_MYSQL_USER')
            password = getenv('HBNB_MYSQL_PWS')
            host = getenv('HBNB_MYSQL_DB')
            db_name = getenv('HBNB_MYSQL_DB')
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}}/{}'.
                                           format(username,
                                                  password,
                                                  host,
                                                  db_name), pool_pre_ping=True)
            if getenv('HBNB_ENV') == 'test':
                Base.metadata.drop_all(self.__engine)


        def all(self, cls=None):
            """Objects that depending of the class name"""
            
            dictionary = {}
            classes = [User, State, City, Amenity, Place, Review]

            if cls == None:
                _query = self.session(User,
                                      State,
                                      City,
                                      Amenity,
                                      Place,
                                      Review).all()
                
                for obj in _query:
                    key_obj = ("{}.{}".format(obj.__class__.name, obj.id))
                    dictionary.update({key_obj: obj})
                return dictionary
            else:
                if cls in classes:
                    _query = self.session(cls).all()
                    for obj in _query:
                        key_obj = ("{}.{}".format(obj.__class__.name, obj.id))
                        dictionary.update({key_obj: obj})
                    return dictionary
                else:
                    return {}

        def new(self, obj):
            """New object in database"""
            self.session.add()
            
        def save(self):
            """save changes"""
            self.session.commit()

        def delete(self, obj=None):
            """Delete objetc from database"""
            self.session.delete(obj)

        def reload(self):
            """Creating all tables"""
            Base.metadata.create_all(self.__engine)
            
            session_factory = sessionmaker(self.__engine, expire_on_commit=False)
            self.__session = scoped_session(session_factory)
            
            
        

