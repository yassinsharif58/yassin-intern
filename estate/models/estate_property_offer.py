from odoo import models, fields, api

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    _order = "price desc"

    price = fields.Float(required=True)
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], copy=False, default=False)
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True, onDelete="cascade")

    def write(self, vals):
        if 'status' in vals:
            for offer in self:
                if vals['status'] == 'accepted':
                    if offer.property_id.state == 'offer_accepted':
                        raise models.ValidationError("An offer has already been accepted for this property.")
                    offer.property_id.selling_price = offer.price
                    offer.property_id.buyer_id = offer.partner_id
                    offer.property_id.state = 'offer_accepted'
        return super().write(vals)