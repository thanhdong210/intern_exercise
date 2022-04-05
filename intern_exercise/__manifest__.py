{
    'name': "Parking manage",
    'summary': "Parking manage",
    'description': "Manage car parking in parking lot",
    'author': "Thanh Dong",
    'website': "None",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/parking_lot.xml',
        'views/parking_vehicle.xml',
        'views/lot_vehicle_relation.xml',
        'views/parking_ticket.xml',
        'views/parking_pricelist.xml',
        'views/parking_pricelist_item.xml',
        'views/check_out_action_popup.xml',

        'report/reports.xml',
        'report/total_car_now.xml',
        'report/parking_ticket_report.xml'
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}