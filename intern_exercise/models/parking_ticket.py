from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
from datetime import timedelta
import random
import string

class ParkingTicket(models.Model):
    _name = "parking.ticket"
    _description = "Parking ticket"
    _rec_name = 'parking_ticket_name'

    parking_ticket_name = fields.Char('Car name', required=True)
    parking_lot_id = fields.Many2one('parking.lot', required=True)
    car_image = fields.Binary("Car Image", attachment=True, help="Car Image")
    car_type = fields.Many2one("lot.vehicle.relation", required=True, domain="[('lot', 'in', [parking_lot_id])]")
    check_in = fields.Datetime("Check in", required=True)
    check_out = fields.Datetime("Checkout")
    total_time = fields.Char("Total time")
    code = fields.Char("Code", required=True, compute="_generate_code")

    def create_ref_code():
        date = fields.Date(string='Date', default=datetime.today())
        return ''.join(random.choices(str(date) + string.digits, k = 15))

    @api.depends("parking_ticket_name")
    def _generate_code(self):
        for record in self:
            code = record.create_ref_code
            record.code = code

    @api.onchange('check_in', 'check_out')
    def calculate_hours_saving(self):
        for record in self:
            if record.check_in and record.check_out:
                d1 = datetime.strptime(str(record.check_in),'%Y-%m-%d %H:%M:%S') 
                d2 = datetime.strptime(str(record.check_out),'%Y-%m-%d %H:%M:%S')       
                d3 = d2 - d1
                delta = d3 / timedelta(hours=1)
                record.total_time = str(str(round(delta, 0)) + " hours")

    

    


    


