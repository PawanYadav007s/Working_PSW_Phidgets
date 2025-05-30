# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller import __main__ as pyinstaller

project_root = os.path.abspath('.')
phidget_dlls_dir = r'C:\Program Files\Phidget22\bin'  # Change this path if different
static_dir = os.path.join(project_root, 'static')
templates_dir = os.path.join(project_root, 'templates')

# Ensure the directory containing your Phidget DLLs is correctly specified
phidget_dlls = collect_data_files('Phidget22', subdir='bin')  # Adjust if needed

a = Analysis(
    ['app.py'],  # Your main script
    pathex=[],
    binaries=phidget_dlls,  # Include DLLs here
    datas=[
        (templates_dir, 'templates'),
        (static_dir, 'static'),
    ],
    hiddenimports=[
        'jinja2.ext',
        'pyvisa.resources.serial',
        'pyvisa_py',
        'zeroconf',
        'serial.tools.list_ports',
        # Any other required imports
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

# Create the final executable
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PSW_Controller',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to True if you need a console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(project_root, 'icon.ico'),  # Correct absolute path
)
