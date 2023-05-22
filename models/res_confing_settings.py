# -*- coding: utf-8 -*-

from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    hr_expense = fields.Many2one('hr.expense')
    accountant_user_id = fields.Many2one('res.users', related='company_id.accountant_user_id', readonly=False)
