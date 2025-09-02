=======
Installing `SPHEREx_Ices_Simulator`
============================

Requirements
------------

This package has the following dependencies:

* `Python <http://www.python.org>`_ 3.8
* `Numpy <http://www.numpy.org>`_ 1.19 or later
* `Astropy <http://www.astropy.org>`__ 4.0 or later
* `scipy <https://www.scipy.org>`__ 1.7 or later
* `sphinx`__ 3.2 or later
* `myst-parser`__ 0.16 or later
* `readthedocs-sphinx-search`__ 0.1.1 or later
* `argparse`__ 1.4 or later`
* `SPHEREx-Sky-Simulator`

Installation
------------

Currently, the only path to install the `SPHEREx_Ices_Simulator` package is
from the git repositor (you must be logged-in)::

    git clone https://github.com/vtcloud/SPHEREx_Ices_Simulator.git
    cd SPHEREx_Ices_Simulator
    pip install .

If editing of the package content is required, install with::

    git clone https://github.com/vtcloud/SPHEREx_Ices_Simulator.git
    cd SPHEREx_Ices_Simulator
    pip install -e .

###### Alternate installation or updating method:

You can also install the latest developer version in a single line with pip.
However, there might be a few adjustments to be made in order for the
program to work correctly,- see Installation::

    pip install git+https://github.com/vtcloud/SPHEREx_Ices_Simulator.git
