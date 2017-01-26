# -*- coding: utf-8 -*-
from typing import Dict, Any

__all__ = ["editor"]


def edit(project: Any, params: Dict[str, str]) -> Dict[str, str]:
    """
    Add a new method to a Python class in its given module.

    Note: For now, we play dumb and simply add a method at the end of the
    file. Next step will be to load the Python AST or, even better, rely on
    some microgrammars to aim exactly where we want to!
    """
    eng = project.context().pathExpressionEngine()
    res = eng.evaluate(project, "//*/File()[@name='"+params['mod_name']+"']")

    for match in res.matches():
        print("Modifying module => " + match.path())
        match.append("\n    def "+params['method_name']+"(self): \n        print('hey')")

    return {"status":"OK", "message": ""}


editor = {
    "tags": ["python"],
    "name": "AddMethodToPythonClass",
    "description": "Add a method to a Python class",
    "parameters": [
        {
            "required": True,
            "description": "the name of the module to edit",
            "displayName": "Python import module",
            "displayable": True,
            "validInput": "the name of the module to edit",
            "pattern": "^\\w[-\\w.]*$",
            "minLength": 1,
            "name": "mod_name"
        },
        {
            "required": True,
            "description": "the class name in that module",
            "displayName": "Class name",
            "displayable": True,
            "validInput": "the name of a class",
            "pattern": "^[\\w]*$",
            "minLength": 1,
            "name": "class_name"
        },
        {
            "required": True,
            "description": "the new method name",
            "displayName": "Method name",
            "displayable": True,
            "validInput": "the name of the method to add",
            "pattern": "^[\\w]*$",
            "minLength": 1,
            "name": "method_name"
        }
    ],
    "edit": edit
}
