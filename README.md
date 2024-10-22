# camSortXS
Deep learning and autoML routines and applications to X-ray data
http://bit.ly/camSortXS


<table border="0">
 <tr>
    <td><a href"http://bit.ly/camSortXS"><img src="https://github.com/dani-lbnl/camSortXS/blob/main/camSortXS.png" width="600"></a>
<p>     camSortXS
    </td>
    <td>
       <p>
        camSortXS is a set of routines for autonomously sort X-ray scattering patterns from large image datasets of energy critical materials, imaged using 4 techniques: SAXS, WAXS, GISAXS and GIWAXS. Sorted patterns depend upon deep learning based on TensorFlow and AutoML algorithms. The image dataset includes thousands of patterns from real experiments performed by multiple users from a synchrotron-light beamline. Each scattering pattern undergoes featurization using 8 methods, including different architectures for deep learning, generating a total of 25 possible representations per pattern. These are input to AutoML that creates 5 different classification models per featurization, which are individually evaluated using 7 metrics of performance. 
       <p>
      - <a href="https://github.com/dani-lbnl/camSortXS/blob/main/MDPI_Journal_of_Imaging_2020_ushizima.pdf">[Preprint]</a>
       <p>
      - <a href="https://www.american-cse.org/static/2021-CSCE-BOOKLET-with-cover.pdf">[Proceedings]</a>
      </td>
 </tr>
</table>

## Datasets:
Temporarily in Google [drive](https://drive.google.com/drive/folders/1Tq9nKdz7W1l-5lFxNvbTPuTV2F1zGi8F?usp=sharing), soon to be on Dryad.

## Codes (full camSortXS toolset will be available upon acceptance):
These are key parts of camSortXS that will allow to understand adopted strategies and results described in paper submitted to J. of Imaging in Jan 2021

- Feature extraction schemes:
  - [GLCM](https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_glcm.html)
  - [Histogram-based](https://github.com/dani-lbnl/camSortXS/blob/main/histogram.py)
  - [LeNet](https://github.com/dani-lbnl/camSortXS/blob/main/train_lenet.ipynb)
  - Deeper CNNs: [[docs]](https://keras.io/api/applications)

- AutoML
  - pyCaret routines: [[our routine w/ dask]](https://github.com/dani-lbnl/camSortXS/blob/main/paralleldask.py) [[docs for LightGBM, XGBoost, Random Forest, Extra trees, Catboost]](https://pycaret.org/predict-model/)
  - running in a super computer [[queue]](automl_nersc_job.q) 
  - Metrics  

- GradCAM via Keras
 - [[our implementation]](https://github.com/dani-lbnl/camSortXS/blob/main/grad_cam_activation_map.ipynb)
 - [[docs]](https://keras.io/examples/vision/grad_cam/)

## Abstract:
X-ray scattering is an experimental technique that generates patterns used to provide sub-nanometer structural information about materials, e.g. polymers. In order to capture the diffuse scattering patterns from disordered systems, distinct techniques have been developed: small or wide angle X-ray scattering (SAXS or WAXS) and their respective surface-sensitive variation due to grazing incidence known as GISAXS and GIWAXS. During a single experiment, which are often high-throughput, these different techniques can be used interchangeably. Therefore, screening and analyzing the acquired patterns requires complex processing seldom amenable to manual interaction. This paper proposes camSortXS, a set of computational tools for autonomously sorting X-ray scattering patterns from large image datasets of energy critical materials, imaged using 4 techniques: SAXS, WAXS, GISAXS and GIWAXS. Sorted patterns depend upon deep learning based on TensorFlow and AutoML algorithms. The image dataset includes thousands of patterns from real experiments performed by multiple users from a synchrotron-light beamline. Each scattering pattern undergoes featurization using 8 methods, including different architectures for deep learning, generating a total of 25 possible representations per pattern. These are input to AutoML that creates 5 different classification models per featurization, which are individually evaluated using 7 metrics of performance. Our exploration shows that different architecture choices might lead to similar accuracy rates at diverse computing times. These are promising results toward automating screening of patterns for metadata recovery, and enabling autonomous experiments for film design.

## Future work:
[LabelMaker](https://github.com/ahexemer/LabelMaker)
