from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Material(models.Model):
    _name = "kedatech.material"
    _description = "KedaTech Exam's Material"

    code = fields.Char(string="CODE", required=True)
    name = fields.Char(string="Name", required=True)
    material_type = fields.Selection(
        string="Type",
        selection=[
            ("fabric", "Fabric"),
            ("jeans", "Jeans"),
            ("cotton", "Cotton")
        ],
        required=True
    )
    buy_price = fields.Float(string="Buy Price", required=True)
    supplier = fields.Many2one(
        comodel_name="res.partner",
        string="Supplier",
        domain=[("supplier_rank", "=", 1)],
        required=True
    )

    @api.constrains("buy_price")
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError("Buy price cannot be less than 100")
