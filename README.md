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
      - <a href="https://github.com/dani-lbnl/techwomen/blob/main/Techwomen2021_lesson1.pdf">[Preprint]</a>
       <p>
      - <a href="https://github.com/dani-lbnl/techwomen/blob/main/Techwomen2021_lesson1.pdf">[Video]</a>
      </td>
 </tr>
</table>

## Datasets:
Temporarily in Google [drive](https://drive.google.com/drive/folders/1Tq9nKdz7W1l-5lFxNvbTPuTV2F1zGi8F?usp=sharing), soon to be on Dryad.

## Codes:
- Feature extraction schemes:
  - [GLCM](https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_glcm.html)
  - [Histogram-based]
  - [LeNet](https://github.com/s-miramontes/ISVC2019)

- AutoML
  - [pyCaret routines](https://pycaret.org/predict-model/)
  - running in a super computer
  
- Metrics  
 

## Abstract:
X-ray scattering is an experimental technique that generates patterns used to provide sub-nanometer structural information about materials, e.g. polymers. In order to capture the diffuse scattering patterns from disordered systems, distinct techniques have been developed: small or wide angle X-ray scattering (SAXS or WAXS) and their respective surface-sensitive variation due to grazing incidence known as GISAXS and GIWAXS. During a single experiment, which are often high-throughput, these different techniques can be used interchangeably. Therefore, screening and analyzing the acquired patterns requires complex processing seldom amenable to manual interaction. This paper proposes camSortXS, a set of computational tools for autonomously sorting X-ray scattering patterns from large image datasets of energy critical materials, imaged using 4 techniques: SAXS, WAXS, GISAXS and GIWAXS. Sorted patterns depend upon deep learning based on TensorFlow and AutoML algorithms. The image dataset includes thousands of patterns from real experiments performed by multiple users from a synchrotron-light beamline. Each scattering pattern undergoes featurization using 8 methods, including different architectures for deep learning, generating a total of 25 possible representations per pattern. These are input to AutoML that creates 5 different classification models per featurization, which are individually evaluated using 7 metrics of performance. Our exploration shows that different architecture choices might lead to similar accuracy rates at diverse computing times. These are promising results toward automating screening of patterns for metadata recovery, and enabling autonomous experiments for film design.



