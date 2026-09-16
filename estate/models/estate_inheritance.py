# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_agent = fields.Boolean(string='Is Real Estate Agent', default=False)
    agent_since = fields.Date(string='Agent Since')

class EstateProperty(models.Model):
    _name = 'estate.property'
    _inherit = ['estate.property', 'mail.thread']

    # Inheriting estate.property to support chatter messaging in Task C
    pass

class EstatePropertyOffer(models.Model):
    _inherit = 'estate.property.offer'

    @api.model_create_multi
    def create(vals_list):
        offers = super().create(vals_list)
        for offer in offers:
            prop = offer.property_id
            if prop and prop.expected_price:
                if offer.price < (prop.expected_price * 0.90):
                    prop.message_post(
                        body=f"Warning: An offer of {offer.price} was submitted, which is lower than 90% of the expected price ({prop.expected_price})."
                    )
        return offers

class EstatePropertyOfferHistory(models.Model):
    _name = 'estate.property.offer.history'
    _inherit = 'estate.property.offer'
    _description = 'Estate Property Offer History'

    archive_reason = fields.Char(string='Archive Reason')