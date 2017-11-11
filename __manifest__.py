# -*- coding: utf-8 -*-
{
    'name': "karma_wlr",

    'summary': """
        Manage the progress of Wholesale Line Rental (WLR) Orders.""",

    'description': """
        Manage the progress of Wholesale Line Rental (WLR) Orders.
    """,

    'author': "Karma Computing Ltd",
    'website': "http://karmacomputing.co.uk",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'crm', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/example_webpage.xml',
        'views/detail_page.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
