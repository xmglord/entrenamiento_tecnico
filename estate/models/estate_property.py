from odoo import api, fields, models

#We use the date util as said in odoo documentation
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This is a Estate Property"

    name = fields.Char(required = True)
    description = fields.Text()
    postcode = fields.Char()
    #Functioncontext_today is recommended for default values
    date_availability = fields.Date("Available nearest date", default = lambda self: fields.Date.context_today(self)\
            + relativedelta(months=3), copy= False)
    expected_price = fields.Float(required = True)
    selling_price = fields.Float(readonly = True, copy = False)
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection=[('north', 'North'),\
            ('south', 'South'), ('east', 'East'), ('west', 'West')])
    active = fields.Boolean("Active", default=True)
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        required=True,
        copy=False,
        default="new",
    )
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    user_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    total_area = fields.Integer(string="Total Area (sqm)", compute="_compute_total_area")
    best_price = fields.Float(string="Best Offer", compute="_compute_best_price")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for proper in self:
            proper.total_area = proper.living_area + proper.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for proper in self:
            proper.best_price = max(proper.offer_ids.mapped("price")) if proper.offer_ids else 0.0
