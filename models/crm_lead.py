from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = "crm.lead"

    crm_checklist_ids = fields.Many2many("crm.checklist")
    checkbox_progress = fields.Integer(compute="_compute_checkbox_progress")

    @api.depends("crm_checklist_ids")
    def _compute_checkbox_progress(self):
        for rec in self:
            if rec.crm_checklist_ids:
                checkbox_true = len(rec.crm_checklist_ids.filtered(lambda l: l.checkbox))
                checkbox_all = len(rec.crm_checklist_ids)
                rec.checkbox_progress = checkbox_true * 100 / checkbox_all
            else:
                rec.checkbox_progress = 0
