# Procedural programming

Procedural programming, procedures, also known as routines, subroutines or functions, are carried out as a series of computational steps.

For us, it refers to writing  the series of feature creation, feature transformation, model training and data scoring steps, as functions, that then we can call and run one after the other.

## Organization of the code

In procedural programming, the code is divided in three scripts:
1. **the functions (or procedures):** to create and transform features, and to train and save the models and make the predictions
2. **the training script:** calls the previous functions in order to train and save the models
3. **the scoring script:** calls the previous functions in order, to score new data

In addition to these three scripts, we typically include a yaml file where we gather:
- hard coded variables to engineer, and values to use to transform features.
- hard coded paths to retrieve and store data

By changing these values, we ca re-adjust our models.

Let's make and overview of the advantages and disadvantages of **Procedural Programming**

## Advantages

- Straightforward from jupyter notebook
- No software development skills required
- Easy to manually check if it reproduces the original model

## Disadvantages

- The code is really prone to errors
- Difficult to test it
- Difficult to build a software on top of it
- Need to save a lot of intermediate fils to store the transformation parameters