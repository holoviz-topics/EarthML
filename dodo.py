import os

if "PYCTDEV_ECOSYSTEM" not in os.environ:
    os.environ["PYCTDEV_ECOSYSTEM"] = "conda"

from pyctdev import *  # noqa: api


def _prepare_paths(root, path, filename):
    if root == '':
        root = os.getcwd()
    root = os.path.abspath(root)
    path = path if os.path.isabs(path) else os.path.join(root, path)
    return {
        'real': os.path.join(path, filename),
        'test': os.path.join(path, 'data', '.data_stubs', filename),
        'temp': os.path.join(path, 'tmp_' + filename),
    }


def task_ecosystem_setup():
    """Set up conda with updated version, and yes set to always"""
    return {'actions': [
        "conda config --set always_yes True",
        "conda update conda",
    ]}


def task_env_create():
    """Create environment from environment.yml and environment-dev.yml"""
    return {'actions': [
        "pip uninstall -y doit pyctdev",
        "conda env update -f environment.yml -n earthml"#,
#        "conda env update -f environment-dev.yml -n earthml",
    ]}


def task_small_data_setup():
    """Experimental: Create catalog from real and stubs; substitute for real catalog."""

    def create_joined_catalog(root='', path='examples', filename='catalog.yml'):
        import yaml

        paths = _prepare_paths(root, path, filename)

        # move real catalog file to temp if temp doesn't exist
        if os.path.exists(paths['temp']):
            print("Fail: Temp file already exists - try 'doit small_data_cleanup'")
            return
        os.rename(paths['real'], paths['temp'])

        # create joined version reading from temp and test
        with open(paths['temp']) as temp_cat:
            d = yaml.load(temp_cat)
            with open(paths['test']) as test_cat:
                d['sources'].update(**yaml.load(test_cat)['sources'])

                with open(paths['real'], mode='w') as real_cat:
                    real_cat.write(yaml.dump(d))
        print("Created catalog from real and stubs; substituted for real catalog.")

    return {'actions': [create_joined_catalog]}


def task_small_data_cleanup():
    """Experimental: Replace the test version of the catalog with the real one"""

    def remove_joined_catalog(root='', path='examples', filename='catalog.yml'):
        paths = _prepare_paths(root, path, filename)

        if not os.path.exists(paths['temp']):
            print("Nothing to do - no temp file found. Use git status to "
                  "check that you have the real catalog at {}".format(paths['real']))
            return

        os.remove(paths['real'])
        os.rename(paths['temp'], paths['real'])
        print("Replaced the test version of the catalog with the real one.")

    return {'actions': [remove_joined_catalog]}


def task_build_website():
    """Build website using nbsite"""
    return {'actions':[
        "nbsite generate-rst --org pyviz-topics --project-name earthml --offset 1 --nblink=top",
        "nbsite build --what=html --output=builtdocs",
    ]}
