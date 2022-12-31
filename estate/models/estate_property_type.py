from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _sql_constraints = [
            ("check_name", "UNIQUE(name)", "The name must be unique"),
        ]

    name = fields.Char("Name", required=True)
