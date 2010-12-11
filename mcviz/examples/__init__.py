from os import walk
from os.path import join as pjoin
from pkg_resources import resource_filename


def find_all_files(where, ignore=lambda x: False):
    all_files = []
    for path, dirs, files in walk(where):
        all_files.extend(pjoin(path, f) for f in files if not ignore(f))
    return sorted(all_files)

def get_all_example_input_paths():
    return find_all_files(EXAMPLE_INPUT_BASE,
                          ignore=lambda f: f.endswith(".py") or
                                           f.endswith(".pyc"))
                                  
EXAMPLE_INPUT_BASE = resource_filename("mcviz.examples", "inputs")
EXAMPLE_INPUT_PATHS = get_all_example_input_paths()
EXAMPLE_INPUT_PATHS_NOBASE = [
    f[len(EXAMPLE_INPUT_BASE)+1:] for f in get_all_example_input_paths()]
