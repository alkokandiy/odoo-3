from odoo import models, fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'Talaba'

    name = fields.Char(string='F.I.Sh.', required=True)
    age = fields.Integer(string='Yosh')
    phone = fields.Char(string='Telefon')
