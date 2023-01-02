from odoo import api, fields, models
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Estate Property Offer"
    _order = "price desc"
    _sql_contraints = [
            ("check_price", "CHECK(price > 0)", "The price must be strictly positive"),
        ]

    price = fields.Float(string="Price")
    status = fields.Selection(
            selection=[
                ("accepted", "Accepted"),
                ("refused", "Refused"),
                ],
            string="Status",
            copy=False,
            )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.date_deadline = date + relativedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.validity = (offer.date_deadline - date).days

    def action_accept(self):
        if "accepted" in self.mapped("property_id.offer_ids.status"):
            raise UserError("An offer as already been accepted.")
        self.write(
                {
                    "status": "accepted",
                }
            )
        return self.mapped("property_id").write(
                {
                    "state": "offer_accepted",
                    "selling_price": self.price,
                    "buyer_id": self.partner_id.id,
                }
            )

    def action_refuse(self):
        self.write(
                {
                    "status": "refused"
                }
            )
        if "accepted" not in self.mapped("property_id.offer_ids.status"):
            self.mapped("property_id").write(
                    {
                        "state": "new",
                        "selling_price": 0,
                        "buyer_id": None,
                    }
                )
