# -*- coding: utf-8 -*-
{
    'name': 'ov_wine',
    'installable': True,
    'summary': 'wine database',
    'description': """
ov-wine - wine-database
=======================
This addon extends the product-structure with specific wine-attributes. 
    """,
    'author': 'Ovento GmbH',
    'website': 'http://www.ovento.ch',
    
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'product', 'account', 'web','website','web_enterprise','website_sale','stock'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/ov_view.xml',
        'views/snippets.xml',
        'views/s_ov_wine_attributes.xml',
        'menus/ov_menu.xml',
        'data/data.xml',
        'report/template_mod.xml',
        'report/mv_rechnung.xml',
        'report/mv_auftrag.xml',
        'report/address_template_mod.xml',
        'report/swk_report.xml',
        'report/ov_winelist.xml',
        'report/ov_winelist_template.xml',
        'report/ov_winesheet_template.xml',
        'report/swk_report_detail.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
}
