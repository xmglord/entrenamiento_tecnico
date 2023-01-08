from odoo import models, Command
from odoo.exceptions import UserError

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        res = super().action_sold()
        self.check_access_rights('write')
        self.check_access_rule('write')
        print(" reached ".center(100, '='))
        for prop in self:
            self.env["account.move"].sudo().create(
                {
                    "partner_id": prop.buyer_id.id,
                    "move_type": "out_invoice",
                    "invoice_line_ids": [
                        Command.create({
                            "name": prop.name,
                            "quantity": 1.0,
                            "price_unit": prop.selling_price * 6.0 / 100.0,
                        }),
                        Command.create({
                            "name": "Administrative fees",
                            "quantity": 1.0,
                            "price_unit": 100.0,
                        }),
                    ],
                }
            )
        return res
