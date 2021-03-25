# -*- coding: utf-8 -*-

from colossal import models, fields, api


class school(models.Model):
    _name = 'school.school'
    _description = 'school.school'

    name = fields.Char()
    max_students = fields.Integer()
    passrate = fields.Float(compute="_passrate_pc", store=True)
    description = fields.Text()

    @api.depends('passrate')
    def _passrate_pc(self):
        for record in self:
            record.passrate = float(record.passrate) / 100

class student(models.Model):
    _name = 'student.student'

    name =  fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    photo = fields.Binary(string='Image')
    gender = fields.Selection([('male','Male'), ('female', 'Female'),('others', 'Others')],
                                string='Gender')
    student_dob = fields.Date(string='Date of Birth')
    student_blood_group = fields.Selection(
    	[('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
     	('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
    	string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')