{
    'name': 'Custom Contact MOdule',
    'version': '1.0',
    'category': 'Contact',
    'summary': 'Replicates the cashflow forecast screen similar to Sage X3 with search and MRA reprocess functionality.',
    'description': """
        This module provides a cashflow forecast screen that allows users to filter invoices by date, customer, 
        invoice status, and other criteria. Users can also select multiple invoices and reprocess them to MRA.
    """,
    'author': 'Greytrix Business Solution',
    'website': 'https://yourwebsite.com',
    'depends': ['base', 'contacts'],
    'data': [
        'views/res_parnter_views.xml',
        # 'views/cashflow_forecast_line_tree_view.xml',
        # 'views/cashflow_forecast_search_view.xml',
        # 'views/cashflow_forecast_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}