{
    'name':'ht_gym_mgnt',
    'version':'14.0.0.1.0',
    'summary':'Gym activities',
    'description':'''Customer can take a membership of the gym. also, specify the purpose and if they need any coach for that than we can provide coach to them.''',
    'Author':'Ruchita Sapariya',
    'website':'http.google.com',
    'depends':['contacts'],
    'data':[
        'security/ir.model.access.csv',
        'views/gym_membership_views.xml',
        'views/customer_booking_views.xml',
        'views/inherit_partner_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}

