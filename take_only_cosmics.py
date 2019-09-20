import numpy as np
import astropy.io.fits as pyfits
import os
import glob

allmasks = glob.glob('/h/ninou/trainset/detrended_trainset/images/cosmics_removed/*.cosmics_mask.fits')
i=0

for mask in allmasks:
    i+=1
    mask_split = mask.split('cosmics_removed/')
    file = mask_split[0] + mask_split[1].split('.cosmics_mask')[0] + '.fits'
    
    mask_data = pyfits.getdata(mask)
    data = pyfits.getdata(file)
    
    cosmics = mask_data * data
    
    
    dir = mask_split[0].split("/images")[0] + '/cosmic_rays' + '/cosmic_rays_' + str(i) + '.fits'
    pyfits.writeto(dir, cosmics, overwrite=True)