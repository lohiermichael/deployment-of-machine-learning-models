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

## 2. Feature Engineering

* **Missing data**: Absence of values for certain observations within a variable.
*Reasons:*
    * It can be lost or not stored properly
    * The value doesn't exist in the first place

* **Labels**: Variables for which the value is a String an not numerical. These are **categorical variables**
*Issues*:
    * **Cardinality**: the number of values the categorical variable can take. High cardinality can be an issue because it will dominate other low-cardinality variables
    * **Rare labels**: variables that don't often appear. For instance if the value appear on the test set and not on the train set, we don't know how to deal with them
    * **Categories**: they are String and thus need to be encoded

* **Distribution**: For numerical variables. Is the data following a Gaussian curve or is it skewed

* **Outliers**: For some algorithm, the presence of outliers may be detrimental: values that are too high or too low compared to the other values

* **Feature magnitude**: if the scale values the variables are not the same, it may affect the outcome of some algorithms. For instance, the following algorithms are sensitive to feature scaling:
    * Linear regression
    * Neural Networks
    * PCA
    * ...

