.. _usage:

Usage
=====

Initialization
--------------

.. code-block:: python

    from chzip import ChZip, Locality
    z = ChZip()

.. _download-dir:

Download directory
------------------

The resources have been downloaded to a "resource directory" on your disk.
It contains all the files needed for this library to work.

It can be set manually by calling the constructor with the absolute path
as argument.

It defaults to the `res/` directory inside the installation path.
If changed, you will need to call 
:py:meth:`chzip.ChZip.download_and_unpack_all` once, and 
:py:meth:`chzip.ChZip.upgrade_all` after that.


.. _all-localities-matching-a-zip-code:

Get all localities matching a ZIP code
---------------------------------------

Example for ZIP code 1696, giving one result, i.e. one
:py:class:`chzip.Locality`, with a different short (18 chars) and
long (27 chars) name:

.. testcode::

    > results = z.find(1696)
    [<Locality[short_name='Vuisternens-Ogoz',
              long_name='Vuisternens-en-Ogoz',
              canton='FR']>]

    > results[0].long_name
    "Vuisternens-en-Ogoz"

..    > results[0]['long_name']
..    "Vuisternens-en-Ogoz"

.. note::
    If possible, always use the long name.


Get all locality *names* matching a ZIP code
--------------------------------------------

If all you want from the section ":ref:`all-localities-matching-a-zip-code`" is
the long name of localities, you can use this little snippet of code::

    z.long_names( zip=1696 )

.. The same goes for the short names. Of course you can use all the filters from
.. the :py:meth:`chzip.ChZip.find` method as explained below.

.. seealso::  :py:attr:`chzip.common.Locality.short_name` and 
    :py:attr:`chzip.common.Locality.long_name`
    to understand the difference of both formats.


Find localities matching the exact name
----------------------------------------

.. testcode::

    > z.find( long_name='Vuisternens-en-Ogoz' )

    [<Locality[short_name='Vuisternens-Ogoz',
    long_name='Vuisternens-en-Ogoz',
    canton='FR']>]

Find localities containing a search term
-----------------------------------------

The following method is very handy when you need to match the user input
with a locality of the database. It will returns a list of matching localities
as previously. 

.. testcode::

    > z.find( long_name_like='Vuisternens-en-Ogoz' )
    [<Locality[short_name='Vuisternens-Ogoz',
               long_name='Vuisternens-en-Ogoz',
               canton='FR']>]

.. warning:: 

    You are responsible to take care of the query string as
    this may return thousands of results with dumb queries, which could use a lot
    of memory. You may be served better with the `all` method as explained here:
    :ref:`all_method`.

.. .. note:: 
.. 
..     You can use a SQL *LIKE* expressions (e.g. ``%le-Château`` for names ending with
..     "le-Château").

.. _all_method:

Get all localities (no search criteria)
---------------------------------------

Because the data set may be pretty big, the :py:meth:`chzip.ChZip.all` method
returns an iterator.

Use it as following::

    for locality in z.all():
        do_something_with( locality )

If you are looking for a list, then::

    l = list( z.all() )
