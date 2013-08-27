Preface
=======

The Issue
---------

The Swiss Postal Service provides a list of zip codes with the associated
locality names. This is great, but to use it one would have to download
the tab-delimited text file, convert it to a format easily accessible with
Python. After that one would have to figure out the format of the data
and what are all the fields for. 

Most people having the need to look for
zip codes and locality names would do it as simple as possible, ending
with something hard to understand and not easily re-usable. They would
probably not implement something such as automatic unpacking and updating
and keep obsolete data in a database, which could lead to serious problems.

More importantly they would have lost a lot of time parsing a 
stupidly formatted file instead of spending more time on their work
or with their friends, their family, their pets or taking care of
them.

The Goal
--------

The goal of this project is to avoid every Python programmer in
Switzerland who need this data to figure out how to use it and
implement a custom solution from scratch.

This library has been developed with its users in mind, and I am
looking forward for your feedback and your usecases.

The most important thing I would like to archive is that you can
install chzip and look for locality names associated with a zip code
under a minute. Look at the :ref:`usage` page and try this thing out,
then tell me if I have succeeded.
