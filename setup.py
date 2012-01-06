import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = CHANGES = ''

requires = ['pyramid', 'Paste']

setup(name='pyramid_basicauth',
      version='0.0',
      description="Pyramid plugin for HTTP Basic access authentication",
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
          "Framework :: Pylons",
          "Intended Audience :: Developers",
          "License :: Repoze Public License",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: WSGI",
          "Topic :: Internet :: WWW/HTTP",
          ],
      keywords='authentication pyramid basic',
      author='',
      author_email='',
      url='http://pypi.python.org/pypi/pyramid_basicauth',
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      )
