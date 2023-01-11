{
    'name': "Real Estate",
    'version': '16.0.0.0.1',
    'depends': [
        'base',
        'web',
    ],
    'license': 'LGPL-3',
    'author': "German, Vauxoo",
    'category': 'Real Estate/Brokerage',
    # data files always loaded at installation
    'data': [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/estate_property_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_offer_views.xml",
        "views/res_users_views.xml",
        "views/estate_menus.xml",
        "data/estate.property.type.csv",
        "report/estate_reports.xml",
        "report/estate_report_views.xml",
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        "demo/estate_property.xml",
        "demo/estate_offer.xml",
    ],
    'application' : True,
}
