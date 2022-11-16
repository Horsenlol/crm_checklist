from odoo import models, fields


class CrmChecklist(models.Model):
    _name = "crm.checklist"

    name = fields.Char()
    checkbox = fields.Boolean()
