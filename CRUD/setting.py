import json

from flask import jsonify, request

from config import db
from MODEL.setting import Setting

class CrudSetting:

    @staticmethod
    def get_all_setting():
        settings = Setting.objects()
        print(settings[0].to_json())
        return [Setting.to_json() for Setting in settings]

    @staticmethod
    def get_setting_by_people_is(people_id):
        Setting_get= Setting.objects(id_people=people_id).first()
        print(Setting_get)
        if Setting_get is None:
            return {
                "message": "not found",
                "status":404
            }
        else:
            return Setting_get.to_json()

    @staticmethod
    def delete_setting_by_id(people_id):
        Setting_get= Setting.objects(id_people=people_id).first()
        if Setting_get is None:
            return jsonify({'error': 'data not found'})
        else:
            Setting_get.delete()
            return jsonify({'message': 'succesful'})

    @staticmethod
    def create_setting(record):
        Setting_Create = Setting(**record)
        Setting_Create.save()
        return jsonify(Setting_Create.to_json())


    @staticmethod
    def update_setting(record):
        setting = Setting.objects(id_people=record['id_people']).first()
        if not setting:
            return jsonify({'error': 'data not found'})
        else:
            setting.update(
                liste_wifi=record['liste_wifi'],
                manette_list=record['manette_list'],
                authorization=record['authorization']
            )
            return jsonify(setting.to_json())




