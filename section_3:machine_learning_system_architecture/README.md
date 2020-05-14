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







