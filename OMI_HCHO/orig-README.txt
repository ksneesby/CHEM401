
EXAMPLE WORKFLOW:


1) run the creation script for a month (takes around an hour) with this code:
./regrid_month 2005 1
2) check the output is created in Data folder
3) write a script which analyses the output - for example:
python3 example_regrid_swaths.py


0) pre-requisites: probably need to set up the right python environment
I'm using python3 and several NCI modules: 
    hdf5
    hdf-eos
    python3/3.5.2
    python3/3.5.2-matplotlib
    netcdf/4.2.1.1
It looks like I'm using these python packages:
    h5py
    pandas
    numpy
    basemap
    

MAIN SCRIPT: regrid_swaths.py 
contains a bunch of methods which take OMI satellite swaths, and MODIS fires, and grids them into daily averages at whatever resolution you want

The resolution can be re-set in the 'globals' section of the script
Currently it's set at .25x.3125 - and takes around 45 mins to run for one day

EXAMPLE SCRIPT: example_regrid_swaths.py
shows how to use the methods in regrid_swaths.py for reading and plotting one or multiple days of data

NCI RUNNING Scripts:
regrid_day.sh
    Runs the regrid_swaths.py methods  to produce a single day of regridded omi swaths and fires

regrid_month.sh
    Runs 31 instances of regrid_day.sh on the queue

