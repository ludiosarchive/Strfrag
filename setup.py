#!/usr/bin/env python

from distutils.core import setup

import strfrag

setup(
	name='Strfrag',
	version=strfrag.__version__,
	description=('StringFragment type to represent parts of str objects; '
		'used to avoid copying strings during processing'),
	url="https://github.com/ludios/Strfrag",
	author="Ivan Kozik",
	author_email="ivan@ludios.org",
	classifiers=[
		'Programming Language :: Python :: 2',
		'Development Status :: 3 - Alpha',
		'Operating System :: OS Independent',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
	],
	py_modules=['strfrag', 'test_strfrag'],
)
