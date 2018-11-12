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

Abstract

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

Introduction

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

Requirements

Design 

Architecture

Dataset

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

Implementation

Benchmark

Conclusion

Acknowledgement
