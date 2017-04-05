
from setuptools import setup, find_packages
setup(name='three',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      install_requires=['setuptools'],
      entry_points = """\
      [console_scripts]
      three = three.three:three
      """
)
