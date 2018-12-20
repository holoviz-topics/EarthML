import os
import yaml

if "PYCTDEV_ECOSYSTEM" not in os.environ:
    os.environ["PYCTDEV_ECOSYSTEM"] = "conda"

from pyctdev import *  # noqa: api

root_param = {
    'name':'root',
    'long':'path to root project dir',
    'short': 'r',
    'type': str,
    'default': ''
}
path_param = {
    'name':'path',
    'long':'examples path',
    'short': 'p',
    'type': str,
    'default': 'examples'
}
filename_param = {
    'name':'filename',
    'long':'catalog filename',
    'short': 'f',
    'type': str,
    'default': 'catalog.yml'
}


def _prepare_paths(root, path, filename):
    if root == '':
        root = os.getcwd()
    root = os.path.abspath(root)
    path = path if os.path.isabs(path) else os.path.join(root, path)
    return {
        'real': os.path.join(path, filename),
        'test': os.path.join(path, 'data', '.data_stubs', filename)
        'temp': os.path.join(path, 'tmp_', filename)
    }


def task_conda_setup():
    """Experimental: set up conda with updated version, and yes set to always"""
    return {'actions': [
        "conda config --set always_yes True",
        "conda update conda",
    ]}

def task_env_setup():
    """Experimental: create environment from environment.yml and environment-dev.yml"""
    return {'actions': [
        "pip uninstall -y doit pyctdev",
        "conda env update -f environment.yml -n earthml",
        "conda env update -f environment-dev.yml -n earthml",
        "conda activate earthml",
    ]}

def task_small_data_setup():
    """Experimental: create catalog from real and stubs and substitute for real"""

    def create_joined_catalog(root, path, filename):
        paths = _prepare_paths(root, path, filename)

        # move real catalog file to temp if temp doesn't exist
        if os.path.exists(paths['temp']):
            print('Temp file already exists')
            return

        os.rename(paths['real'], paths['temp'])
        os.remove(paths['real'])

        # create joined version reading from temp and test
        with open(paths['temp']) as temp_cat:
            d = yaml.load(temp_cat)
            with open(paths['test']) as test_cat:
                d['sources'].update(**yaml.load(test_cat)['sources'])
            print('NEW CATALOG CONTENTS:', d)

            with open(path['real'], mode='w') as real_cat:
                real_cat.write(yaml.dump(d))

    return {
        'actions':[
            CmdAction(create_joined_catalog),
        ],
        'params': [root_param, path_param, filename_param]}

def task_small_data_cleanup():
    """Experimental: Replace the test version of the catalog with the real one"""

    def remove_joined_catalog(root, path, filename):
        paths = _prepare_paths(root, path, filename)

        if os.path.exists(paths['temp']):
            os.remove(paths['real'])
            os.rename(paths['temp'], paths['real'])

    return {
        'actions':[
            CmdAction(remove_joined_catalog),
        ],
        'params': [root_param, path_param, filename_param]}

def task_build_website():
    """Experimental: create test_catalog and use in place of real catalog"""
    return {'actions':[
        "nbsite generate-rst --org pyviz-topics --project-name earthml --offset 1 --nblink=top",
        "nbsite build --what=html --output=builtdocs",
        "doit move_json"
    ]}

def task_move_json():
    """Experimental: copy json from doc dir to builtdocs. This moved to nbsite"""
    return {'actions':[
        'cp doc/*.json builtdocs/ 2>/dev/null || :',
        'cp doc/topics/*.json builtdocs/topics/ 2>/dev/null || :',
        'cp doc/tutorial/*.json builtdocs/tutorial/ 2>/dev/null || :',
    ]}
