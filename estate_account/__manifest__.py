{
    'name': "Real Estate Accounting",
    'version': '1.0',
    'depends': [
        'estate',
        'account',
    ],
    'author': "German",
    'category': 'Customs',
    'description': """
    This is the second module
    """,
    # data files always loaded at installation
    'data': [
        "report/estate_reports.xml",
    ],
    # data files containing optionally loaded demonstration data
    'demo': [],
    'application' : True,
}
