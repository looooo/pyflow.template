import os
from setuptools import setup, find_packages

# TODO: This is currently not possible because of missing __init__.py
# from PyFlow.Packages.template.version import currentVersion

package_dir = os.path.join("PyFlow", "Packages")
packages = find_packages(package_dir)
packages = [os.path.join(package_dir, pkg) for pkg in packages]

setup(name='pyflow.template',
      version="0.0.1",
      packages=packages,
      maintainer="looooo",
      maintainer_email="sppedflyer@gmail.com",
      url="https://github.com/looooo/pyflow.template",
      description="template for a pyflow extensions",
      # install_requires=['numpy'], 
      include_package_data=True)