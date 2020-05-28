# Writing Production Code for Machine Learning Deployment

## Overview

In section 2, we have been through different steps of the ML pipeline with code written in Jupyter Notebooks. Three of these steps must be kept to write production code from:
1. Data pre-processing: feature engineering
2. Variable selection
3. Machine Learning model building

We want to write **Production code** to:
* Create and Transform features
* Incorporate the feature selection
* Build Machine Learning Models
* Score new data

**Production code** is not written in Jupyter notebooks but rather in script, for instance Python script.

**How to write production code for an entire ML pipeline?**

There are 3 main ways:
1. **Procedural Programming**: write a sequence of functions similarly to what we did in Jupyter Notebooks
2. **Custom Pipeline Code:** Calls the procedure in order with OOP
3. **Third-party pipeline:** using for instance the scikit-learn pipeline

We will finally discuss **feature selection**.

## Feature selection in CI/CD

 Should it be part of the ML automated pipeline?

 In production, we want to build a pipeline that is:
 * fully integrated
 * continuously deployed

 In practice:
 1. We build a model once
 2. We build the entire **deployment pipeline**
 3. We create **tests** for the continuous integration
 4. Once those tests are fulfilled, the model is automatically deployed
 5. It is made available to the other systems to make calls to it

 As we are in a **continuous deployment  framework**, When the model is updated:
 1. it is retrained
 2. the pipeline will automatically run the tests
 3. if passed, it will automatically be redeployed

 This system has advantages and disadvantages

 ### Advantages

 - Reduced overhead in teh implementation of the new model
 - The new model is almost immediately available to the business systems

 ### Disadvantages

 - Lack of versatility: as the pipeline is built from one dataset, it can't accept potential new variables from other data sources
 - No additional data can be fed through the pipeline, as the entire processes are based on the first data on which it was built

 **Including a feature selection algorithm as part of the pipeline**
 - ensures that from all the available features only the most useful ones are selected to train the model
 - Potentially avoids overfitting
 - enhances model interpretability

 **However,**
- we would need to deploy code to engineer all available features in the dataset, regardless of whether they will be finally used by the model
- error handling and unit testing for all the code to engineering features

**Suitable, if...**

- Model build and refresh on same data
- Model build and refresh on smaller datasets

**Not suitable, if...**

- Model is built using datasets with a high feature space, as it will involve a big piece of production code to engineer and handle errors.
- Model is constantly enriched with new data sources. In this case, we'd better focus on the R&D part of the code to select the features carefully








