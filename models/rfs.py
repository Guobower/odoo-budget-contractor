# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ReadyForService(models.Model):
    _name = 'budget.contractor.rfs'
    _rec_name = 'reference_no'
    _description = 'Ready For Service'

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------
    reference_no = fields.Char(string='Reference No')
    date = fields.Date(string='Date')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    contract_id = fields.Many2one('budget.contractor.contract', string='Contract')

    # COMPUTE FIELDS
    # ----------------------------------------------------------

    # CONSTRAINS FIELDS
    # ----------------------------------------------------------

    # BUTTON ACTIONS / TRANSITIONS
    # ----------------------------------------------------------
