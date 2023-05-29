''' USE THIS TO GENERATE THE .ZIP TO INSTALL THE ADDON.
    The output folder is /builds '''

# Update this to match your addon module name aka folder name of your source.
ADDON_MODULE_NAME = 'addon_template'


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import glob
try:
    import python_minifier
    use_minifier = True
except ImportError as e:
    use_minifier = False
from fnmatch import fnmatch
from os.path import join, dirname, exists, isdir
from os import walk
from pathlib import PurePath
from shutil import ignore_patterns, make_archive, copytree, rmtree


root=dirname(__file__)
module_dir=join(root, ADDON_MODULE_NAME)
build_dir=join(root, 'build')

# Make a copy of the src folder to build dir.
_temp_dir = join(build_dir, 'temp')
if exists(_temp_dir) and isdir(_temp_dir):
    rmtree(_temp_dir, ignore_errors=True)
module_copy_dir = join(_temp_dir, ADDON_MODULE_NAME) # So that we have a folder inside the .zip with all addon files in there. 'temp' will be replaced by the .zip...
copytree(module_dir, module_copy_dir, ignore=ignore_patterns('__pycache__', '*.pyc', '*.pyo', '*.old.py', '*.dev.py'))

# Minify .py files to decrease space.
if use_minifier:
    minify_re=join(module_copy_dir, '/**/*.py') # r'.\sculpt_plus\*.py'
    code=''
    # for filepath in  glob.iglob(minify_re, recursive=True):
    for path, subdirs, files in walk(module_copy_dir):
        for filename in files:
            filepath = PurePath(path, filename)
            if filepath.suffix != '.py':
                continue
            with open(filepath, 'r', encoding="utf8") as f:
                raw_code = f.read().replace("\0", "")
                if not raw_code:
                    continue
                code = python_minifier.minify(raw_code, remove_annotations=False)
            with open(filepath, 'w', encoding="utf8") as f:
                f.write(code)

# Compress folder to .zip
version='0.0.1'#str(bl_info['version'])[1:-1].replace(', ', '.')
with open(join(module_copy_dir, '__init__.py'), 'r') as f:
    for line in f.readlines():
        if line.startswith('bl_info'):
            if use_minifier:
                bl_info = eval(line[8:])
                version = str(bl_info['version'])[1:-1].replace(', ', '.')
            break
build_name=ADDON_MODULE_NAME.replace('_', ' ').replace('-', ' ').capitalize().replace(' ', '')
zip_path=join(build_dir, build_name+'_'+version)
make_archive(zip_path, 'zip', _temp_dir)

# Clenup.
rmtree(_temp_dir, ignore_errors=True)
