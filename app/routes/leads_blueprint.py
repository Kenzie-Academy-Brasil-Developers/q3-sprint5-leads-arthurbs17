from flask import Blueprint

from app.controllers import leads_controller

bp_leads = Blueprint("bp_leads", __name__, url_prefix="/leads")

bp_leads.post("")(leads_controller.create_lead)