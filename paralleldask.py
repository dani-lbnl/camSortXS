from glob import glob
from distributed import Client, LocalCluster

from pycaret.utils import version
#version()

import pandas as pd
from glob import glob
from sklearn.preprocessing import StandardScaler
from pycaret.classification import *
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score,cohen_kappa_score,matthews_corrcoef
from sklearn.decomposition import FastICA, PCA
import numpy as np
from time import time
import os
import dask

dask.config.set({'temporary_directory':'/global/cscratch1/sd/ushizima/TonyHey/'})
path = '/global/cfs/cdirs/als/users/dushizima/danixray/TonyHey/classic/'

def func(tup):
    index, file_f, file_l = tup

    out_success = path+'results/res_'+file_f.split('/')[-1]
    success_file = out_success + ".s"

    # file already computed skip
    if os.path.exists(success_file):
        return

    models = ['et','lightgbm','xgboost','rf','catboost'] #see above
    cont_frame = index * len(models)

    metrics = ['file','classifier','accuracy','accuracy_std','recall','recall_std','precision','precision_std','f1','f1_std',
               'kappa','kappa_std','matthews_corrcoef','matthews_corrcoef_kappa','time']
    results = pd.DataFrame(columns = metrics)
    #normalize_frame
    feat = pd.read_csv(file_f,header=None,dtype=float)
    label = pd.read_csv(file_l,header=None)
    data = pd.DataFrame(StandardScaler().fit_transform(feat)) #standardize

    #pca

    ica = PCA(n_components=5)#FastICA(n_components=5,max_iter=210)
    principalComponents = ica.fit_transform(data)  #reconstruct
    icaDf = pd.DataFrame(data = principalComponents, columns = ['pc1','pc2','pc3','pc4','pc5'])

    #fix dataframe
    label.columns = ['label']
    icaDf['label'] = label['label']
    icaDf.label.replace([0,1,2,3], ['WAXS','GISAXS','GIWAXS','SAXS'], inplace=True)

    for model in models: #run each model
        out_success = path+'results/res_'+file_f.split('/')[-1]

        print(model)
        acc = []
        recall = []
        precision = []
        f1 = []
        kappa = []
        matthews = []
        time_ = []
        for i in range(1):#run a model 10 times
            #shuffle the data
            time_ini = time()
            clf1 = setup(icaDf, target = 'label', log_experiment=False, experiment_name=file_l, silent=True,n_jobs=10,verbose=False,train_size=0.5) #

            #create classifier instance, tunning and predict
            classifier = create_model(model,verbose=False)
            tuned = tune_model(classifier,verbose=False,optimize = 'F1')
            pred_holdouts = predict_model(tuned,verbose=False)
            time_end = time()
            time_.append(time_end-time_ini)
            #computing metrics
            acc.append(accuracy_score(pred_holdouts['label'],pred_holdouts['Label']))
            recall.append(recall_score(pred_holdouts['label'],pred_holdouts['Label'],average='macro'))
            precision.append(precision_score(pred_holdouts['label'],pred_holdouts['Label'],average='weighted'))
            f1.append(f1_score(pred_holdouts['label'],pred_holdouts['Label'],average='micro'))
            kappa.append(cohen_kappa_score(pred_holdouts['label'],pred_holdouts['Label']))
            matthews.append(matthews_corrcoef(pred_holdouts['label'],pred_holdouts['Label']))

        #Save metrics after 10 runs
        results.loc[cont_frame] = [file_f,model,np.mean(acc),np.std(acc),np.mean(recall),np.std(recall),np.mean(precision),
                           np.std(precision),np.mean(f1),np.std(f1),np.mean(kappa),np.std(kappa),np.mean(matthews),
                           np.std(matthews),np.mean(time_)]
        cont_frame += 1
    #ensembled_models = compare_models(whitelist = models(type='ensemble').index.tolist(), fold = 3)
    print(path+'results/res_'+file_f.split('/')[-1])
    results.to_csv(path+'results/res_'+file_f.split('/')[-1], index=True)

    # write success file in end
    out_s = open(success_file,'w')
    out_s.write('1')
    out_s.close()



def main():
    scheduler = LocalCluster(n_workers=8,threads_per_worker=1)
    client = Client(scheduler)
    files_features = glob(path+'*feature_vectors_*.csv')
    files_labels = [i.replace('feature_vectors_','labels_')for i in files_features]


    # generate list of tasks
    list_of_tasks = list(zip(range(len(files_features)), files_features,files_labels))
    #list_of_tasks = list_of_tasks[0:11] #debugging
    result = client.map(func, list_of_tasks)


    # blocking
    client.gather([result])
