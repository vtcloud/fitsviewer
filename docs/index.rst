<<<<<<< Upstream, based on branch 'master' of https://github.com/vtcloud/SPHEREx_Ices_Simulator
SPHEREx_Ices_Simulator
===============

The purpose of the SPHEREx_Ices_Simulator is to create simulated SPHEREx Ices spectra similar to what we currently expect the SPHEREx mission will observe. The source of the high spectral resolution input spectra include existing observations like from JWST, ISO, etc with spctral resolutions exceeding the highest SPHEREx spectral resolution of 130 in Band 6. In addition, the simulator will create fully artificial spectra with Gaussian absorption features for which tau, absorption width, column densities, and other parameters are fully known. Another source is the combination of high-spectral resolution laboratory spectra.

The rough steps to create the simulated spectra are (with obvious variations for the different aforemention origins of the spectra):

1.) Create a high spectral resolution wavelength grid;
2.) Insert the desired ice absorption features in a corresponding tau-array with all entries equal 1;
3.) Apply an extincted continuum to the spectrum from 2;
4.) Spectrally Downsample the spectrum from 3.) to the SPHEREx spectral elements.



Documentation
-------------

.. toctree::
    :maxdepth: 2

    installing.rst
    using.rst

Reporting issues and getting help
---------------------------------

Please help us improve this package by reporting issues via 
`GitHub <https://github.com/vtcloud/SPHEREx_Ices_Simulator/issues>`_. 
You can also open an issue if you need help with using the package.

Developers
----------

This package was developed by:

* Volker Tolls

=======
Documentation
-------------

.. toctree::
    :maxdepth: 2

    installing.rst
    using.rst
    theory.rst
    source/readme.rst
    source/packages/modules.rst
    contributing.rst
    conduct.rst
    changelog.rst
    autoapi/index

Reporting issues and getting help
---------------------------------

Please help us improve this package by reporting issues via 
`GitHub <https://github.com/vtcloud/SPHEREx_Ices_Simulator>`_. 
You can also open an issue if you need help with using the package.

Developers
----------

This package was developed by:

* Volker Tolls
>>>>>>> 4f384fe documents updates

