# Note by Nikolaus Demmel 28.03.2014: My contributions are licensend under the
# same as CMake (BSD). My adaptations are in part based
# https://github.com/qgis/QGIS/tree/master/cmake which has the following
# copyright note:

# FindLibPython.py
# Copyright (c) 2007, Simon Edwards <simon@simonzone.com>
# Redistribution and use is allowed according to the terms of the BSD license.
# For details see the accompanying COPYING-CMAKE-SCRIPTS file.

import sys
import distutils.sysconfig

print(f"exec_prefix:{sys.exec_prefix}")
print(f"major_version:{str(sys.version_info[0])}")
print(f"minor_version:{str(sys.version_info[1])}")
print(f"patch_version:{str(sys.version_info[2])}")
print(f"short_version:{'.'.join(map(lambda x: str(x), sys.version_info[:2]))}")
print(f"long_version:{'.'.join(map(lambda x: str(x), sys.version_info[:3]))}")
print(f"py_inc_dir:{distutils.sysconfig.get_python_inc()}")
print("site_packages_dir:%s" % distutils.sysconfig.get_python_lib(plat_specific=1))
for e in distutils.sysconfig.get_config_vars('LIBDIR'):
  if e != None:
    print(f"py_lib_dir:{e}")
    break
