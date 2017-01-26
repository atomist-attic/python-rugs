# Atomist 'python-rugs'

Work in progress. Unreleased.

These [Rugs][rug] will enable Rug to elegantly work with [Python][python] 
files and projects.

For now those editors don't actually do anything, they only showcase the 
toolchain.

[rug]: http://docs.atomist.com/
[python]: https://www.python.org/
[npm]: https://www.npmjs.com/
[cli]: https://github.com/atomist/rug-cli
[JavaScripthon]: https://github.com/azazel75/metapensiero.pj
[transcrypt]: http://transcrypt.org/

## Requirements

This Rug archive requires the followings to be installed:

* [Python][python] 3.5
* [npm][npm]

Once installed, run the following commands:

```
$ cd .atomist
$ pip install -r requirements.txt
$ npm install 
```

This will install both the Python dependencies and the JavaScript dependencies
to generate appropriate Rug JavaScript payload.

## Building this Rug

Unlike Rugs implemented using the DSL or TypeScript, this one needs an extra
step before you can test, install or publish it.

Indeed, it is implemented in Python that is transpiled to JavaScript that can
be loaded by the Rug runtime.

To achieve this, run the following command:

```
$ python py2rug.py
```

This will transpile all Python editors into their EcmaScript 5 twin. 

Now you can use the [rug cli][cli] as usual to apply your editors.

## Can writing Rugs in Python be done?

The cuurrent archive demonstrates that it's possible to write a Rug in a 
language that is not JVM based nor JavaScript superset.

However, it also shows the limits of such an exercise. Indeed, even though you
can transpile the Python language into its JavaScript equivalent, the Python
libraries are not converted into their related JavaScript package (obviously).

If we wanted to achieve something remotely useful, we would need to go with
one of the following options:

1. implement JavaScript modules (that are allowed in our runtime) in Python
   with the same interface so that we can write Python code with those 
   interfaces. This is what we do when we export our Scala types interfaces
   to TypeScript so TypeScript editors don't complain
2. implement the entire Rug runtime in Python and have a Python rug engine
   much like what we have in JVM land. Then we could benefit from the Command
   interface
3. use a different transpiler that transpiles all the Python code (and imported
   modules) into JavaScript
4. do not bother pretending we are writing Python that runs and type using
   the Python code exactly what we would type in Javascript so the code would
   run once generated only

None of these options are particularly attractive.

Option 2. is just not a potential candidate as we will not implement, run and
support multiple runtimes.

Option 1. could be done if we had only a very small 
subset of functions we wanted to map between Python and JavaScript. These could
live in a python package that we support (see the `rugpy` package
in the `.atomist/editors` directory). This would be limited however because we 
would have to map all imported dependencies as well.

Option 3. is not a relevant alternative because it smells endless subtle bugs.
But we could look at [Transcrypt][transcrypt] if we were curious.

Option 4. would work with the transpiler we are using in this project because
this transpiler only reads the Python AST to transpile it. It does not load it
as if it was runnable Python. As long as the code written respects the AST, that
would be fine. Even if we import modules that don't exist in Python so that 
those imports get mapped to a JS `require(...)` call by the transpiler.

Overall, this shows that to write useful Rugs in languages outside the JVM/JS
ecosystems isn't going to be simple.

## Rugs

### AddMethodToPythonClass

The `AddMethodToPythonClass` editor adds a method to a class in a module.

#### Prerequisites

There are no prerequisites to running this editor.

#### Parameters

To run this editor, you must supply the following parameters.

Name | Required | Default | Description
-----|----------|---------|------------
`mod_name` | Yes | |  The relative path, to the root of the project, of the module to edit
`class_name` | Yes | |  The name of the class to the method to (not used yet)
`method_name` | Yes | | The name of the method to add

#### Running

Assuming your project directory structure:

```
myproj
  __init__.py
  subpkg
    __init__.py
    mymod.py

Run it as follows:

```
$ cd myproj
$ rug generate atomist-rugs:python-rugs:AddMethodToPythonClass \
    mod_name=mymod.py \
    class_name=accounting\
    method_name=hello
```


---
Created by [Atomist][atomist].
Need Help?  [Join our Slack team][slack].

[atomist]: https://www.atomist.com/
[slack]: https://join.atomist.com/
