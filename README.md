# Python package for Kyon robot description

This repository repackages the kyon repository into a pip-installable package. Making it installable via pip
and findable with python utilities.
You can find an example of how to do so in `src/pykyon/xacro_compile_example.py`.

As this is a repo containing a git submodule, clone with:

```
git clone --recurse-submodules <repo_url>
```

You can test that everything works with `src/pykyon/xacro_compile_example.py`.
To run the script you will need to install pykyon with pip and to install adarl (just for a couple of helper
functions, no need to install its full depenndencies).
You can install pykyon either directly from pip (using the git repo) or by cloning it and installing it in editable mode:
I suggest you do all of this in a virtual environment.

```
pip install -e pykyon
```

You can install some basic dependencies with:

```
pip install -r pykyon/requirements.txt
```