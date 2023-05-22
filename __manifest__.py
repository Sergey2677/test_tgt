# -*- coding: utf-8 -*-
{
    'name': "Test task (TGT)",
    'summary': """Tesk task for TGT""",
    'description': """Tesk task for TGT""",
    'author': "Sergey Zheleznyakov",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'hr_expense'],
    'data': [
        'views/hr_expense_res_config_settings_view_form_inherit.xml',
        'views/hr_expense_view_hr_expense_sheet_form_inherit.xml',
        'views/report_expense_sheet_inherit.xml',
    ],
}
