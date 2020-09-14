# Section 13: A Deep Learning Model with Big Data

## Introduction

In this section, we will deploy a **CNN** (Convolutional Neural Network) that was trained on a large dataset and also needs large data to make its predictions.

We will cover some of the challenges and things to consider when deploying models that consume large datasets.

### What is big data

**Big data** is used to talk about large volume of data in business, most of the time in **analytics** and **machine learning**

Data can be:
- Structured
- Semi-structured
- Unstructured

Although **Big Data** doesn't equate to any specific volume of data, the term is ofter use to describe: **terabytes**, **petabytes** or even bigger datasets.

In business, the most likely scenarios that involves big datasets are those that contain:
- **text**: large documents
- **images**
- **time series**: complex enough to be solved with **LSTM** (Long Short-Term Memory Network)

**Note:** *LSTM is a type of recurrent neural network capable of remembering the past information and while predicting the future values, it takes the past information into account.* 

For these types of problems, **deep learning** models are the most usually built. These DL models will contain various **layers** and thousands of **parameters** that need to be determined.

### Challenges of using big data in ML

- Neural networks can be extremely compute heavy
- **Training** takes up a lot of compute power
- **Scoring** can also take a lot of computing power
- Neural Networks are difficult to scale
- Neural Networks normally rely on **GPUs**
-  **GPUs** can be scarce and expensive

### Deployment pipeline for CNN

- Coding Challenges
- Deployment Challenges

## V2 Plant Seedlings: dataset description

In this part, we will present the dataset that we are going to use to build and compute the expensive ML model.

TH **V2 Plant Seedlings** dataset comes from Kaggle. 

It consists of:
- **5539 images** of 
- **crop and weed seeds** belonging to
- **12 different species**

The challenge is:<br>
Given an image of the plant, **predict which specie it belongs to**.

We choose this dataset because:
- it is big enough to cover some of the challenges of deploying a machine learning model built on a large dataset
- it is small enough to follow the videos along while running 

After this section, we should be able to apply what we learnt utilizing these dataset to larger datasets and more complex models.

## Reproducibility in Neural Networks

We are going to cover the common problems encountered when trying to obtain reproducible results with Keras and how to try and avoid them.

### Reminder: why does reproducibility matter?

- Reproducibility ensures that models' gains in performance are genuine: they won't come out of nowhere. 

This is particularly relevant for NN as they have a multitude of parameters that need to be fit an many of them rely on random initialization.

- Reproducibility reduces or eliminates variations when re-running experiments: it is essential for testing, continuous integration and iterative refinement of models 

This is crucial when we are looking to improve a previous model that we have already in-house because without reproducible results we wouldn't be sure whether the increase in performance is real or cost by the intrinsic randomness

- Reproducibility is increasingly important as sophisticated models and real-time data streams push us towards distributed training across clusters of GPUs: more sources of non determinism behavior during model training

### What causes non-reproducibility in Neural Networks?

- **Random initialization of layer weights:** the weights of the different layers are initialized randomly

- **Shuffling of datasets:** the dataset is randomly shuffled for example if we leave 10% of the samples for cross-validation without model fit

- **Noisy hidden layers:** dropout layers, which exclude the contribution of a particular neuron, are initialized randomly

- **Changes in ML frameworks:** different versions of mL libraries can lead to different behaviors

- **Non-deterministic GPU floating point calculations:** if using GPUs, certain functions in cuDNN, the Nvidia DEEp Neural Networks library for GPUs, are stochastic, which means that they are initialized randomly at each run.

- **CPU multi-threading:** CPU parallelization when using Tensorflow can also introduce non-reproducibility

### How to control for random initialization

- **Keras** gets its source of randomness from the **numpy random number generator. 

Therefore, seeding the numpy random generator both for Therano or TensorFlow backend

- Tensorflow uses multiple threads, which may cause non-reproducible results.

Force TensorFlow to use single thread. This decision is a trade-off between reproducibility and speed

- **In Python 3, you need to set a flag before running your script**

PYTHONHASHSEED=0

- Set the cuDNN  as deterministic

## Wrap up

### Training in CI: Speed and Memory Considerations

We have seen in this section that we are bound to scenarios where:
- Data is too huge to be included in packaged: in this cases, it is still important to keep a reference and a version of the dataset no matter where it is stored for the sake of reproducibility

- Data can't fit in memory: in this case there are particular techniques: loading and training by batch with Keras for instance.



Training demanding model issues relying on big datasets have the following issue:
- You are likely to need more powerful machines for training neural network: we might consider using GPUs and pay extra for that

### Key Learning points

- Even with larger datasets, you still need to think about reproducibility
- Training in CI is more important and beneficial than ever with deep learning as the cloud server can be more powerful than a local one
- Be sure to tune your machines consider using GPUs
- Reproducibility in Neural Networks has some particular challenges





