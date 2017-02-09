# -*- mode: python -*-

block_cipher = None


a = Analysis(['videogame_gui.py'],
             pathex=['/Users/ricardochejfec/Programming/python_gui/qt5_practice/videogame'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='videogame_gui',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='dab.icns')
app = BUNDLE(exe,
             name='videogame_gui.app',
             icon='dab.icns',
             bundle_identifier=None)
