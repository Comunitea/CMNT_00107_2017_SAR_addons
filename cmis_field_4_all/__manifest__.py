# -*- coding: utf-8 -*-
{
    'name': "cmis_field_4_all",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['cmis_field', 'cmis_web'],
    'post_init_hook': 'post_init_check',

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
}