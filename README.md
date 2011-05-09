Strfrag overview
================

A `strfrag.StringFragment` represents part of a `str` object.
This can be used to avoid copying long `str` objects as you
incrementally process them.

```
>>> from strfrag import StringFragment
>>> sf = StringFragment("hello world", 2, 8)
>>> sf
<StringFragment for 0xf74c5240, pos=2, size=8, represents 'llo worl'>
>>> str(sf)
'llo worl'
>>> sf.as_buffer()
<read-only buffer for 0xf74c5240, size 8, offset 2 at 0xf74c5220>
>>> StringFragment("hello world", 1, 5) == StringFragment("ello ", 0, 5)
True
```


Installation
============

`python setup.py install`

This installs the modules `strfrag` and `test_strfrag`.


Running the tests
=================

Install Twisted, then run `trial strfrag`


Code style notes
================

This package mostly follows the Divmod Coding Standard
<http://replay.web.archive.org/http://divmod.org/trac/wiki/CodingStandard> with a few exceptions:

*	Use hard tabs for indentation.

*	Use hard tabs only at the beginning of a line.

*	Prefer to have lines <= 80 characters, but always less than 100.
