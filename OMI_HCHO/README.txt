Modified version of JWG original README specific to Kate's needs

EXAMPLE WORKFLOW:

0) pre-requisites: probably need to set up the right python environment
It looks like I'm using these python packages in Python 3:
    h5py
    pandas
    numpy
    basemap
    

1) check the required output is created in Data folder
2) write a script which analyses the output - for example:
python3 example_regrid_swaths.py


MAIN SCRIPT: regrid_swaths.py 
contains a bunch of methods which take OMI satellite swaths, and MODIS fires, and grids them into daily averages at whatever resolution you want

  The resolution can be re-set in the 'globals' section of the script
  Currently it's set at .25x.3125 - and takes around 45 mins to run for one day

You won't need those. But it also contains methods you will use like reading the regridded files and plotting a map

EXAMPLE SCRIPT: example_regrid_swaths.py
shows how to use the methods in regrid_swaths.py for reading and plotting one or multiple days of data
