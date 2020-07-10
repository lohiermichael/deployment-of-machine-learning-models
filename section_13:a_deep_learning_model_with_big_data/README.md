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

