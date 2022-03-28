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
        'views/parking_ticket.xml'
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}