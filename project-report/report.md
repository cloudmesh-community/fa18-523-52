# Morphological Image-based Profiling of Skin Lesions for Scientific Community :hand: fa18-523-52

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
are varied. Some of which include administrative claim records, health
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

This project requires Python 2.7 or greater to integrate the Pandas and NumPy packages. It 
requires at least 420 KB of storage to hold the HAM10000 dataset. The project also 
requires the Anaconda platform to access Jupyter Notebook with Numpy and Pandas packages 
installed. The cloud service analytics were performed on KNIME's Cloud Analytics Platform. 

## Design 

The design of the project was to obtain the dataset and test it on a web services.
First, we tested the dataset on Jupyter Notebook to get a baseline of the components.
After creating some visualizations, we then incorporated the data into KNIME's Analytics Cloud 
Platform.

## Architecture

Before we made any implementations on this project, we realized that we would be using
multiple software packages. Therefore, we wanted to ensure that they were all in the
same place. To do this, we installed Anaconda. Anaconda is an open-source, free
distribution software with Python and R available packages already installed. It's 
main purpose is to provide simple tracking of these packages with an easy, user-friendly
dashboard design[@fa18-523-52-conda]. Each version of its packages are managed by its
package management system, Conda. In Anaconda, we used Jupyter and Jupyter Notebook to 
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

Pandas is a Python package also automatically downloaded with Anaconda. It provides many
data analysis features that are widely used in data visualization. Pandas is able to 
incorporate many types of data formats as well. For example, Pandas can read in tabular 
data from SQL or Excel, it can obtain ordered or unordered data, arbitrarily matrixed data,
and it can even read in data that has no labels. Pandas is able to handle missing values and
also non-floating point data by labeling it as NaN. One important feature we specifically
used was to convert data that incorporated NumPy structures into DataFrame objects. This 
feature allowed Pandas to easily read and control the data into an acceptable format that
was able to successfully create a readable graph. Another convienient tool we used while 
manipulating my dataset was Pandas ability to slice and create subsets of my data. This 
allowed me to create new tables and graphs from carefully selected data where we saw possible
correlations. To create detailed visualizations, Pandas incorporates matplotlib API 
[@fa18-523-52-pandas]. Matplotlib allows the import of visualization libraries that can be
read by Pandas. Matplotlib is a 2D plotting library that can be used in Python scripts and
the Jupyter notebook, which we have previously mentioned. Some examples of the types of plots
matplotlib includes is histograms, bar charts, scatterplots, errorcharts, power spectra, and
more[@fa18-523-52-matplotlib]. 

## Installation
To install Jupyter itself you must already have Python 2.7 or Python 3.3 or greater. It
is recommended to go ahead and download Anaconda, like we did, so that all of your packages 
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

The dataset we have chosen is often used in training tools for medical
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

The first part in analyzing the HAM10000 dataset is to acquire it as well as the Anaconda
platform. Once you access the Jupyter Notebook and import the necessary Python packages,
you are ready to begin analyzing the data. Jupyter is a great tool to use in data analysis
becuase you can easily manipulate your code line-by-line. By performing multiple plotting
algorithms, you get a great visualization of relationships amongst the dataset. Of course,
there are simple methods to analyze singular features and columns in your dataset. The 
method below shows multiple statistical analyses on the age feature.

```python
db['age'].describe()

count    9919.000000
mean       52.067749
std        16.686741
min         5.000000
25%        40.000000
50%        50.000000
75%        65.000000
max        85.000000
```

The first algorithm that was used in my Jupyter-based script was a DataFrame comparison 
between the localization and age features. This comparison shows the number of patients who
recorded diagnosed skin lesions for different locations in addition to their differing
ages. The Pandas DataFrame is a class that has the ability to take in a mutable, 
two-dimensional data structure that contains labeled axes[@fa18-523-52-pandas]. It is known
as the primary Pandas data structure. There are many examples of methods that can be used
with this structure on Pandas documentation. To configure a visual of this correlation, the
following code was imposed:

```python
#name the database file to your liking after completed download
db=pd.read_csv('534data.csv')
df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['age', 'localization']).cumsum()
df3['localization'] = pd.Series(list(range(len(db))))
df3.plot(x='localization', y='age')
```

The generated plot is as shown below +@fig:localAge :

![Correlation of localization and age](images/localAge.png){#fig:localAge}

The visualization makes it obvious that there can be many different localizations per age
group. This visualization also supports the need for varied datasets in the clinical domain. 
It ultimately makes it quite difficult to make assumptions on singular lesion samples because
the locations are varied no matter the age. 

Another algorithm that was imposed on Jupyter Notebook to create a visual analysis was an 
autocorrelation analysis. Autocorrelations are important in data analysis because they give
important information regarding the quality of your dataset. Specifically, it checks randomness
within your values with can also give clues to missing or empty values that you may have 
missed when cleaning the data. Over time, the data is compared to see if it lies near zero. If
the data is considered random, the time series autocorrelation will be near zero for all time-
lag separations. If the series is considered non-random, then the autocorrelations will be 
non-zero. The graph that is generated shows two horizontal lines that indicate 95% and 99% 
confidence bands. Using the following code, we have generated the following autocorrelation plot
+@fig:autocorrelation. 

![Autocorrelation](images/autocorrelation.png){#fig:autocorrelation}

Since the values in the above autocorrelation plot are within the 95%, and some very close to the
99% correlation lines, it can be said that the dataset is far from random. This is promising
because it reinforces the quality and trust within the dataset. 

Another technical tool that we used to analyze my dataset was the KNIME Cloud Analytics Platform
[@fa18-523-52-KNIME]. The KNIME cloud can be integrated via the Azure Marketplace or on 
Amazon AWS. KNIME stands for KoNstanz Information MinEr and is an open source
data analytics software that creates services and applications for data science projects. KNIME 
allows its users to create visual workflows with a user-friendly drag and drop graphical interface
that depletes the need for any programming. However, KNIME does allow implementation of other 
scripting languages such as Python [@fa18-523-52-KNIME] or R [@fa18-523-52-KNIME] that creates 
connections to abilities within Apache Spark or other machine learning tools. KNIME allows imports
of datasets from a variety of formats, some of which include CSV [@fa18-523-52-machine] , PDF 
[@fa18-523-52-machine] , JSON [@fa18-523-52-JSON] and more. The workflows and visualizations that 
KNIME produces allows export in many of these formats as well. It also supports several unstructured
data types from images, documents, and certain networks. KNIME operates by a node system that 
includes embedded modules that help its users build their workflow. With this node system, users can
make changes at every step of their analysis to ensure the most current version. KNIME also provides 
detailed visualizations from a set of defined graphs and charts which can lead to predictive analyses 
and machine learning implementations. Users can shape their data by a variety of mathematical models 
such as statistical tests, standard deviations, and means. Users can even select specific features for
use in possible machine learning datasets and apply filters to mark out some of the data if needed.

KNIME is a platform that can perform intense data analytics on a graphical user interface and 
incorporate a user-friendly workflow. It incorporates large or small data sets and even projects as 
broad as deep learning. KNIME is diverse in that its users do not necessarily need to know any coding 
languages to use it. KNIME is a process-oriented, single base workflow with basic input/output 
manipulations. KNIME is an open source platform that uses thousands of its documented nodes within the
node repository for use in the KNIME workbench. A node is a single processing point of data manipulations
within your workflow. A workflow is described as a sequence of steps a user follows in their platform that
is used to complete their final product. The collection of nodes that creates a KNIME workbench is able to
be executed locally or within the KNIME web portal on its own server. The workflow that KNIME follows first
begins with data collection, data cleaning, data integration, and finally, feature extraction. This workflow
allows for large files such as a CSV to be accessed through the web portal and it can therefore be 
manipulated through several wizards [@fa18-523-52-guided].

KNIME has the ability to be integrated with other techonlogies for larger open-source projects. 
These cloud services allow for user's projects to be analyzed even further. For example, KNIME can
be used with Amazon AWS [@fa18-523-52-aws] and Azure [@fa18-523-52-azure]. KNIME's platform can be
hosted on Microsoft Azure Cloud Services. Azure allows KNIME to perform its analytical, machine g
learning, and deep learning tasks on its integrated server. This application can be downloaded from
Azure's Marketplace. KNIME can also be incorporated with Amazon AWS. When KNIME is connected to AWS
resources, users can leverage the memory available while connected to the relational database 
service to construct SQL queries visually. KNIME's Analytic Platform is a free service for all who 
use it. However, if you are using KNIME on a cloud service such as Azure or AWS, there are often 
subscription fees associated. Students and other organizations can receive discounts or allocated 
amounts for a specified time of use. KNIME is a data analysis software platform that allows for easy
read and manipulation of large datasets that can ultimately be used to make inferences and 
predictions. Its user-friendly interface allows for a broad integration of users and sometimes more 
efficient workflows. KNIME has several applications for its users such as data modeling, machine 
learning, predictive analysis, and more. After visualization, users can extract specific features 
from their data and implement it into a model of their choice, which can then be exported as a CSV 
file.

Creating visualizations in the KNIME platform is extremely easy. The steps to create visual 
analyses on KNIME's analytic platform are to first drag and drop the CSV Reader node into the 
workflow. Once in the workflow, import the dataset from where you saved it locally by right-
clicking on the CSV Reader node, and choosing Configure. Once the dialog box pops up, choose
the number of rows and columns to include (we included them all). Then, choose which algorithm 
you would like to impose on the dataset by searching the node directory again. For my first 
analysis, we chose to do a basic graph showing the amount of different diagnostic descriptions
per area (localization). The figure below shows this correlation, +@fig:dx. 

![Descriptions by location](images/dx.png){#fig:dx}

The above image shows proof that although some diseases are more relevant than others, it is
important to have variable datasets such as these. Having so improves the accuracy of other
diagnoses because of the increased comparison amongst individual units of data. It emphasizes
that no matter the location, there can be many different types of apparent disease types. 
Another created image is the visual of density among three data features. We chose to generate
this graph with all three features along separate axes. The figure below indicates these 
results +@fig:subplots52.

![Subplots](images/subplots.png){#fig:subplots52}

Using KNIME's analytical platform, we was able to use defined algorithms to further expand my
visualizations. One algorithm we explored was that of parallel coordinates. Parallel coordinates
is a graph that exemplifies the many differences between multiple variables and features. In the
graph I've generated, the age and sex features are placed on their own axes. The lines that 
connect the two features together are the actual values of the two features. Each line can be 
seen as an accumulation of the points that lie upon each axis [@fa18-523-52-pc]. The downside of
this algorithm is that sometimes the dataset can make the graph look somewhat dense. The figure 
below shows the parallel coordinates of age and sex within the HAM10000 dataset, which is also 
quite dense +@fig:pc.

![Parallel Coordinates of Age and Sex](images/parallelcoordinates.png){#fig:pc}

KNIME allowed me to create this visualization without the use of any code, as their GUI is 
simple enough that programming is not always necessary. However, we also created this picture 
through code in Jupyter Notebook. The following script shows how we was able to do this.

```python
from pandas.plotting import parallel_coordinates
df=pd.DataFrame(np.random.randn(1000, 2), columns=['age', 'sex'])
parallel_coordinates(df, 'dx')
```

Another algorithm we incorporated was logistic regression. This type of analysis compares a
nominal independent and dependent variable. The regression model is used to predict a 
possible outcome between the two given variables[@fa18-523-52-lg]. The logical question we thought
of when performing this analysis was if the location of skin cancer on a person's body had any 
influence or correlation on which type of cancer it was. The following image +@fig:lg52 was 
created to show the logistic regression in this dataset. It shows that the relationship between
cause of diagnosis (description/dx) and location is very much varied. There are, of course, some
outliers, but it seems as though one can conclude that many different types of skin cancers can 
occur in numerous locations. This can be useful for medical professionals or students who are 
using this dataset as a training tool. It can also be said that conclusions can not automatically
be made on what type of cancer is in a given region just by initial glance or statistics. 

![Logistic Regression of dx and localization features](images/logisticRegression.png){#fig:lg52}

It turns out that our analysis is correct in that different types of cancers can occur in varied
locations. The figure below, +@fig:locations52, actually shows the amount of different localizations
within the dataset. Therefore, the relationship between these two features is not very strong. 
Everyone knows that one of the most common risks for skin cancer is sun exposure and ultraviolet 
light. Melanoma (mel) and basal cell carcinoma (bcc), most often caused by these factors, can occur
in areas such as the face, arms, chest, back, scalp, ears, neck, and so on [@fa18-523-52-cancsociety].
However, skin cancers can also occur in areas where the sun cannot reach [fa18-523-52-abchealth].
These occurances can be caused by a genetic mutation or a change in gene regulation that causes
healthy cells to divide with errors. These mutated cells could then invade other parts of the body
and spread. It has also been seen that skin cancers can possibly be caused by pollutants or toxins
in the environment [fa18-523-52-abchealth]. 

![Skin Cancer Localizations Within the HAM10000 Dataset](images/localizations.png){#fig:locations52}

A good algorithm to test the relationship between diseases and the sexes is a regression tree. A
regression tree is an algorithm that predicts the results of two, usually categorical, variables.
The regression model is quite easy to interpret. Using KNIME's analytical platform, we conducted 
a predictive regression tree diagram of the sexes within the HAM10000 dataset. The results show 
that the dataset includes a higher number of diseased males than females. The figure below shows 
the results in the model of the actual regression tree +@fig:tree52. This analysis is also 
important to know because there is no evidence that strongly supports a specific sex to have a
greater or lesser chance of developing a disease. It is easy to see that there are 54.7% of males
with diseases in the dataset and 48.8% of females with diseases. 

![Regression Tree of the Sexes](images/regresstionTree.png){#fig:tree52}

## Benchmark

The presence of big data analysis in healthcare is increasing exponentially. The burden placed on 
medical professionals to read and understand each patient's medical history as well as handling the
current visit is sometimes too much to ask. The use of big data in the healthcare sector would make
the time spent analysing each patient's medical history much shorter, resulting in an increased 
amount of face-to-face communication time between the patient and professional. Predictive analysis 
is a large advantage taking place in healthcare's use of big data today. Predictive analyses can be
used to identify risks for future diseases among patients and therefore, doctors can use that 
information to prescribe certain medications, health-promoting activities, and other preventative 
measures. As mentioned earlier, electronic health records are now being used as one of the most 
reliable forms of big data in healthcare. It is obvious, especially in the modern age, that we 
realize people's health is ever-changing and there are multiple factors that weigh in for almost 
every medical situation. Use of big data in healthcare setting is also being seen in medical 
research. Analysis of recovery methods for certain drugs and treatments in cases of cancer can be 
used to discover the best-working plan [@fa18-523-52-realworld].  

## Conclusion

The use of big data analytics in heathcare is variable, but has an exciting future. The teaming up 
of data scientists with medical professionals will expand society's knowledge for determining the 
identity of a disease or even a patient's future. Big data in healthcare has the ability to give us
inferences to outcomes and diseases we may have not even seen coming. The combination of these two 
fields will definitely speed up research and increase the rate of discovery from both sides. This 
starry-eyed future, however, comes at a cost. Acquiring reliable datasets are expensive, the data 
must be kept confidential, and it must also be extremely accurate regarding its inclusion requirements.
The HAM10000 dataset, which satisifies all of the above credentials, is one of many big datasets being
used for analysis among medical professionals. The analyses performed on this dataset is just the 
beginning of what can truly be done to explore further information into the relationship between the 
donated skin lesions and its multiple features. 

## Acknowledgement

Thanks are given to Professor Geoffrey Fox and Professor Gregor von Laszewski for providing the 
inspiration to create the analyses displayed in this project.
