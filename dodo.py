import os
if "PYCTDEV_ECOSYSTEM" not in os.environ:
    os.environ["PYCTDEV_ECOSYSTEM"] = "conda"

from pyctdev import *  # noqa: api

def task_before_test():
    """Experimental: create test_catalog and use in place of real catalog"""
    return {'actions':[
        'python before_test.py',
        'mv test_catalog.yml examples/catalog.yml'
    ]}


def task_move_json():
    """Experimental: copy json from doc dir to builtdocs. This should move to nbsite"""
    return {'actions':[
        'cp doc/*.json builtdocs/ 2>/dev/null || :',
        'cp doc/topics/*.json builtdocs/topics/ 2>/dev/null || :',
        'cp doc/tutorial/*.json builtdocs/tutorial/ 2>/dev/null || :',
    ]}