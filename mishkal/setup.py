#! /usr/bin/python
from distutils.core import setup
from glob import glob

# to install type:
# python setup.py install --root=/

setup (name='SalamScout Softwares', version='0.5',
      description='Mishkal Softwares',
      author='Taha Zerrouki',
      author_email='taha.zerrouki@gmail.com',
      url='http://tashkeel.qutrub.org/',
      license='GPL',
	 console = [
        {
            "script": "scoutgameconsole.py",
            "icon_resources": [(1, "favicon.ico")]
        }
    ],
	 windows = [
        {
            "script": "main_gui.py",
            "icon_resources": [(1, "favicon.ico")]
        }
    ],

      #scripts=['Qutrub'],
      classifiers=[
          'Development Status :: 5 - Beta',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS independent',
          'Programming Language :: Python',
          ]);

