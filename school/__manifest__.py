# -*- coding: utf-8 -*-
{
    'name': "school",
    'sequence': 100,
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
    Value add student
        
        """,

    'description': """
       school students
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/colossal/colossal/blob/13.0/colossal/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base_setup'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/student_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': [],
	
    'license': 'AGPL-3',
        
    'installable': True,
        
    'application': True,
        
    'auto_install': False,
}
