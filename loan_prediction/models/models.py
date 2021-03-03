# -*- coding: utf-8 -*-

from odoo import models, fields, api


class loan_prediction(models.Model):
    _name = 'loan_prediction.loan_prediction'
    _description = 'loan_prediction.loan_prediction'

    name = fields.Char()
    amount = fields.Float()
    score = fields.Float(compute="_prediction_score", store=True)
    description = fields.Text()

    @api.depends('amount')
    def _prediction_score(self):
        for record in self:
            record.score = float(record.amount) / 100


class Loan(models.Model):
    _name = 'loan.loan'

    loan_id = fields.Char(string="Loan ID", required=True)
    loan_officer = fields.Char(string="Loan Officer", required=True)
    age = fields.Integer()  	
    ed = fields.Integer()  
    employ = fields.Integer()  
    address = fields.Integer()  
    income = fields.Integer()  
    debtinc = fields.Float() 
    creddebt = fields.Float() 
    othdebt = fields.Float() 
