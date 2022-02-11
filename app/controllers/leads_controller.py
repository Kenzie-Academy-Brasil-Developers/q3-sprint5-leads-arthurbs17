from flask import request, jsonify, current_app
from app.models.leads_model import LeadsModel
from http import HTTPStatus
import re
from app.exc.wrong_phone import WrongPhone
from app.services.data_processing import data_processing
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from app.exc.wrong_keys import WrongKeyReceived
from datetime import datetime

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

def get_leads():
    
    leads_list = current_app.db.session.query(LeadsModel).order_by(LeadsModel.visits.desc()).all()

    if not leads_list:
        return jsonify({"message": "Nenhum dado inserido ainda!"}), HTTPStatus.OK

    return jsonify(leads_list), HTTPStatus.OK

def update_lead():
    try:
        data = request.get_json()
        data_key = data.keys()

        if list(data_key)[0] != 'email' or len(list(data_key)) > 1:
            error = WrongKeyReceived(data)
            return jsonify(error.only_email_message), HTTPStatus.BAD_REQUEST
            
        lead = LeadsModel.query.filter_by(email=data["email"]).one()
        att_status = {"visits": lead.visits +1, "last_visit" : datetime.now()}

        for key, value in att_status.items():
            setattr(lead, key, value)
            
        current_app.db.session.add(lead)
        current_app.db.session.commit()

        return jsonify("Updated"), HTTPStatus.OK
    
    except NoResultFound:
        return jsonify({"message": "Dado não encontrado no banco"}), HTTPStatus.NOT_FOUND