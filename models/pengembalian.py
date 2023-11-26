from odoo import fields, models, api, _


class PerpustakaanPengembalian(models.Model):
    _name = 'perpustakaan.pengembalian'

    name = fields.Char(string='Pinjaman', copy=False, readonly=False, index=True,
                       default=lambda self: _('New'))
    pinjam_id = fields.Many2one(string='Dokumen Pinjam', required=True, comodel_name='perpustakaan.peminjaman',
                                domain=[('status', '=', 'dipinjam')])
    kembali_date = fields.Date(string='Tanggal Kembali')
    pengelola_id = fields.Many2one(string='Pengelola', comodel_name='res.users',
                                   domain=[('is_pengelola', '=', True)], required=True,
                                   default=lambda self: self.env.user)
    buku_id = fields.Many2one(string='Buku', comodel_name='perpustakaan.buku', related='pinjam_id.buku_id')
    anggota_id = fields.Many2one(string='Peminjam', comodel_name='res.users', domain=[('is_anggota', '=', True)],
                                 related='pinjam_id.anggota_id')
    pinjam_date = fields.Date(string='Tanggal Pinjam', related='pinjam_id.pinjam_date')
    deadline = fields.Date(string='Deadline Pengembalian', related='pinjam_id.deadline')
    status = fields.Selection([
        ('default', 'Default'),
        ('selesai', 'Sudah Kembali'),
        ('selesai_telat', 'Sudah Kembali (Terlambat)')
    ], 'Status', default='default')

    @api.model
    def create(self, vals_list):
        if vals_list.get('name', 'New') == 'New':
            vals_list['name'] = self.env['ir.sequence'].next_by_code('perpustakaan.pengembalian.seq') or 'New'
            result = super(PerpustakaanPengembalian, self).create(vals_list)
            return result

    def action_confirm(self):
        data = self.env['perpustakaan.peminjaman'].search([('name', '=', self.pinjam_id.name), ('status', '=', 'dipinjam')],
                                                          limit=1)
        if data:
            data.write({'status': 'kembali'})
        if self.kembali_date > self.deadline:
            self.status = 'selesai_telat'
        else:
            self.status = 'selesai'
