{
    'name': 'Add Custom Field in Sales',
    'version': '1.0',
    'summary': 'Adds a custom field to the Sales Order form after the date_order field.',
    'description': 'This module adds a custom field after the date_order field in the Sales Order form.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
