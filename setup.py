import cx_Freeze

executables = [cx_Freeze.Executable("main.py", base="Win32GUI")]

cx_Freeze.setup(
    name="Math Game",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": [("sound_files", "sound_files"), ("images", "images"),
                                             ("save_files", "save_files")]}},
    executables=executables
)
