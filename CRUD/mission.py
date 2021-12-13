import json

from flask import jsonify
from MODEL.mission import Mission

class CrudMission:

    @staticmethod
    def get_all_mission():
        missions = Mission.objects()
        return [Mission.to_json() for Mission in missions]

    @staticmethod
    def get_mission_by_id(id_mission):

        mission = Mission.objects(id_mission=id_mission).first()
        if mission is None:
            return jsonify({"error": "not found"})
        else:
          return mission.to_json()

    @staticmethod
    def delete_by_id(id_mission):
        mission = Mission.objects(id_mission=id_mission).first()
        if not mission:
            return jsonify({'error': 'data not found'})
        else:
            mission.delete()
        return jsonify(mission.to_json())

    @staticmethod
    def create_mission(record):
        mission = Mission(**record)
        mission.save()
        return jsonify(mission.to_json())


