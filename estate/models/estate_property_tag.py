from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Tag'
    _order = 'name'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color Index')

    _sql_constraints = [
        ('check_name_uniq', 'unique(name)', 'The tag name must be unique!')
    ]