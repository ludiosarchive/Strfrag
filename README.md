Strfrag
=======

A `strfrag.StringFragment` represents part of a `str` object.
This can be used to avoid copying long `str` objects as you
incrementally process them.

```
>>> from strfrag import StringFragment
>>> sf = StringFragment("hello world", 2, 8)
>>> sf
<StringFragment for 0xf74c5240, pos=2, size=8, represents 'llo worl'>
>>> sf[2]
'o'
>>> sf[2:5]
<StringFragment for 0xf74c5240, pos=4, size=3, represents 'o w'>
>>> str(sf)
'llo worl'
>>> sf.as_buffer()
<read-only buffer for 0xf74c5240, size 8, offset 2 at 0xf74c5220>

# StringFragments that represents the same bytes are equal:

>>> StringFragment("hello world", 1, 5) == StringFragment("ello ", 0, 5)
True
```



## Installation

`python setup.py install`

This installs the modules `strfrag` and `test_strfrag`.



## Running the tests

Install Twisted, then run `trial strfrag`
