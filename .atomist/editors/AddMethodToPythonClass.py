# -*- coding: utf-8 -*-
from typing import Dict, Any

__all__ = ["editor"]


def edit(project: Any, params: Dict[str, str]) -> Dict[str, str]:
    """
    Add a new method to a Python class in its given module.

    TODO: See why an <EOF> char is added along with the new method
    """
    eng = project.context().pathExpressionEngine()
    res = eng.evaluate(project, "/Directory()/File()[@name='"+params['mod_name']+"' and /PythonRawFile()]/PythonRawFile()//classdef()[/NAME[@value='"+params['class_name']+"']]")
    for match in res.matches():
        match.append("\n    def "+params['method_name']+"(self):\n        print('hey')\n")

    return {"status":"OK", "message": "Method added to class"}


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
