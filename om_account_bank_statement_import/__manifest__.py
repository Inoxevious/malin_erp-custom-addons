# -*- encoding: utf-8 -*-

{
    'name': 'Colossal 14 Account Bank Statement Import',
    'version': '14.0.1.2.0',
    'category': 'Accounting',
    'depends': ['account'],
    'website': 'https://www.colossalmates.tech',
    'author': 'Colossal Mates, Colossal SA',
    'support': 'colossalmates@gmail.com',
    'maintainer': 'Colossal Mates',
    'license': 'LGPL-3',
    'description': """Generic Wizard to Import Bank Statements In Colossal14 Community Edition.
(This module does not include any type of import format.)
OFX and QIF imports are available in Enterprise version.""",
    'data': [
        'security/ir.model.access.csv',
        'account_bank_statement_import_view.xml',
        'account_import_tip_data.xml',
        'wizard/journal_creation.xml',
        'views/account_bank_statement_import_templates.xml',
    ],
    'demo': [
        'demo/partner_bank.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': True,
}
