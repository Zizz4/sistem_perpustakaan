from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_penerbit = fields.Boolean(string='Penerbit')
    buku_terbitan_ids = fields.One2many(comodel_name='perpustakaan.buku', inverse_name='penerbit_id', string="Buku Terbitan")
