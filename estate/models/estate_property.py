from odoo import fields, models

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
