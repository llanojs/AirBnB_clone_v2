#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

asociation = Table('place_amenity', Base.metadata,
                   Column('place_id',
                          String(60),
                          ForeignKey("places.id"),
                          primary_key=True,
                          nullable=False),
                   Column('amenity_id',
                          String(60),
                          ForeignKey("amenities.id"),
                          primary_key=True,
                          nullable=False)
                   )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review',
            backref='place',
            cascade='all, delete')

        amenities = relationship(
            'Amenity',
            secondary="place_amenity",
            viewonly=False
        )
    else:
        @property
        def reviews(self):
            """Getter method for reviews
            Return: list of reviews with place_id equal to self.id
            """
            from models import storage
            from models.review import Review
            review_dict = storage.all(Review)
            review_list = []

            for _review in review_dict.values():
                if _review.place_id == self.id:
                    review_list.append(_review)
            return review_list

        @property
        def amenities(self):
            """Getter method for reviews
            Return: list of reviews with place_id equal to self.id
            """
            from models import storage
            from models.amenities import Amenity
            amenities_saved = storage.all(Amenity)
            amenities_obj = []

            for obj in amenities_saved.values():
                if obj.id in amenity_ids:
                    amenities_obj.append(obj)
            return amenities_obj

        @amenities.setter
        def amenities(self, obj):
            """obj inside """
            from models.amenities import Amenity
            if isinstance(obj, Amenity):
                amenity_ids.append(obj.id)
