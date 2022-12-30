{
    'name': "XM Module",
    'version': '1.0',
    'depends': [
        'base',
        'web',
    ],
    'author': "German",
    'category': 'Customs',
    'description': """
    This is the first module
    """,
    # data files always loaded at installation
    'data': [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_offer_views.xml",
        "views/estate_menus.xml",
    ],
    # data files containing optionally loaded demonstration data
    'demo': [],
    'application' : True,
}
