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