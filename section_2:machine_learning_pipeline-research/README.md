# Machine Learning Pipeline - Research Environment

## 1. Overview

A typical Machine Learning pipeline is made of the following steps:
1. **Gathering the data**: coming from different area of the business or from third-parties. The objective is to make the data available to the **data scientist** so that he can start analyzing it.
2. **Data analysis**: as soon as we get the data, we want to know:
    * identify the variables
    * understand how they are related to each other
    * know what we want to predict: supervised, unsupervised...
    * know  what variables we can use
3. **Feature Engineering**: transforming the data before passing them through a ML algorithm:
    * filling missing values
    * dealing with categorical variables
    * ...
4. **Feature selection**: finding the variables that are the most predictive ones. Only the chosen variables will be used to build the model
5. **Machine Learning Model building**: trying different algorithms, analyzing their performance and choosing the one or the few ones that perform the bert results. Evaluation is based on relevant **statistical metrics**: MSE, accuracy...
6. **Model building Business uplift evaluation**: the statistical metrics are not enough to evaluate the performance of a ML model in the context of business. We calculate the uplift in **Business value**

After all these steps, we can move towards **model deployment**.
We need to deploy at least the steps 3, 4 and 5 to the **Cloud**. It is not simply a model that we deploy but an entire pipeline.
