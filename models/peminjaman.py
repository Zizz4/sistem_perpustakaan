from odoo import fields, models, api, _
from datetime import date
from odoo.exceptions import UserError


class PerpustakaanPeminjaman(models.Model):
    _name = 'perpustakaan.peminjaman'

    name = fields.Char(string='Pinjaman', copy=False, readonly=False, index=True,
                       default=lambda self: _('New'))
    anggota_id = fields.Many2one(string='Peminjam', required=True, comodel_name='res.users',
                                 domain=[('is_anggota', '=', True)])
    buku_id = fields.Many2one(string='Buku', required=True, comodel_name='perpustakaan.buku')
    pinjam_date = fields.Date(string='Tanggal Pinjam', required=True, default=date.today())
    deadline = fields.Date(string='Deadline', required=True)
    pengelola_id = fields.Many2one(string='Pengelola', comodel_name='res.users', domain=[('is_pengelola', '=', True)],
                                   required=True, default=lambda self: self.env.user)
    status = fields.Selection([
        ('default', 'Default'),
        ('dipinjam', 'Dipinjam'),
        ('kembali', 'kembali')
    ], 'Status', default='default')

    @api.constrains('pinjam_date','deadline')
    def _constrains_peminjaman(self):
        for rec in self:
            if rec.pinjam_date > rec.deadline:
                raise UserError(_("Tidak bisa pinjam apabila deadline terlewat!"))

    @api.model
    def create(self, vals_list):
        if vals_list.get('name', 'New') == 'New':
            vals_list['name'] = self.env['ir.sequence'].next_by_code('perpustakaan.peminjaman.seq') or 'New'
            result = super(PerpustakaanPeminjaman, self).create(vals_list)
            return result

    def action_check_pinjam(self):
        existing_record = self.search([
            ('buku_id', '=', self.buku_id.name),
            ('status', '=', 'dipinjam'),
        ], limit=1)
        if existing_record:
            raise UserError(_('Buku sedang dipinjam'))
        else:
            raise UserError(_('Buku dapat dipinjam'))

    def action_confirm(self):
        existing_record = self.search([
            ('buku_id', '=', self.buku_id.name),
            ('status', '=', 'dipinjam'),
        ], limit=1)
        if existing_record:
            raise UserError(_('Buku sedang dipinjam'))
        else:
            self.status = 'dipinjam'

    def action_kembalikan_buku(self):
        self.status = 'kembali'

    def action_batal_pinjam(self):
        self.status = 'default'
