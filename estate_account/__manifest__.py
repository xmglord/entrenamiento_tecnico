{
    'name': "Real Estate Accounting",
    'version': '16.0.0.0.1',
    'depends': [
        'estate',
        'account',
    ],
    'license': 'LGPL-3',
    'author': "German, Vauxoo",
    'category': 'Customs',
    # data files always loaded at installation
    'data': [
        "report/estate_reports.xml",
    ],
    # data files containing optionally loaded demonstration data
    'demo': [],
    'application' : True,
}
