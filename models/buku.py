from odoo import fields, models, api, _
from odoo.exceptions import UserError


class PerpustakaanBuku(models.Model):
    _name = 'perpustakaan.buku'

    code = fields.Char(string='No Inventaris', copy=False, readonly=False, index=True,
                       default=lambda self: _('New'))
    name = fields.Char('Judul Buku', required=True)
    penulis_id = fields.Many2one(string='Penulis', comodel_name='res.partner', domain=[('is_penulis', '=', True)])
    penerbit_id = fields.Many2one(string='Penerbit', comodel_name='res.partner', domain=[('is_penerbit', '=', True)])
    isbn = fields.Char('ISBN', size=13)
    tahun_terbit = fields.Char('Tahun Terbit', size=4)
    kategori = fields.Selection([
        ('fiksi', 'Fiksi'),
        ('non-fiksi', 'Non-Fiksi')
    ], 'Kategori', default='fiksi')
    halaman = fields.Integer('Jumlah Halaman')

    @api.model
    def create(self, vals_list):
        if vals_list.get('code', 'New') == 'New':
            vals_list['code'] = self.env['ir.sequence'].next_by_code('perpustakaan.buku.seq') or 'New'
            result = super(PerpustakaanBuku, self).create(vals_list)
            return result
