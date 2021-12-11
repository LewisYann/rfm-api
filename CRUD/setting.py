import json

from flask import jsonify, request

from config import db
from MODEL.setting import Setting

class CrudSetting:

    @staticmethod
    def get_all_setting():
        settings = Setting.objects()
        return [Setting._to_json() for Setting in settings]

    @staticmethod
    def get_setting_by_people_is(people_id):
        Setting_get= Setting.objects(people_id=people_id).first()
        return Setting_get.to_json()

    @staticmethod
    def delete_setting_by_id(people_id):
        Setting_get= Setting.objects(people_id=people_id).first()
        if not Setting_get:
            return jsonify({'error': 'data not found'})
        else:
            Setting_get.delete()
        return jsonify(Setting_get.to_json())

    @staticmethod
    def create_setting():
        record = json.loads(request.data)
        Setting_Create = Setting(**record)
        Setting_Create.save()
        return jsonify(Setting_Create.to_json())


    @staticmethod
    def update_setting(record):
        setting = Setting.objects(id=record['id']).first()
        if not setting:
            return jsonify({'error': 'data not found'})
        else:
            setting.update(
                liste_wifi=record['liste_wifi'],
                liste_manette=record['liste_manette'],
                authorization=record['authorization']
            )
        return jsonify(setting.to_json())




