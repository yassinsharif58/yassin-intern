{
    'name': 'Real Estate',
    'version': '18.0.1.0.0',
    'category': 'Real Estate',
    'summary': 'Manage real estate properties and advertisements',
    'depends': ['base', 'mail'],
    'data': [
                'security/ir.model.access.csv',
                'views/estate_property_views.xml',
'views/estate_property_type_views.xml',
'views/estate_property_tag_views.xml',
'views/estate_property_inherit_views.xml',
],
    'installable': True,
    'license': 'LGPL-3',
}