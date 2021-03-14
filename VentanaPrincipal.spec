# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['VentanaPrincipal.py'],
             pathex=['D:\\Users\\FORTY\\Downloads\\Programa Simplex - Big M - PERT-CMP'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [("./interfaz/img/atardecer2.jpg","interfaz/img/atardecer2.jpg","DATA"),("./interfaz/img/iconoDelaTabla.ico","interfaz/img/iconoDelaTabla.ico","DATA"),
("./interfaz/img/fondoPert.png","interfaz/img/fondoPert.png","DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='VentanaPrincipal',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='interfaz\\img\\iconoDelaTabla.ico')
