import os
import sys
import time
import subprocess
import json

import streamlit as st
from pkpy_bindings import generate

if sys.platform != 'linux':
    st.error("This app only works on linux")
    st.stop()

if not os.path.exists("tmp"):
    os.mkdir("tmp")

if not os.path.exists("raylib_parser"):
    ok = os.system('gcc -o raylib_parser -O1 raylib_parser.c')
    if ok != 0:
        st.error("Failed to compile `raylib_parser`")
        st.stop()

st.set_page_config(layout="wide", page_icon=":snake:", page_title="pkpy<=>c bindings generator")

class Config:
    @staticmethod
    def instance() -> 'Config':
        if st.session_state.get('config') is None:
            st.session_state['config'] = Config()
        return st.session_state['config']

    def __init__(self):
        self.output = None

config = Config.instance()

uploaded_file = st.file_uploader("Choose a `.h` file", type="h")

module_name = st.text_input(
    "Module name",
    value="raylib",
)

raylib_parser_define = st.text_input(
    "raylib_parser `--define`",
    value="RLAPI",
)

raylib_parser_truncate = st.text_input(
    "raylib_parser `--truncate`",
    value="RLGL IMPLEMENTATION",
)

vector_pattern = st.text_input(
    "Vector pattern",
    value=r'\bVector(\d)\b',
)

opaque_structs = st.text_input(
    "Opaque structs",
    value="[]",
)

if st.button("Generate"):
    if uploaded_file is None:
        st.error("Please upload a file")
        st.stop()
    prefix = f'tmp/{time.time_ns()}'
    os.mkdir(prefix)

    input_path = f"{prefix}/{uploaded_file.name}"
    output_path = f"{prefix}/{uploaded_file.name}.json"

    with open(input_path, "w", encoding='utf-8') as f:
        f.write(uploaded_file.getvalue().decode("utf-8"))

    cmd = ['./raylib_parser', '-f', 'JSON', '-i', input_path, '-o', output_path, '--define', raylib_parser_define, '--truncate', raylib_parser_truncate]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        st.error(stderr)
        st.stop()
    st.success(stdout)

    config.output = generate(
        output_path,
        module_name=module_name,
        headers=[f'{module_name}.h'],
        vector_pattern=vector_pattern,
        opaque_structs=json.loads(opaque_structs),
    )

if config.output is not None:
    if len(config.output.messages) > 0:
        st.success('\n\n'.join(config.output.messages))
    col_0, col_1, col_2 = st.columns(3)
    pyi = '\n'.join(config.output.pyi)
    cpp = '\n'.join(config.output.cpp)

    col_0_name = f"{module_name}.pyi"
    col_0.download_button(f"Download {col_0_name}", pyi, col_0_name)
    
    col_1_name = f"{module_name}.json"
    col_1.download_button(
        f"Download {col_1_name}",
        json.dumps(config.output.metadata, indent=4, ensure_ascii=False),
        col_1_name
    )

    col_2_name = f"{module_name}w.cpp"
    col_2.download_button(f"Download {col_2_name}", cpp, col_2_name)

    col_L, col_R = st.columns(2)
    col_L.code(pyi, language="py")
    col_R.code(cpp, language="cpp")

