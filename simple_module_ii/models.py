# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Student(models.Model):
    _name = "simple_module_ii.student"
    name = fields.Char(string='姓名', default='请填写姓名')
    stu_no = fields.Char(string='学号', default='请填写学号')