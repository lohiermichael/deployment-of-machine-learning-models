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

## 3. Feature selection

It is the action of keeping a fewer number of features that are more predictive to build our model.

### Motivation

Why do we select features in a business?
1. Simple models are easier to interpret by the end user
2. Reduce the training times
3. Enhance generalization by reducing overfitting
4. Easier to integrate by the Software Developers in production: smaller json messages sent to the model
5. Reduce the risk of data errors during the use of the model: less code for error handling
6. Less information to log
7. Reduce feature engineering code

### Variable Redundancy

There are 4 main types of variable redundancy
1. **Constant variables**: only one value per variable
2. **Quasi-constant variables**: >99% constant
3. **Duplication**: Same variable repeated several times in the same dataset
4. **Correlation**: The correlated variables provide the same information

## Methods

There are there main kind of methods for feature selection on data:
1. **Filter methods**
    * Independent of the ML algorithm
    * Based only on variable characteristics

*PROS*:

    * Quick and easy method
    * Fast
    * Model agnostic

*CONS*:

    * Doesn't capture redundancy
    * Doesn't capture feature interaction

2. **Wrapper methods**
    * Consider ML algorithm
    * Evaluate features by groups

*PROS*:

    * Considers feature interaction
    * Best performance
    * Best feature subset for a given algorithm

*CONS*:

    * Not model agnostic
    * Computation expensive
    * Often impracticable

3. **Embedded methods**
    Feature selection during training of ML algorithm

*PROS*:

    * Good model performance
    * Capture feature interaction
    * Better than filter
    * Faster than wrapper

*CONS*:

    * Not model agnostic

In this course, we will try to remove **feature selection** from the pipeline to aim efficiency. We will then select the feature ahead of the pipeline and then pass a list of the features to keep for the model.










