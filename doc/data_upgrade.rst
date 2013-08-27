.. _data-upgrade:

Data upgrade
============

After :ref:`installing <installation>` `chzip`, the ZIP codes and city names are 
already up-to-date.

This data is updated the 2nd of each month [#f1]_. I recommend you to set up a cron job
to never miss one update.

Update automatically using a cronjob
------------------------------------
On UNIX, create a script with the following content::

    #!/usr/bin/env python3
    import chzip
    chzip.upgrade_all()

Make it executable with ``chmod +x my_script.py`` and add this to your cronjobs
with `crontab -e` to update the data every 2nd of the month at 03:04 AM:

.. code-block:: bash

    # m h dom mon dow command
      4 3 2   *   *   /somewhere/my_script.py

If you don't want to create a separate file just for this 
you can also run it with ``python -c 'import chzip; chzip.upgrade_all()'``

.. note::
    The user running the :py:meth:`chzip.ChZip.upgrade_all()` method
    must have permissions to write into the installation folder.
    If you installed this library with your package manager or using
    `sudo`, you will need to be `root` to do that.

.. rubric:: Footnotes

.. [#f1] Swiss Post updates are available on the 1st of the month 
    but the data is valid from the 2nd. It makes almost no difference
    if you get the data one day earlier. By the way, ZIP codes don't
    change often, and if that's the case, the mail will be "redirected"
    to the appropriate location in the meantime. So, don't worry!
