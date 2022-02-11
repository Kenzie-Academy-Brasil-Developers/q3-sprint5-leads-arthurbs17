from flask import Blueprint

from app.controllers import leads_controller

bp_leads = Blueprint("bp_leads", __name__, url_prefix="/leads")

bp_leads.post("")(leads_controller.create_lead)
bp_leads.get("")(leads_controller.get_leads)
bp_leads.patch("")(leads_controller.update_lead)