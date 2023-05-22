# -*- coding: utf-8 -*-
import datetime

from odoo import models


class HrExpenseSheetInherit(models.Model):
    _inherit = 'hr.expense.sheet'

    def approve_expense_sheets(self):
        super(HrExpenseSheetInherit, self).approve_expense_sheets()
        self.notify_user_when_approved()
        self.set_approval_date()

    def set_approval_date(self):
        for record in self:
            record.approval_date = datetime.datetime.now()

    def action_submit_sheet(self):
        super(HrExpenseSheetInherit, self).action_submit_sheet()
        self.subscribe_accountant_triggered_by_state()

    def subscribe_accountant_triggered_by_state(self):
        for record in self:
            if record and record.company_id.accountant_user_id:
                record.message_subscribe(partner_ids=[record.company_id.accountant_user_id.partner_id.id])

    def notify_user_when_approved(self):
        for record in self:
            if record and record.company_id.accountant_user_id:
                notification_ids = [(0, 0, {
                    'res_partner_id': record.company_id.accountant_user_id.partner_id.id,
                    'notification_type': 'inbox'
                })]

                self.env['mail.message'].create({
                    'message_type': "notification",
                    'body': "Expense Report approved by manager",
                    'subject': "Notify",
                    'partner_ids': [(4, record.company_id.accountant_user_id.partner_id.id)],
                    'model': self._name,
                    'res_id': self.id,
                    'notification_ids': notification_ids,
                    'author_id': self.env.user.partner_id and self.env.user.partner_id.id
                })
