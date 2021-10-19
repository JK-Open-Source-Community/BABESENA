from distutils.dir_util import copy_tree, mkpath, remove_tree, create_tree
from distutils.dir_util import remove_tree
remove_tree("docs")
mkpath("docs")
copy_tree("_build\html", "docs")
