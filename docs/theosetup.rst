Overview of Simulation Parameter File
=====================================


Below is the printout of an example simulation setup file SISconfig.txt. The file might not be up-to-date and 
the most recent version is in the data directory of the spherex_ices_simulator package.


# SPHEREx Level 4 Ices Pipeline Configuration File
# VT, SAO: 3/24/2023

########################################################
[DEFAULT]
# The home directory can be either ${HOME} or be provided
# with an explicit path.
# home = ${HOME}/SPHEREx/DATA/SISimulator
# data home directory
HOME = /Users/volkertolls
DHOME = /rdat/Projects/SPHEREx/Data/SIS



########################################################
[Directories]
shome = ${DHOME}/SISimulator
workDir = ${DHOME}/work
outpath = ${DHOME}/output

# SPLICES catalog path
splicesFile = /rdat/Projects/SPHEREx/Data/SPLICES/20230428_SPLICES_v7.3_sis.fits

# SPHEREx survey planning file is included in SPHEREx-Sky-Simulator
surveyFile = ${HOME}/git/SPHEREx-Sky-Simulator/py/data/spherex_survey_plan_april_2022.fits

# parsl
max_workers = 1
max_blocks = 4


########################################################
[Simulator]

# Instrument performance: CBE or MEV
Instperf = CBE

avrange = [10.0, 100, 10]
# Av models:
#  only available: G23
AvModel = G23
# Rv
Rv = 3.1

# Number of spectra
n_spectra = 648 

# chunksize for processing in sis_quickcatalog
# best: chunksize is integer fraction of n_spectra
chunksize = 60 

# target selection
selTargets = random

# seed for target random numbers
#  0 means random seed
tseed = 0

# simulation mode:
# 1: SPHEREx Sky Simulator, 2: Ices Simulator (no noise)
simmode = 1

# spectra flux range is pinned to flux0 (in mJy) and the wave0 (in um)
# for whatever the shape of the spectrum is.
# note: saturation is 8, 38, and 42 Jy
# snr=100: 3, 11, 16 mJy in Bands 4, 5, and 6
# default: 3 mJy at 4.0 um
flux0 = 3.0
wave0 = 4.0
funit = mJy
wunit = um


# we have snr values only for a particular band
# also consider Instperf = MEV/CBE above for SNR!
snrband = 5
# snrtype is grid or random
snrtype = grid
# flux range in mJy!
# flrange = [20, 100]
# snrrange is [start, end, step]
snrrange = [100, 200, 50]
# snr=50: 
# snr=100: 
# saturation: 
contR = []


# Line Emission
H-lines = True
#
H2-lines = True
#
CO-Lines = True
# max. amplitude as factor of continuum
CO-ampl = 0.25
# available is grid of CO simulations
# r: random
CO-model = 'r'


# Scattering Peak
enableScattering = True
# max. scattering amplitude as factor of continuum
scatampl = 0.1
# scattering peak base width in um
scatwidth = 0.15


# Stellar models
# available: O, B, A, F, G, K
# missing: M
# stmodels = [F, G, K]
# grid ranges are [start, end, step]
# random range: step is ignored
st_teff = [3500, 6000, 500]
st_logg = [4.5]
st_z    = [0.0]
stpath = /rdat/Projects/SPHEREx/Data/Simulator_Data/sim_stellar_models/SPHEREx_Ices_sim_stellar_models_v3.0.npz



# save primary catalot if name provided (do not comment out next line!)
primcatname = None
# primcatname = 'my_primary_catalog_name

# save secondary catalog if name provided (do not comment out next line!)
seccatname = None
# seccatname = 'my_secondary_catalog_name


########################################################
# Ices: pure theoretical absorption features
[Theoretical]
enableTheo = False
# type can be Gaussian, Lorentzian, or both
thtype = Gaussian
# features can be: 
#   1: H2O, 2:CO2, 3:XNC, 4:CO, 5:OCS, 6:NH3, 7:CH3OH
thfeatures = [1, 2, 3, 4, 5]

# taus (primary if provided) or tau range
taus = [0.0, 0.5, 1, 2, 4, 8]
#trange = [0.0, 8.0, 1.0]

# an example file is in the module's data directory
thparfile = ''
# this parameter overwrites the (single) parameter in the ices parameter file
# if not present, the parameter in the file is use
h2oasymrange = [0.0, 0.4, 0.1]

########################################################
# observed spectra
[Observed]
enableJWST = False
enableISO = False
enableAKARI = False
# other groupd ground-based observations
enableOther = False


########################################################
# Laboratory spectra
[Lab]
enableLab = False
speciesSelection = []

 