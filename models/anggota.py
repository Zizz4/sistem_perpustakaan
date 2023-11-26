from odoo import fields, models, api


class Users(models.Model):
    _inherit = 'res.users'

    is_anggota = fields.Boolean(string='Anggota')
    is_pengelola = fields.Boolean(string='Pengelola')
    nis = fields.Char('NIS', size=8)
    kelas_id = fields.Many2one('perpustakaan.kelas', string='Kelas')
    gender = fields.Selection([
        ('pria', 'Pria'),
        ('wanita', 'Wanita')
    ], 'Gender', default='pria')
    umur = fields.Integer(string='Umur')
