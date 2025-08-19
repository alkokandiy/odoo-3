# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleThree(http.Controller):
#     @http.route('/module_three/module_three', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_three/module_three/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_three.listing', {
#             'root': '/module_three/module_three',
#             'objects': http.request.env['module_three.module_three'].search([]),
#         })

#     @http.route('/module_three/module_three/objects/<model("module_three.module_three"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_three.object', {
#             'object': obj
#         })

