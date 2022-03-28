from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
import json
    
class LotVehicleRelaion(models.Model):
    _name = "lot.vehicle.relation"
    _description = "Lot vehicle relation"
    _rec_name = 'vehicle'
    
    lot = fields.Many2one('parking.lot', 'Parking lot', ondelete='cascade')
    """ vehicle_compute = fields.Char(compute="_compute_vehicle_chosen",
       readonly=True,
       store=False,) """
    vehicle = fields.Many2one('parking.vehicle', 'Parking vehicle', ondelete='cascade')
    quantity = fields.Integer('Quantity')

    """ @api.depends("vehicle")
    def _compute_vehicle_chosen(self):
        for record in self:
            record.product_id_domain = json.dumps(
               [('lot.parking_lot_name', 'not in', [record.lot]), ('vehicle.parking_vehicle_name', 'not in', [record.vehicle])]
           ) """
