# -*- coding: utf-8 -*-
import glob
import os
from typing import List, Any

import click
from metapensiero.pj import __main__ as javascripthon


things_to_remove = [
"""
Object.defineProperty(exports, "__esModule", {
    value: true
});
""",
'var _typing = require("typing");',
"var _typing = require('typing');"
]

@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('javascripthon_args', nargs=-1, type=click.UNPROCESSED)
def run(javascripthon_args: List[Any]):
    """
    Generate JS modules from editors and their Python direct dependencies.
    The output is EcmaScript 5 in a format suitable to be applied in the Rug
    runtime.
    """
    try:
        args = javascripthon_args
        if not javascripthon_args:
            args = "--es5 -o .atomist/editors .atomist/editors/".split(" ")
        javascripthon.main(args)
    except SystemExit:
        # the previous function uses sys.exit() and we don't want
        # to exit now!
        pass

    curdir = os.path.dirname(__file__)
    editors_dir = os.path.join(curdir, '.atomist', 'editors')

    # javascripthon also creates ES6 modules but we don't want them
    # as they will not be loaded by the rug runtime
    for match in glob.iglob(os.path.join(editors_dir, "**/*es6.*"), recursive=True):
        print("Removing: %s" % match)
        os.remove(match)

    # The generated JS modules contain a few things 
    # the rug runtime can't deal with
    for match in glob.iglob(os.path.join(editors_dir, "**/*.js"), recursive=True):
        print("Updating js module: %s" % match)
        with open(match, 'r+') as f:
            content = f.read()
            for thing in things_to_remove:
                content = content.replace(thing.strip(), "")
            f.seek(0)
            f.write(content)
            f.truncate()

    print("Ready! You can now use the rug CLI.")

if __name__ == '__main__':
    run()
