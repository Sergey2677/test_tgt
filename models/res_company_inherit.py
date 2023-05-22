# -*- coding: utf-8 -*-

from odoo import models, fields


class CompanyInherit(models.Model):
    _inherit = "res.company"

    accountant_user_id = fields.Many2one('res.users')

    def write(self, vals):
        res = super(CompanyInherit, self).write(vals)
        accountant_user_id = vals.get('accountant_user_id')
        if accountant_user_id:
            self.subscribe_accountant_triggered_by_accountant_user_id(accountant_user_id)
        return res

    def subscribe_accountant_triggered_by_accountant_user_id(self, accountant_user_id):
        for record in self:
            record_set = record.env['hr.expense.sheet'].search([('state', '=', 'submit')])
            record_accountant_user_id = record.env['res.users'].browse(accountant_user_id)
            record_set.message_subscribe(partner_ids=[record_accountant_user_id.partner_id.id])
