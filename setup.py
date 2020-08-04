from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('garajes.pyw', base=base, icon='iconos\icono.ico')
]

setup(name='Garajes',
      version = '1.0',
      description = '',
      options = {'build_exe': build_options},
      executables = executables)
