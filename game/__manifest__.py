# -*- coding: utf-8 -*-
{
    'name': "game",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ivan",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/game_player.xml',
        'views/game_building_types.xml',
        'views/game_building.xml',
        'views/game_battle.xml',
        'demo/game_data_demo.xml',
        'views/game_building_summary.xml',
        'data/cron_game.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/game_data_demo.xml',
    ],
    'installable': True,
    'application': True,
}
