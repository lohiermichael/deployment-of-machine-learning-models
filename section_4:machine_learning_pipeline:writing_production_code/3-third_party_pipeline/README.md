# Third Party Machine Learning Pipeline

This part is about writing production code to build  Machine Learning Pipeline leveraging the power of a third party pipeline. In this case this third party pipeline will be **Scikit-Learn**.

## Why Scikit-Learn

- Scikit-Learn is a Python library that provides a solid implementation of a range of ML algorithms.

- Scikit-Learn provides efficient versions of a large number of common algorithms.

- Scikit-Learn is characterized by a clean, uniform, and streamlined API.

- Scikit-Learn is written so that most of its algorithms follow that same functionality.

- Once the basic use syntax of Scikit- Learn is understood for one type of model, switching to a new model or algorithm is very straightforward.

- Scikit-Learn provides useful and complete online documentation that allows to understand both what the algorithm is about and how to use it from Scikit-Learn

- Scikit-Learn is so well established in the community, that new packages are typically designed following Scikit-Learn functionality to be quickly adopted by end user, e.g., Keras, MLXtend

## Scikit-Learn organization

Scikit-Learn has three main types of objects:
- **Transformers:** class that aims to transform the data. They typically have: `fit` and `transform` methods. Among them, we find:
    * Scalers
    * Feature selectors
    * One hot encoders

- **Predictors:** class that makes predictions. They carry the `fit` and the `predict` methods. This includes all the ML algorithms:
    * Lasso
    * Decision trees
    * SVM
    * etc...

- **Pipeline:** class that allows you to list and run transformers and predictors in sequence. The characteristics are that:
    * You can list as many transformers as you want
    * The last step of the pipeline should be a predictor

    ## In practice

    We don't need to write a **custom pipeline** because Scikit-Learn took care of that part.
    
    Instead, we need to write code for all of our engineering steps in the way that can be used by the Scikit-Learn Pipeline.

   We need to build individual transformers that allow the `fit-transform` Scikit-Learn functionality so we can integrate the Transformers as part of the Scikit-Learn Pipeline.

   Scikit Learn already has **templates** for the transformers. So, we need to call the templates, **inherit** all the methods and adjust the `fit` and `transform` parts of it

   ## Advantages

   - It can be tested, versioned, tracked and controlled
   - One can build future models on top
   - It follows good software developer practices
   - It leverages the power of an acknowledge API like Scikit-Learn
   - Data scientists are familiar with Pipeline use, so it can reduce over-head
   - Engineering steps can be packaged and re-used in future ML models

   ## Disadvantages

   - It requires software development skills to build and maintain the code
   - It can be an overhead for software developers that need to familiarize with code for sklearn API. For instance, it may be challenging to debug

   




