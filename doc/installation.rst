.. _installation:

Installation
============

The recommended installation method is `pip <http://www.pip-installer.org/>`_::

    pip install chzip

This will automatically install the library and download all the resources files 
required by this library. It can also be done manually at anytime::

    import chzip
    chzip.download_and_unpack_all(download_dir)

.. warning::

    :py:meth:`chzip.ChZip.download_and_unpack_all` erases previous versions of the
    files before beginning, which can result in the absence of files if the download
    or unpacking process fails. For this reason, you should always use 
    :py:meth:`chzip.ChZip.upgrade_all` instead.

.. note::

     For `many reasons <http://stackoverflow.com/a/3220572/753136>`_ I do not plan
     to make an egg for `easy_install`. But feel free to do it :-)
