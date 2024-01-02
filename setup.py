from distutils.core import Extension, setup

setup_args = dict(ext_modules=[Extension("monitor", ["monitor/monitor.c"])])
setup(**setup_args)
