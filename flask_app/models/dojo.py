from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL("dojosandninjas").query_db(query, data)

    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db = connectToMySQL("dojosandninjas").query_db(query)
        all_dojos = []
        for dojo in dojos_from_db:
            all_dojos.append(cls(dojo))
        return all_dojos

    @classmethod
    def dojo_info(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojosandninjas').query_db( query , data )
        # groups will be a list of dojo objects from our raw data
        dojo = cls( results[0] )
        for data in results:
            # Now we parse the ninja data to make instances of ninja and add them into our list.
            ninja_data = {
                "id" : data['id'],
                "first_name" : data['first_name'],
                "last_name" : data['last_name'],
                "age" : data['age'],
                "dojo_id" : data['dojo_id'],
                "created_at" : data['created_at'],
                "updated_at" : data['updated_at'],
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        return dojo

    @classmethod
    def one_dojo(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('dojosandninjas').query_db(query, data)
        print(results)
        return cls (results[0])