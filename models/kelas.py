from odoo import fields, models, api


class PerpustakaanKelas(models.Model):
    _name = 'perpustakaan.kelas'

    name = fields.Char(string="Kelas", required=True)
    anggota_ids = fields.One2many(comodel_name="res.users", inverse_name="kelas_id", string="Anggota",
                                domain=[('is_anggota', '=', True)])

