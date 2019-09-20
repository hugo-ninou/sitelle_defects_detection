import numpy as np
import astropy.io.fits as pyfits
import os
import astroscrappy
import glob

allfiles = glob.glob('/h/ninou/trainset/detrended_trainset/images/*.fits')

for file in allfiles:
    data = pyfits.getdata(file)
    
    max_data = np.max(data)
    indata = data * (data > -500) + max_data * (data <= -500)
    
    mask_bool, clean_data = astroscrappy.detect_cosmics(indata)
    mask = 1*mask_bool
    
    file = file.split('images')
    pyfits.writeto(file[0]+ 'images'+ '/cosmics_removed'+ file[1], clean_data, overwrite=True)
    pyfits.writeto(file[0]+ 'images'+ '/cosmics_removed'+ file[1].split('.fits')[0]+ '.cosmics_mask'+ '.fits', mask, overwrite=True)
    