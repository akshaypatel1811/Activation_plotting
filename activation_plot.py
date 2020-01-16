# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:11:45 2019

@author: Admin
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def read_Plot(filename='subject01_5mps_activations_ankleAssist.dat'):
    read = open(filename, 'r')
    for i in range(3):
        line=read.readline()
    line = read.readline()
    if line.isspace() == True:
        line = read.readline()

    Data_labels = line.split('\t')
    #data
    data = []
    for j in range(len(Data_labels)):
        data.append([])
    for l in read.readlines():
        d = [float(x) for x in l.split()]
        for i in  range(len(Data_labels)):
            data[i].append(d[i])  
    #print(np.add(data[Data_labels.index('time (% gait cycle)')],data[Data_labels.index('time (% gait cycle)')]))         
    Data_labels.append('R_hip_abd')
    data.append(np.mean([data[Data_labels.index('glut_max1_r')],
                            data[Data_labels.index('glut_med1_r')],
                            data[Data_labels.index('glut_med2_r')],
                            data[Data_labels.index('glut_med3_r')],
                            data[Data_labels.index('glut_min1_r')],
                            data[Data_labels.index('glut_min2_r')],
                            data[Data_labels.index('glut_min3_r')],
                            data[Data_labels.index('peri_r')],
                            data[Data_labels.index('sar_r')],
                            data[Data_labels.index('tfl_r')]],axis=0))
    Data_labels.append('R_hip_flex')
    data.append(np.mean([data[Data_labels.index('add_brev_r')],
                             data[Data_labels.index('add_long_r')],
                             data[Data_labels.index('glut_med1_r')],
                             data[Data_labels.index('glut_min1_r')],
                             data[Data_labels.index('grac_r')],
                             data[Data_labels.index('iliacus_r')],
                             data[Data_labels.index('pect_r')],
                             data[Data_labels.index('psoas_r')],
                             data[Data_labels.index('rect_fem_r')],
                             data[Data_labels.index('sar_r')],
                             data[Data_labels.index('tfl_r')]],axis=0))
    Data_labels.append('R_hip_inrot')
    data.append(np.mean([data[Data_labels.index('glut_med1_r')],
                              data[Data_labels.index('glut_min1_r')],
                              data[Data_labels.index('iliacus_r')],
                              data[Data_labels.index('psoas_r')],
                              data[Data_labels.index('tfl_r')]],axis=0))
    Data_labels.append('R_hip_exrot')
    data.append(np.mean([data[Data_labels.index('gem_r')],
                              data[Data_labels.index('glut_med3_r')],
                              data[Data_labels.index('glut_min3_r')],
                              data[Data_labels.index('peri_r')],
                              data[Data_labels.index('quad_fem_r')]],axis=0))
    Data_labels.append('R_hip_ext')
    data.append(np.mean([data[Data_labels.index('add_long_r')],
                             data[Data_labels.index('add_mag1_r')],
                             data[Data_labels.index('add_mag2_r')],
                             data[Data_labels.index('add_mag3_r')],
                             data[Data_labels.index('bifemlh_r')],
                             data[Data_labels.index('glut_max1_r')],
                             data[Data_labels.index('glut_max2_r')],
                             data[Data_labels.index('glut_max3_r')],
                             data[Data_labels.index('glut_med3_r')],
                             data[Data_labels.index('glut_min3_r')],
                             data[Data_labels.index('semimem_r')],
                             data[Data_labels.index('semiten_r')]],axis=0))
    Data_labels.append('R_hip_add')
    data.append(np.mean([data[Data_labels.index('add_brev_r')],
                             data[Data_labels.index('add_long_r')],
                             data[Data_labels.index('add_mag1_r')],
                             data[Data_labels.index('add_mag2_r')],
                             data[Data_labels.index('add_mag3_r')],
                             data[Data_labels.index('bifemlh_r')],
                             data[Data_labels.index('grac_r')],
                             data[Data_labels.index('pect_r')],
                             data[Data_labels.index('semimem_r')],
                             data[Data_labels.index('semiten_r')]],axis=0))
    Data_labels.append('R_Knee_bend')
    data.append(np.mean([data[Data_labels.index('bifemlh_r')],
                             data[Data_labels.index('bifemsh_r')],
                             data[Data_labels.index('grac_r')],
                             data[Data_labels.index('lat_gas_r')],
                             data[Data_labels.index('med_gas_r')],
                             data[Data_labels.index('sar_r')],
                             data[Data_labels.index('semimem_r')],
                             data[Data_labels.index('semiten_r')]],axis=0))
    Data_labels.append('R_Knee_ext')
    data.append(np.mean([data[Data_labels.index('rect_fem_r')],
                             data[Data_labels.index('vas_int_r')],
                             data[Data_labels.index('vas_lat_r')],
                             data[Data_labels.index('vas_med_r')]],axis=0))
    Data_labels.append('R_ankle_pf')
    data.append(np.mean([data[Data_labels.index('flex_dig_r')],
                             data[Data_labels.index('flex_hal_r')],
                             data[Data_labels.index('lat_gas_r')],
                             data[Data_labels.index('med_gas_r')],
                             data[Data_labels.index('per_brev_r')],
                             data[Data_labels.index('per_long_r')],
                             data[Data_labels.index('soleus_r')],
                             data[Data_labels.index('tib_post_r')]],axis=0))
    Data_labels.append('R_inverter')
    data.append(np.mean([data[Data_labels.index('ext_hal_r')],
                             data[Data_labels.index('flex_dig_r')],
                             data[Data_labels.index('flex_hal_r')],
                             data[Data_labels.index('tib_ant_r')],
                             data[Data_labels.index('tib_post_r')]],axis=0))
    Data_labels.append('R_ankle_df')
    data.append(np.mean([data[Data_labels.index('ext_dig_r')],
                             data[Data_labels.index('ext_hal_r')],
                             data[Data_labels.index('per_tert_r')],
                             data[Data_labels.index('tib_ant_r')]],axis=0))
    Data_labels.append('R_everter')
    data.append(np.mean([data[Data_labels.index('ext_dig_r')],
                             data[Data_labels.index('per_brev_r')],
                             data[Data_labels.index('per_long_r')],
                             data[Data_labels.index('per_tert_r')]],axis=0))
    data_r=[]
    for m  in range(len(data[Data_labels.index('R_hip_abd')])):
        data_r.append([data[Data_labels.index('R_hip_abd')][m],
                            data[Data_labels.index('R_hip_flex')][m],
                            data[Data_labels.index('R_hip_inrot')][m],
                            data[Data_labels.index('R_hip_exrot')][m],
                            data[Data_labels.index('R_hip_ext')][m],
                            data[Data_labels.index('R_hip_add')][m],
                            data[Data_labels.index('R_Knee_bend')][m],
                            data[Data_labels.index('R_Knee_ext')][m],
                            data[Data_labels.index('R_ankle_pf')][m],
                            data[Data_labels.index('R_inverter')][m],
                            data[Data_labels.index('R_ankle_df')][m],
                            data[Data_labels.index('R_everter')][m]])
                    
       
    df=pd.DataFrame(data=data_r,columns=['R_hip_abd',
                                         'R_hip_flex',
                                         'R_hip_inrot',
                                         'R_hip_exrot',
                                         'R_hip_ext',
                                         'R_hip_add',
                                         'R_Knee_bend',
                                         'R_Knee_ext',
                                         'R_ankle_pf',
                                         'R_inverter',
                                         'R_ankle_df',
                                         'R_everter'])
    print("Correlation between each other")
    print(df.corr())
    from pandas.plotting import scatter_matrix
    scatter_matrix(df,figsize=(10,10))
    plt.savefig("fig1.jpg")    
        
  
    read.close()    