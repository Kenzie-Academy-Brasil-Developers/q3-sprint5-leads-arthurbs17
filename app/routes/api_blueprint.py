from flask import Blueprint

from app.routes.leads_blueprint import bp_leads

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")

bp_api.register_blueprint(bp_leads)