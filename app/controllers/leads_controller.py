from flask import request, jsonify, current_app
from app.models.leads_model import LeadsModel
from http import HTTPStatus
import re
from app.exc.wrong_phone import WrongPhone
from app.services.data_processing import data_processing
from sqlalchemy.exc import IntegrityError
from app.exc.wrong_keys import WrongKeyReceived

keys_names = ["email", "name", "phone"]

def create_lead():
    data = request.get_json()
    
    try:
        data = data_processing(data)

        for key in keys_names:
            if type(data[key]) != str:
                return jsonify({"message": "Os valores devem ser passados em string"}), HTTPStatus.BAD_REQUEST

        if not re.fullmatch("^\([1-9]{2}\)[0-9]{5}\-[0-9]{4}$",data["phone"]):
            error = WrongPhone(data)
            return jsonify(error.message), HTTPStatus.BAD_REQUEST
        
        new_lead = LeadsModel(**data)

        current_app.db.session.add(new_lead)
        current_app.db.session.commit()

        return jsonify(new_lead), HTTPStatus.CREATED

    except IntegrityError:
        return jsonify({"message": "Email ou telefone já cadastrados!"}), HTTPStatus.UNPROCESSABLE_ENTITY
    
    except TypeError:
        error = WrongKeyReceived(data)
        return jsonify(error.message), HTTPStatus.BAD_REQUEST
    
    except KeyError:
        error = WrongKeyReceived(data)
        if len(error.wrong_key(data)) > 0:
            return jsonify(error.message), HTTPStatus.BAD_REQUEST
        return jsonify(error.miss_keys), HTTPStatus.BAD_REQUEST