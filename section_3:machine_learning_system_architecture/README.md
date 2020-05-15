# Machine Learning System Architecture
## *And why it matters*

A **System** is composed of:
* **Infrastructure:** from hardware to operating system
* **Applications:** Programs performing specific tasks
* **Data**
* **Documentation**
* **Configuration**

**Architecture** is the term used to describe **Systems**. 

**Architecture**: the way software components are arranged and the interactions between them.

As of ML Systems, developing them is fast and cheap but **maintaining** overtime them is challenging.

## Key principles and challenges of ML Systems

* Need for **reproducibility**: how to duplicate ML exactly. It is needed fo research, model improvement, audits...

* **Entanglement**: *ex:* if we change the input feature, further elements in the pipeline may change as well. This refers to the ***"Changing anything, changing everything principle***

* **Data dependencies**: the two inputs of an ML pipeline are code and data. However, some data inputs are unstable.

* **Configuration issues**: need for incrementing models and experimenting

* **Data and feature engineering**: putting the code in an adequate format for certain libraries such as sklearn of Tensorflow can require a lot of code which is challenging to maintain

* **Model errors can be hard to detect with traditional test**: alternative test such as differential tests can be useful

* Separation of expertise: ML System contributors are:
    * DevOps
    * Software engineering
    * Data Science
    * Business people
If the full process is not understood it may lead to errors and lost of time.

The ke Principles for ML System architecture are:
* **reproducibility**: have the ability to replicate a given ML prediction
* **Automation**: retrain, update, deploy models as part of an automated pipeline
* **Extensibility**: have the ability to easily add and update models
* **Modularity**: preprocessing/feature engineering code used in training should be organized into clear pipelines
* **Scalability**: ability to serve model predictions to large numbers of customers (within time constraints)
* **Testing**: test variation between model versions

## Design Approaches to ML System Architecture

There are 4 general ML Architectures (Inexhaustible list):
1. **Train by batch, predict on the fly, serve via REST API**. 

*ex:* a model train persisted off line, loaded in a Web application about houses in real time when  details about a given house are posted by a client to a REST API

2. **Train by batch, predict by batch, serve through a database**.

*ex:* a user upload a CSV of houses with the input details. Then, he receives an email 30 minutes later to check the website to see the results. This application will perform the batch prediction with an asynchronous task queue and those results will be saved to a shared database which can be accessed by a web application.

3. **Train, predict by streaming**

*ex:* our application could read a prediction from a distributed queue or an updated model from this distributed queue and easily load it

4. **Train by batch, predict on mobile**

*ex:* No backend service is needed to make the prediction. It could be made on device

## Architecture Component Breakdown

We are going to breakdown the **1. Train by batch, predict on the fly** method that we are going to investigate later in the course.

The high level architecture is composed as followed:
* **Data Layer**: provides access to all our data sources to train our models. It also simplifies the challenge of data reproducibility
* **Feature Layer**: is responsible for generating feature data in a transparent, reusable, and scalable manner
* **Scoring Layer**: transforms feature into predictions. We often use scikit-learn as the industry standard for this layer. Other libraries are Xgboost and Keras for Neural Networks
* **Evaluation Layer**: monitors the equivalence of different models. This layer can be used to check how closely  the predictions on live traffic matches the training predictions for example

## Building a Reproducible ML Pipeline

What is reproducibility in Machine Learning?

Reproducibility is the ability to duplicate a machine learning model exactly, such that given the same raw data, both models return the same output.

To ensure reproducibility between research and production we need to ensure it for the different steps of the pipeline:

1. **Gathering data:** 

This is potentially the most difficult step to ensure reproducibility.

Problems occur if the training dataset can't be reproduced at a latter stage.

*ex1:* The databases are constantly updated and overwritten, therefore values present at a certain time point differ from values later on.

*ex2:* The order of data during data loading is random, for instance when retrieving the rows with SQL.

**How to ensure reproducibility when we inject our data?**

* Save a snapshot of training data (either the actual data, or a reference to a storage location such as AWS S3)
    - PRO: if the data is not pulled from too many different  and if it is not too big
    - CONS: it may not be allowed to store the data on another platform because of regulations and if too big, not been able to store it somewhere else

* Design the data sources with accurate timestamps, so that a view of the data at any point in time can be retrieved
    - PRO: it works in the ideal situation
    - CONS: it may require a real effort to re-design the data sources

For SQL randomness, we can ***"order by"***

2. **Data preprocessing and variable selection:** feature creation

**Lack of reproducibility may arise from:**

* Replacing missing data with random extract values
* Removing labels based on percentages of observations
* Calculating statistical values like the mean to use for missing value replacement
* More complex equations to extract features, e.g., aggregating over time

**How to ensure reproducibility?**

By adopting a few code practices, it is easy to minimize the lack of reproducibility.

* Code on how a feature is generated should be tracked under **version control** and published with auto incremented or timestamp hashed versions.

* Many of the parameters extracted for feature engineering depend on the data used for training. Therefore, we have to ensure that the data is reproducible in the first place.

* If replacing by extracting random samples, always set the seed.

3. **ML Model Building**

**How to ensure reproducibility?**

* Record the order of the features
* Record applied feature transformations, e.g., standardization
* Record the hyperparameters
* For models that require an element of randomness to be trained (decision trees, neural networks, gradient descent), always set the seed.
* If the final model is a stack of models, record the structure of the ensemble

4. **Model deployment:** Software environment and implementation

**How to ensure reproducibility?**

* For full reproducibility, the software versions should match exactly - applications should list all third party library dependencies and their versions.

* Use a container and track its specifications, such as image version ( which will include important information such as operating system version)

 * Research, develop and deploy utilizing the same language, e.g., python

 * Prior to building the model, understand how the model will be integrated in production -how the model will be consumed-, so you make sure the way it was designed can be fully integrated.
    * Examples of partial deployment include, some data not being available at the time of consuming the model live
    * Filters in place do not allow a certain cohort of data to be seen by the model