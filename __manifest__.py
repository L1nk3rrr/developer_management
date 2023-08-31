# -*- coding: utf-8 -*-

{
    'name': 'Developers Management',
    'version': '16.0.0.0.0',
    'summary': 'Module for Managing Developers',
    'description': '''
The "Developers Management" module is designed to streamline the process of managing developers within 
the Odoo 16 Community platform. 
With this module, you can easily organize and keep track of your team of developers, 
each with their specific information and roles. 
The module offers an intuitive interface for adding, editing, and viewing developer profiles, 
enhancing your ability to manage and collaborate effectively.
     ''',

    'author': 'Valentyn Starushok',
    'website': 'https://github.com/L1nk3rrr',
    'license': 'GPL-3',

    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/developer.xml',
        'views/company.xml',
        'views/menu.xml',
    ],
    'test': [
        'tests/test_developers_management.py',
    ],
}
