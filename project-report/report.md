Morphological Image-based Profiling Dataset of Cells for Scientific Community :hand: fa18-523-52

| Anna Heine
| avheine@iu.edu
| Indiana University
| hid: fa18-523-52
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-523-52/blob/master/project-report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/fa18-523-52/tree/master/project-code)

---

Keywords:
fa18-532-52, lesion, medical

---

## Abstract

One major area that is being utilized highly today within big data platforms is
that of medical image collection. Medical image datasets are often used as 
training tools as a source of comparison when analyzing diagnostic images from
current or past cases of diseases. The issue in this field is that current 
datasets lack the diversity and number of samples that is necessary to make
sufficient predictions based on analysis. With valuable datasets, medical 
advances can be made to deliver more personalized medicine, to create predictive
diagnostic models, research treatment methods, improve the overall value of 
healthcare, and much more. The main goal of medical big data analysis is to find
associations and correlations within complex data. The HAM10000 dataset is a 
significant resource for analysis because it includes over 10,000 dermatoscopic 
images that have been carefully stained and optimized to display skin-lesion 
biopsies. The grafts entered into this dataset were verified and therefore proven
worthy based on expert consensus, a follow-up, and in-vivo microscopy. Each 
individual donation is tracked by its patient identification number, image 
identification number, donor age, donor sex, localization on the body, and a 
final inclusion reasoning. 

## Introduction

The big data revolution has changed multiple industries around the world, one of
which largely includes the field of medicine. The role of big data in the medical 
sector is high-grade as it aims to be predictive in order to diagnose patients and
even discover new treatment methods. This means that the data obtained and used in 
these models must be wide enough to include a variety of patients and diseases. 
Disease is a major unknown for many reasons in medicine. Big data has recently been
shown to be beneficial in disease management as it provides aggregate information 
around multiple aspects of a disease. For example, some datasets include functionality
and characteristics of DNA and RNA, proteins, cell types, tissues, organs, and more
[@fa18-523-52-intro]. The ability for these models to evolve and grow are what will 
advance the predictive analysis so desired in the field today. The sources of big data 
are varied. Some of which include administrative claim records, electronic health
records, the internet, medical imaging, and clinical trials [@fa18-523-52-ncbi]. 

Despite the vast number of sources, medical big datasets can be quite different than 
other types of big data. The main difference is located in the form of accessing the 
data. Because of privacy laws and ethical stances, some medical data is hard to come by.
The fact that data has been breached in other industries such as in business and 
consumerism models, most people are hesitant to include large amounts of people's private
health records in one location. That being said, medical datasets have to be managed so 
that the records being added follow a specific, structured protocol. These datasets are 
also costly, as they may need to be examined and measured multiple times by trained 
personnel to ensure correctness. The nature of the data is therefore, dangerously 
susceptible to human error, as most of it usually contains information we are not very 
sure about to begin with. Although data scientists have found methods and reasonings that
allow for the production of medical datasets, they are often unreliable because the amount
of data contained is just too small to make any valuable inferences or claims. 

Though there are many challenges medical big data will need to dissolve in order to gain
popularity and trust, the field is already proven to hold valuable insights. For example,
the field will expand the use of big data into other industries by providing a basis for 
accumulating data of various sources and materials. Medical big data can provide answers
to uncertainties even when lacking substantial evidence. The influx of continued large 
medical datasets is contributing to the advance of trusted future predictive healthcare
learning models. The overall goal is not to automate the position of a trained physician,
but to make the diagnostic process much easier and more efficient as well as aid in 
several areas of medical research. 

The realm of skin cancer research is more or less crying out for big data analysis.
Melanoma, specifically, affects around 73,000 new people each year which will result in
about 9,000 deaths [@fa18-523-52-digital]. There is no general biomarker for melanoma, which 
causes for imprecise diagnostic margins. With this prelavence of disease in society, the 
amount diagnoses per melanoma skin lesion sometimes reaches up to 36 because of 
false-negative uncertainties [@fa18-523-52-digital]. However, with big datasets and the use
of computer algorithms, there has been a significant increase in diagnostic accuracy -less 
than 5% error rates. 

## Requirements

## Design 

## Architecture

Before I made any implementations on this project, I realized that I would be using
multiple software packages. Therefore, I wanted to ensure that they were all in the
same place. To do this, I installed Anaconda. Anaconda is an open-source, free
distribution software with Python and R available packages already installed. It's 
main purpose is to provide simple tracking of these packages with an easy, user-friendly
dashboard design[@fa18-523-52-conda]. Each version of its packages are managed by its
package management system, Conda. In Anaconda, I used Jupyter and Jupyter Notebook to 
perform most of my data analysis. Jupyter allows for data manipulation across many 
programming languages. Jupyter is also an open-source web application that allows for 
distribution of documents, code, and other projects for collaboration. It has many uses:
data cleansing, statistical data modeling, visualization, machine and deep learning, data
transformation, and more. Once a project has been created, your work can be output as HTML,
images, video, or LaTeX[@fa18-523-52-jupyter]. The Notebook specifically can contain both 
code and text. These formats have the ability to create descriptions and visible output for
graphs of many types. Jupyter runs via client-server, which means it does not need Internet
access to be run. Each notebook contains a kernel which controls the execution of the code
inside it. For example, if you wanted to execute Python code, the notebook would execute
via the ipython kernel. To manually execute a file, the user must either choose to run 
each cell one at a time by clicking Run on the left of each line or by cliking on Run All
in the Cell menu[@fa18-523-52-jupyterNotebook].

NumPy is a package that interacts with Python to provide numerical operations. NumPy uses
its own defined library to make things like arrays and matrices and invoke operations on 
them. The most basic object in NumPy is the ndarray object. The ndarray holds arrays of 
homogeneous data types which are compiled for efficiency. NumPy arrays have a fixed size
array and are homogeneous, which is different from regular Python arrays. NumPy also has
vectorized and broadcasting behavior which both work to amplify performance and decrease
compile time. Vectorized code is simple and easy to read code that typically is prone to 
less bugs. The code sometimes is mistaken for mathematical notations, but of course, 
results in Python-looking code. Broadcasting describes the step-by-step behavior of 
operations. It is beneficial in taking the outer operation of two arrays to make a combined
array. However, both arrays must be of same dimension[@fa18-523-52-numPy].



talk about pandas






## Installation
To install Jupyter itself you must already have Python 2.7 or Python 3.3 or greater. It
is recommended to go ahead and download Anaconda, like I did, so that all of your packages 
are in one place. To download the latest version of Anaconda, follow the code below:
```python
import webbrowser
webbrowser.open('https://www.anaconda.com/download/')
```

From there, you will have to choose which operating system to download from. That is all 
you have to do to install Anaconda. You know have an open platform with many packages 
for use. One of these packages is Jupyter Notebook. To run Jupyter Notebook the following
line into the command prompt:
```bash
jupyter notebook
```
Now you can begin using Jupyter's Notebook to create visuals and write code for that
manipulates your data. NumPy and Pandas are also automatically downloaded with the latest
version on Anaconda. 

## Dataset

The dataset I have chosen is often used in training tools for medical
professionals and is one of the only few available skin lesion datasets. The HAM10000 
(Human Against Machine with 10000 training images) dataset contains dermatoscopic images
from different populations that include all general diagnostic categories that have been 
discovered in this type of medicine. The diagnostic categories in this dataset include
diseases such as: Bowen's disease (akiec), basal cell carcinoma (bcc), benign keratosis-
like lesions (bkl), dermatofibroma (df), melanoma (mel), melanocytic nevi (nv), and 
vascular regions (vasc). The confirmation of the samples that were entered into the 
dataset are given: histopathology (histo), follow-up examination (follow_up), expert 
consensus (consensus), or confirmation via in-vivo confocal microscopy (confocal). Each
image within the dataset can be tracked by their lesion-id [@fa18-523-52-harvard].

## Implementation

## Benchmark

## Conclusion

## Acknowledgement
