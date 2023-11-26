from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_penulis = fields.Boolean(string='Penulis')
    buku_tulisan_ids = fields.One2many(comodel_name='perpustakaan.buku', inverse_name='penulis_id', string="Buku Tulisan")

    @api.onchange('company_type')
    def _onchange_company_type(self):
        for rec in self:
            if rec.company_type == 'company':
                rec.is_penulis = False
