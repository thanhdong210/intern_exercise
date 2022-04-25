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
    parking_lot_id_relate = fields.Integer(related='parking_lot_id.id')
    car_image = fields.Binary("Car Image", attachment=True, help="Car Image")
    car_type_id = fields.Many2one("lot.vehicle.relation", required=True, domain="[('lot.id', 'in', [parking_lot_id])]")
    car_type_id_relate = fields.Integer(related='car_type_id.vehicle.id')
    check_in = fields.Datetime("Check in", required=True)
    check_out = fields.Datetime("Checkout")
    total_time = fields.Char("Total time")
    code = fields.Char("Code", readonly=True)
    price = fields.Float("Price")
    state = fields.Selection([
        ('checked_out', "Checked out"),
        ('staying_in', "Staying in")
    ], default='staying_in')
    """ car_price_id = fields.Many2one("parking.pricelist", domain="[('car_type.id', '=', car_type_id_relate)]")
    car_price_id_price = fields.Float(related='car_price_id.price')
    check_car_type = fields.Boolean()
    
    #, compute="_compute_price"
    #, domain="[('car_type', 'in', [car_type_id])]" """



    def action_check_out(self):  
        #hour   
        print(self.car_type_id_relate)
        self.check_out = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        d1 = datetime.strptime(str(self.check_in),'%Y-%m-%d %H:%M:%S') 
        d2 = datetime.strptime(str(self.check_out),'%Y-%m-%d %H:%M:%S')       
        d3 = d2 - d1
        delta = d3 / timedelta(hours=1)      
        delta2 = str(round(delta, 0))

        #price
        global price1
        price1 = 0
        for record in self:
            line = self.env['parking.pricelist.item'].search([('car_type_id.id', '=', record.car_type_id_relate), ('parking_pricelist_id.id', '=', record.parking_lot_id.pricelist_id.id)])
            #print(line)
            #price1 = 0
            for row in line:
                if float(record.total_time) >= row.from_hour and float(record.total_time) <= row.to_hour:                    
                    price1 = row.price
                self.write(vals={'total_time': delta2, 'price': price1, 'state': 'checked_out'})

        return {
            'name': "Checkout",
            'context': {'default_price': self.price, 'default_total_time': self.total_time},
            'type': 'ir.actions.act_window',
            'res_model': 'checkout.action',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'views': [(False, 'form')],
        }

    @api.model
    def create(self, vals): 
        vals['code'] = self.create_ref_code()
        return super().create(vals)
         # ir.sequence

    # def write(self, vals): update table set a =1 b=2 where id in self.ids

    def create_ref_code(self):
        now= datetime.strftime(fields.Datetime.context_timestamp(self, datetime.now()), "%Y-%m-%d %H:%M:%S")
        #print(date)
        now2 = now.split("-")
        now3 = ""
        for l in now2:
            now3 += l
        now4 = now3[:10]
        random1 = ''.join(random.choices(string.digits, k = 7))
        code = now4 + str(random1)
        return code

    # @api.onchange("car_type_id")
    # def _readonly_car_price(self):
    #     for record in self:
    #         record.check_car_type = True

    #         if record.car_type_id:
    #             record.check_car_type = True
    #         else:
    #             record.check_car_type = False

    # @api.depends("parking_ticket_name")
    # def _generate_code(self):
    #     for record in self:
    #         code = record.create_ref_code()
    #         record.code = code

    # @api.onchange('check_in')
    # def calculate_hours_saving(self):
    #     for record in self:
    #         if record.check_in and record.check_out:
    #             d1 = datetime.strptime(str(record.check_in),'%Y-%m-%d %H:%M:%S') 
    #             d2 = datetime.strptime(str(record.check_out),'%Y-%m-%d %H:%M:%S')       
    #             d3 = d2 - d1
    #             delta = d3 / timedelta(hours=1)
    #             record.total_time = str(str(round(delta, 0)))
    #             print(delta)

    # @api.onchange('total_time')
    # def _compute_price(self):
    #     for record in self:
    #         line = self.env['parking.pricelist.item'].search([('car_type_id.id', '=', record.car_type_id_relate), ('parking_pricelist_id.id', '=', record.parking_lot_id.pricelist_id.id)])
    #         print(line)
    #         for row in line:
    #             if float(record.total_time) > row.from_hour and float(record.total_time) < row.to_hour:
    #                 record.price = row.price

    
    



    

    


    


