# Section 6: Creating a ML Pipeline Application

In this section, we will be covering everything from:
- Preparing the training data
- Feature engineering
- Training the model
- Performing prediction within the model package

We will be **packaging the model** so that we can make an easy use of it in other applications

## What will be new?

Key Differences with the code already covered will include:
- Work within a Github repository
- Introduce Tooling (such as Tox)
- Adding Prediction Module
- Introduce Testing
- Versioning
- Logging
- Packaging

## Why does this matter?

Build your models in a way that allows you to:
- Reproduce any prediction
- Reduce the risk of errors
- Debug problems in the code base
- Elegantly handle errors
- Have a modular structure

The steps of this section can be tracked in the following [repo](https://github.com/lohiermichael/public-repo-deployment-ml-models.git) that I forked from the course template.

## Wrap-up


### Key Learning Points

- **Package your model for reproducibility with effective use of versioning (including data)**

We have talked a lot about versioning. We did not only versioned the ML model but also the training data and the dependencies.

- **Clearly organize you preprocessing and feature engineering steps**

This is going to make any adjustment and adaptation to the model much simpler. Every time you change a preprocessing step or an engineering step, one should be incrementing the model version for the sake of differentiation of versions

- **Persist your predictions**

That includes both inputs and outputs. In section 6, we did that through logs. If we are in a regulated
or environment where you might be audited, you should be persisting to **databases** to make sure that we never loose that information.

- **Abstract model details in config**

Make the config file easily readable so that updates are simple

- **Validate your data**

The input we receive is not going to be necessarily of the format we except. The good practice is to use schemas and always plan a layer of safety
