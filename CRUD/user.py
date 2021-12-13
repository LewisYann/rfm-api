from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from config import app,db
from MODEL.user import User


class CrudUser:
    @staticmethod
    def get_info_by_user(id):
        cursor = User.objects(idUser=id).first()
        if cursor is not None:
            return cursor.to_json()
        else:
            return False

    @staticmethod
    def get_login(login,password):
        cursor = User.objects(login=login,password=password).first()
        if cursor is not None:
            return {"statu":True, "data":cursor.to_json()}
        else:
            return {"statu":False}


    @staticmethod
    def delete_user(id):
        cursor = User.Objects(idUser=id).first()
        cursor.delete()

    @staticmethod
    def get_all_user():
        cursor = User.objects()
        return [User.to_json() for User in cursor]


    @staticmethod
    def create_user(record):
        user=User(**record)
        user.save()
        return user.to_json()



