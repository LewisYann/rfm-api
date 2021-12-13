from config import app
from flask import request, jsonify, session, redirect, render_template
from config import app, db
from CRUD.setting import CrudSetting
from CRUD.mission import CrudMission
from CRUD.user import CrudUser
import json
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from functools import wraps
import uuid
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

#login

@app.route('/login', methods=['POST'])
def login():
    record=json.loads(request.data)
    data= CrudUser.get_login(record['login'], record['password'])
    print(data)
    if data["statu"]:
        return jsonify(data['data'])
    else:
        return jsonify({"statu": 404})

@app.route('/login/get/all/<id>', methods=['GET'])
def get_all_login(id):
    data= CrudUser.get_info_by_user(id)
    print(data)
    if data==False:
        return jsonify({"statu":"not found"})
    elif data["authorization"]>1 :
        return jsonify(CrudUser.get_all_user())
    else:
        return jsonify({"error":"acces denied"})




@app.route('/create/user', methods=['POST'])
def create_user():
    record=json.loads(request.data)
    idUser=str(uuid.uuid4())
    token = jwt.encode({'idUser' : idUser, 'exp' : datetime.utcnow() + timedelta(minutes=600)}, app.config['SECRET_KEY'])
    record['token']=token
    record['refresh_token']=token
    record['idUser']=idUser
    data = CrudUser.create_user(record)
    return jsonify(data)

@app.route('/create/<id>', methods=['GET'])
def delete_user(id):
    CrudUser.delete_user(id)
    return {"statu":200}



@app.route('/list/setting', methods=['GET'])
def list_setting():
    return jsonify(CrudSetting.get_all_setting())

@app.route('/get/setting/<id>', methods=['GET'])
def get_setting_by_id(id):
    return jsonify(CrudSetting.get_setting_by_people_is(people_id=id))

@app.route('/create/setting', methods=['POST'])
def create_setting():
    record=json.loads(request.data)
    return (CrudSetting.create_setting(record))

@app.route('/delete/setting/<id>', methods=['GET'])
def delete_setting(id):
    return CrudSetting.delete_setting_by_id(id)

@app.route('/update/setting', methods=['POST'])
def update_setting():
    record=json.loads(request.data)
    return (CrudSetting.update_setting(record))

#Mission endPoints
@app.route('/list/mission', methods=['GET'])
def list_mission():
    return jsonify(CrudMission.get_all_mission())

@app.route('/get/mission/<id>', methods=['GET'])
def get_mission_by_id(id):
    return (CrudMission.get_mission_by_id(id))

@app.route('/create/mission', methods=['POST'])
def create_mission():
    record=json.loads(request.data)
    return (CrudMission.create_mission(record))

@app.route('/delete/mission/<id>', methods=['GET'])
def delete_mission(id):
    return (CrudMission.delete_by_id(id_mission=id))


if __name__ == "__main__":
    app.run(debug=True)