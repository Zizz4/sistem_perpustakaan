{
    'name': 'Sistem Perpustakaan',
    'version': '16.0',
    'summary': 'Arkana Final Task Intensive Stage: Sistem Perpustakaan',
    'description': 'Sistem Perpustakaan',
    'category': 'Productivity',
    'author': 'Muhamad Syahril Aziz',
    'license': 'LGPL-3',
    'depends': ['base', 'contacts'],
    'data': [
        'security/security_perpustakaan_group_access.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/buku_sequence.xml',
        'data/peminjaman_sequence.xml',
        'data/pengembalian_sequence.xml',
        'views/menu.xml',
        'views/buku.xml',
        'views/penulis.xml',
        'views/penerbit.xml',
        'views/kelas.xml',
        'views/anggota.xml',
        'views/peminjaman.xml',
        'views/pengembalian.xml',
        'report/report_peminjaman.xml',
        'report/ir_actions_report.xml',
    ],
    'demo': [
        'demo/sistem_perpustakaan_demo_data.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
