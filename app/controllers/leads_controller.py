from flask import request, jsonify, current_app
from app.models.leads_model import LeadsModel
from http import HTTPStatus
import re
from app.exc.wrong_phone import WrongPhone
from app.services.data_processing import data_processing

def create_lead():
    data = request.get_json()
    data = data_processing(data)
    
    if not re.fullmatch("^\([1-9]{2}\)[0-9]{5}\-[0-9]{4}$",data["phone"]):
        error = WrongPhone(data)
        return jsonify(error.message), HTTPStatus.BAD_REQUEST

    for value in data.values():
        if type(value) != str:
            return {"error": f"{value} have to be string"}, HTTPStatus.BAD_REQUEST
        
    new_lead = LeadsModel(**data)

    current_app.db.session.add(new_lead)
    current_app.db.session.commit()

    return jsonify(new_lead), HTTPStatus.CREATED

    