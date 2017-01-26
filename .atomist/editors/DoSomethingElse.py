# -*- coding: utf-8 -*-
from typing import Dict, Any
from .rugpy.stuff import echo

__all__ = ["editor"]


def edit(project: Any, params: Dict[str, str]) -> Dict[str, str]:
    """
    Add a new method to a Python module.
    """
    print(echo("doing other thing"))
    return {"status":"OK", "message": "Everything is cool"}


editor = {
    "tags": ["python"],
    "name": "DoSomethingElse",
    "description": "Add a method to a Python class",
    "parameters": [
        {
            "required": True,
            "description": "the import path of the python module to load",
            "displayName": "Python import module",
            "displayable": True,
            "validInput": "the Python package import path of a Python module",
            "pattern": "^\\w[-\\w.]*$",
            "minLength": 1,
            "name": "python_mod_import"
        }
    ],
    "edit": edit
}
