from setuptools import setup, find_packages

import trading

with open("README.md", "r") as readme_file:
    readme = readme_file.read()
    
requirements = []

setup(
      name="trading",
      version=trading.__version__,
      author="Daniel Gallagher",
      author_email="daniel-gallagher@outlook.com",
      description="Trading Application",
      long_description=readme,
      long_description_content_type="text/markdown",
      url="https://github.com/danielgallagher8/trading.git",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requirements,
      classifiers=[
              "Programming Language :: Python :: 3.7",
              "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
              ],
      )
