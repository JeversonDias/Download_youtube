import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "include_files": [("icone.ico", "icone.ico")]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="NomeDoSeuPrograma",
    version="1.0",
    description="Descrição do seu programa",
    options={"build_exe": build_exe_options},
    executables=[Executable("Baixar_vídeos_do_youtube.pyw", base=base, icon="icone.ico")]
)
