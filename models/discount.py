# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple


class VolumeDiscount(models.Model):
    _name = 'budget.contractor.discount'
    _description = 'Volume Discount'
    _order = 'threshold desc'

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------
    threshold = fields.Monetary(string='Threshold', currency_field='currency_id')
    sequence = fields.Integer(string='Sequence')
    discount_percentage = fields.Float(string='Discount Percent (%)', digits=(5, 2))
    is_default = fields.Boolean(string='Is Default')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    currency_id = fields.Many2one('res.currency', readonly=True,
                                          default=lambda self: self.env.user.company_id.currency_id)
    contract_id = fields.Many2one('budget.contractor.contract', string='Contract')
    discount_rule_id = fields.Many2one('budget.contractor.discount.rule', string='Discount Rule')

    # COMPUTE FIELDS
    # ----------------------------------------------------------

    # CONSTRAINS FIELDS
    # ----------------------------------------------------------

    # BUTTON ACTIONS / TRANSITIONS
    # ----------------------------------------------------------
