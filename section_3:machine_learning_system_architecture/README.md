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








