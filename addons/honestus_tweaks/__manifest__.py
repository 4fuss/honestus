{
    'name': "Honestus dev assignment",
    'version': '16.0.1.0.0',
    'depends': [
        'base',
        'auth_signup',
        'sale',
        'website'
    ],
    'author': "Adam Kawczyński",
    'category': 'Website',
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'report/sale_report_views.xml',
        'views/templates.xml',
        'views/sale_views.xml',
        'views/sale_order_report_template.xml',
    ],
}
