# -*- coding: utf-8 -*-
# from colossal import http


# class LoanPrediction(http.Controller):
#     @http.route('/loan_prediction/loan_prediction/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loan_prediction/loan_prediction/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('loan_prediction.listing', {
#             'root': '/loan_prediction/loan_prediction',
#             'objects': http.request.env['loan_prediction.loan_prediction'].search([]),
#         })

#     @http.route('/loan_prediction/loan_prediction/objects/<model("loan_prediction.loan_prediction"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loan_prediction.object', {
#             'object': obj
#         })
