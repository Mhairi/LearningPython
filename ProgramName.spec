# -*- mode: python -*-
a = Analysis(['kate2.py'],
             pathex=['/home/bryan/LearningPython'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ProgramName',
          debug=False,
          strip=None,
          upx=True,
          console=False )
