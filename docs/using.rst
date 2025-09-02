*******************************
SPHEREx_Ices_Simulator Cookbook
*******************************

This cookbook provides instructions about how to use the SPHEREx_Ices_Simulator
python package.


Basic instructions
==================

The simplest use case for the `SPHEREx_Ices_Simulator` package is executing it in demo mode. From the command line execute just::

   >>>execSIS -d 2
   
   or
   
   >>>execSIS -d 1

This will execute the simulator by simulating observations with a default set of Gaussian absorption features. The difference 
between the 2 demo mode is that demo mode "-d 2" uses the SPHEREx Sky Simulator to downsample the spectrum and demo mode "-d 1"
uses a build-in downsampler. The second downsampler uses the SPHEREx spectral element bandpasses, but no instrument noise, zodi, 
etc according to the current observation and instrument models are added to the spectrum. The advanced use is described in the 
next sections.

Advanced usage
==============

The SPHEREx Ices Simulator (SIS) has several operational modes and additional modes will be added in the future if required. The 
current modes are:

Mode 1:

   Creating a set of simulated spectra with random parameters.

Mode 2:

   Creating a set of simulated spectra from a parameter grid.

Mode 3:

   Creating simulated spectra from JWST spectra. - TBI




vtcloud, 6/26/2023
