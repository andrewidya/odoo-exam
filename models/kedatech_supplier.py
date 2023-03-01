from odoo import api, fields, models


class Supplier(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    supplier_rank = fields.Integer(default=1)
    customer_rank = fields.Integer(default=0)

    @api.model
    def create(self, vals_list):
        if isinstance(vals_list, dict):
            vals_list = [vals_list]

        for value in vals_list:
            value['supplier_rank'] = 1
            value['customer_rank'] = 0

        return super().create(vals_list)
