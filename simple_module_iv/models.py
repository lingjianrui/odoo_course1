# -*- coding: utf-8 -*-
from odoo import api, fields, models


class StudentExt(models.Model):
    _inherit = "simple_module_ii.student"
    state = fields.Char(string='iv继承')

    @api.multi
    def action_publish(self):
        self.write({
            'state': 'published'
        })
        return {}