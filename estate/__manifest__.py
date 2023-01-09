{
    'name': "Real Estate",
    'version': '1.0',
    'depends': [
        'base',
        'web',
    ],
    'author': "German",
    'category': 'Real Estate/Brokerage',
    'description': """
    This is the first module
    """,
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
