# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError
import re
import logging

class Lottery(models.Model):
    _name = "lottery"
    _description = "Lottery"
    @api.model
    def _default_user(self):
        return self.env.user.id

    
    name = fields.Char(string='Sequence', required=True, translate=True,default="New")
    user_id = fields.Many2one('res.users',default=_default_user,required=True)
    company_id = fields.Many2one('res.company')
    draw_number = fields.Char(string='Draw Number',default="000",required=True)
    state = fields.Selection([
        ('draft', 'New'),
        ('confirm', 'Confirm'),
        ('pending', 'Locked'),
        ('done', 'Draw Completed'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    @api.model
    def create(self, vals):
        if 'company_id' in vals:
            self = self.with_company(vals['company_id'])
        result = super(Lottery, self).create(vals)
        if vals.get('name', _('New')) == _('New'):
            # ~ seq_date = None
            # ~ if 'date_order' in vals:
                # ~ seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
            vals['name'] = self.env['ir.sequence'].next_by_code('lottery') or _('New')
        # ~ if re.match("^[0-9]\d{3}$", vals.get('draw_number')) != None:
            # ~ raise UserError(_('Enter three digit number'))
        _logger = logging.getLogger(__name__)
        _logger.exception('In the Log file to view the  %s', vals)
        return result

    def write(self, vals):
        # Do not allow changing the company_id when account_move_line already exist
        if vals.get('company_id', False):
            raise UserError(_('You cannot change the company '))
        return super(Lottery, self).write(vals)

    def action_confirm(self):
        self.write({'state':'confirm'})

   
