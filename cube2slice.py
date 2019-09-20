import numpy as np
import astropy.io.fits as pyfits
import os
infos=open('info.list', 'r').readlines()


for line in infos:
    info = line.split('\n')[0]
    info = info.split(' ')
    satellites = info[3].split(';')
    satellites = [int(i) for i in satellites]
    path = info[0]
    cube = pyfits.getdata(path)
    for i in range(len(cube)):
        if i+1 not in satellites:
            name = '/h/ninou/trainset/detrended_trainset/images/'+ path.split('fits')[0] + str(i) + '.fits'
            pyfits.writeto(name,cube[i],overwrite=True)