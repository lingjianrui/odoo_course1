# -*- coding: utf-8 -*-
from odoo import api, fields, models


class StudentExt(models.Model):
    _inherit = "simple_module_ii.student"
    test = fields.Char(string='iii继承')