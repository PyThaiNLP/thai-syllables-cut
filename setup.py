# -*- coding: utf-8 -*-
from setuptools import setup
requirements = ['pythainlp>=1.5.2','future>=0.16.0']
setup(name='pythaisyllables',
      version='0.1.1',
      description='Thai syllables segmentation',
      url='https://github.com/wannaphongcom/thai-syllables-cut',
      author='Wannaphong Phatthiyaphaibun',
      author_email='wannaphong@kkumail.com',
      license='Apache Software License 2.0',
      install_requires=requirements,
      package_data={'': ['LICENSE', 'LICENSE-DICT.md', 'README.md', 'dict.txt']},
      include_package_data=True,
      packages=['.'],
      zip_safe=False)