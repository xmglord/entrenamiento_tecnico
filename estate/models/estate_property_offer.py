from odoo import api, fields, models, _
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"
    _order = "price desc"
    _sql_contraints = [
        ("check_price", "CHECK(price > 0)", "The price must be strictly positive"),
    ]

    price = fields.Float()
    status = fields.Selection(
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        copy=False,
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    property_type_id = fields.Many2one("estate.property.type", related="property_id.property_type_id",
                                       string="Property Type", store=True)

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
            raise UserError(_("An offer as already been accepted."))
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

    @api.model
    def create(self, vals):
        prop = self.env["estate.property"]
        if vals.get("property_id"):
            prop = prop.browse(vals["property_id"])
            if prop.state == 'sold':
                raise UserError(_("You cannot make an offer on a sold property"))
        if prop and vals.get("price"):
            proper = self.env["estate.property"].browse(vals["property_id"])
            if proper.offer_ids:
                max_offer = proper.best_price
                if fields.float_compare(vals["price"], max_offer, precision_rounding=0.01) <= 0:
                    raise UserError(_("The offer must be higher than %.2f"), max_offer)
            proper.state = "offer_received"
        return super().create(vals)
