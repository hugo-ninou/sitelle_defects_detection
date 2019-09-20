import tensorflow as tf
import numpy as np
import astropy.io.fits as pyfits
import os
import detrend


filters=['C1','C2','C4','SN1','SN2','SN3']
dir = '/h/ninou/trainset/'
    
    
def detrend_trainset():
    for filter in [filters[-1]]:
        
        list_list_data = open(dir + filter + '_trainset.list', 'r').readlines()
        
        flat_cam1 = dir + list_list_data[0].split('\n')[0]
        flat_cam2 = dir + list_list_data[1].split('\n')[0]
        flat_files = ( flat_cam1, flat_cam2 )
        
        print(filter)
        step=1
        for list_data_str in list_list_data[2:]:
            print('step=',step)
            list_data = dir + list_data_str.split('\n')[0]
            c = detrend.cube(list_data, flat_files)
            name = list_data.split('/')[-1]
            name = name.split('.')[0]
            c.export('/h/ninou/trainset/detrended_trainset/' + name)
            step+=1