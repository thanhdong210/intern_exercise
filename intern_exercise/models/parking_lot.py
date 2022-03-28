from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime

class ParkingLot(models.Model):
    _name = "parking.lot"
    _description = "Parking lot"
    _rec_name = 'parking_lot_name'

    parking_lot_name = fields.Char('Parking lot name', required=True)
    working_time_from = fields.Float("Working time from", required=True)
    working_time_to = fields.Float("Working time to", required=True)
    parking_vehicle_id = fields.Many2many("lot.vehicle.relation")
    parking_vehicle_ids = fields.Many2many('parking.vehicle', relation='lot_vehicle', column1='parking_lot_id', column2='parking_vehicle_id', string="Lot Vehicle")
    total_car_now = fields.Integer("Total car", compute='_compute_total_car')

    def open_car_park(self, context=None):
        field_ids = self.env['parking.lot'].search([('id','=',self.id)])
        domain = [('id', 'not in', [field_ids.id]), ('parking_lot_id.id', '=', self.id)]
        #view_id_tree = self.env['ir.ui.view'].search([('name','=',"parking.ticket.tree")])

        return {
            'name': self.parking_lot_name + "'s ticket",
            'context': {'default_parking_lot_id': self.id},
            'type': 'ir.actions.act_window',
            'res_model': 'parking.ticket',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'target': 'current',
            'domain': domain,
        }

    @api.depends("total_car_now")
    def _compute_total_car(self):
        for record in self:
            record.total_car_now = record.env['parking.ticket'].search_count([('parking_lot_id', '=', record.id)])

