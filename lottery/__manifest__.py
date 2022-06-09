# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Lottery',
    'version' : '1.1',
    'summary': 'Lottery',
    'sequence': 10,
    'description': """ Lottery
   """,
    'category': 'Lottery',
    'depends' : ['base', 'product','sales_team'],
    'data': [
        'security/lottery_security.xml',
        'security/ir.model.access.csv',
        'views/lottery_view.xml',
        'data/ir.sequence.data.xml',
           ],
    'demo': [
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
