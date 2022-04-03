import pytest
import nbformat as nbf
import os
from IPython import get_ipython, start_ipython
import subprocess


def test_basic():
    assert True

def create_notebook(name, code):
    nb = nbf.v4.new_notebook()
    nb['cells'] = [nbf.v4.new_code_cell(code)]
    fname = name
    with open(fname, 'w') as f:
        nbf.write(nb, f)

def delete_notebooks(names):
    for name in names:
        if os.path.isfile(name):
            os.remove(name)
    
def test_create_notebook():
    create_notebook('start_nb.ipynb', 'print("hello world")')
    assert os.path.isfile('start_nb.ipynb')
    subprocess.run(['jupyter', 'nbconvert', '--execute', '--inplace', 'start_nb.ipynb'])
    delete_notebooks(['start_nb.ipynb'])

# def test_ipython():
#     inst = start_ipython()
#     assert inst is not None
#     assert inst.get_ipython().user_ns is not None
