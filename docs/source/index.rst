.. gramfuzz documentation master file, created by
   sphinx-quickstart on Sun Dec 11 23:19:53 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

imagetext - Saving and reading data visually from images
====================================

imagetext allows one to save and read text (visually) to/from an
image.

Installation
^^^^^^^^^^^^

imagetext is available on PyPI and can be installed via pip!

.. code-block:: bash

   pip install imagetext


.. _tldr_example:

TLDR Example
^^^^^^^^^^^^


Writing to Images
-----------------

Suppose we want to save the data "HELLO WORLD" into an image as
visual characters:

.. code-block:: python

    import imagetext

    data = "HELLO WORLD"
    output_path = "test.png"
    imagetext.create(data=data, dest=output_path)

That's it!

Below is what the resulting ``test.png`` file looks like:

Reading from Images
-------------------

Now let's read ``HELLO WORLD`` back out of the image:

.. code-block:: python

   import imagetext

   output_path = "test.png"
   data = imagetext.read(output_path)
   print(data) # prints HELLO WORLD

Stand-Alone Script
------------------

``imagetext`` also provides a standalone script:

.. code-block:: text
   blah blah blah

imagetext Reference Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: imagetext
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
