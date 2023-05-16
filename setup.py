import sys
from cx_Freeze import setup, Executable


# ---------------------------------------------------------------------
build_exe_options = {
    "packages": ['customtkinter', 'tkinter', 'datetime', 'hashlib', 
                 'PIL', 'json', 'sqlite3', 'os', 'sys','CTkMessagebox'],  
                 # List of packages to include
    "excludes": ['flask', 'ttkthemes',],  # List of packages to exclude
    "include_files": ['icons/','config/', 
    'C:/Users/Kennart Tech/AppData/Local/Programs/Python/Python310/Lib/site-packages/customtkinter/assets'],  # List of files to include
    "include_msvcr": True,  # This include Microsoft Visual C++ runtime
    "optimize": 2, #These increase the speed of the software in terms of the perfomance                      
    # "zip_include_packages": ['icons/tools'],
    # "zip_exclude_packages": [],
    # "zip_exclude_dlls": [],
}
# ----------------------------------------------------------------------

# ------------------------------------------------------------------
shortcut_table = [#This defines the shorcut to be created for the frozen executable
    ("DesktopShortcut",             # Shortcut
     "DesktopFolder",               # Directory_
     "SwiftSell",                   # Desktop icon Name
     "TARGETDIR",                   # Component_
     "[TARGETDIR]homepage.exe",     # Target
     None,                          # Arguments
     None,                          # Description
     None,                          # Hotkey
     None,                          # Icon
     None,                          # IconIndex
     None,                          # ShowCmd
     "TARGETDIR",                   # WkDir
     ),
]


msi_data = {"Shortcut": shortcut_table}
# ------------------------------------------------------------------

# -----------------------------------------------------------------
base = None  #this will set the base of the application to a GUI application on Windows.
if sys.platform == "win32":
    base = "Win32GUI"
# ------------------------------------------------------------------

# ------------------------------------------------------------------------
script_path = "homepage.py"  # Replace with the path to your Python script
# ------------------------------------------------------------------------

# -----------------------------------------------------------------------
setup(
    name="SwiftSell",
    version="1.1.0",
    description="POINT OF SALES",
    options={
        "build_exe": build_exe_options,
        "bdist_msi": {"data": msi_data},
    },
    executables=[Executable(script_path, base=base, icon="icons/logo.ico", shortcut_name="homepage")],
    author="Softwarehub",
)
# ----------------------------------------------------------------------------

#✅ """Make sure to install  (pip install cx-Freeze)

#✅ """Instruction to use this script to convert you python files into .exe"""

#✅ """Make sure where the icons='icons/logo.ico' 'is', you have the same directory in you project folder containing ico file"""

"""At the top where `include_files` is make sure you follow and copy your path to where customtkinter is install and replace it with my own

#🚨✅ example  (C:\Users\Kennart Tech\AppData\Local\Programs\Python\Python310\Lib\site-packages\customtkinter\assets)
"""

            #-------------------Final----------------#
#✅ """Open your windows terminal navigate to your project directory where your python script that you want to convert is, then type (e.g python setup.py bdist_msi) and hit enter"""