# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 08:39:05 2020

@author: teeji
"""


import peewee as pw
import db_config
import psycopg2

db = pw.PostgresqlDatabase(
    db_config.POSTGRES_DB,
    user=db_config.POSTGRES_USER, 
    password=db_config.POSTGRES_PASSWORD,
    host=db_config.POSTGRES_HOST, 
    port=db_config.POSTGRES_PORT
)

class BaseModel(pw.Model):
    class Meta:
        database = db

# Table Description
class Review(BaseModel):

    review = pw.TextField()
    rating = pw.IntegerField()
    suggested_rating = pw.IntegerField()
    sentiment_score = pw.FloatField()
    brand = pw.TextField()
    user_agent = pw.TextField()
    ip_address = pw.TextField()

    def serialize(self):
        data = {
            'id': self.id,
            'review': self.review,
            'rating': int(self.rating),
            'suggested_rating': int(self.suggested_rating),
            'sentiment_score': float(self.sentiment_score),
            'brand': self.brand,
            'user_agent': self.user_agent,
            'ip_address': self.ip_address
        }

        return data

# Connection and table creation
db.connect()
db.create_tables([Review])