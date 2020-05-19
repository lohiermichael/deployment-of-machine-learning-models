# Custom Machine Learning Pipeline

We will discuss how to write production code to create a custom ML Pipeline utilizing **Object oriented programming**.

In Procedural Programming, we need to:
- **hard-code** the engineering parameters.
*ex:* the mapping labels in the (previous section)
- **save** multiple objects and data structures. *ex:* the scaler model.

A slight change from the `config.py` file can impact the code. To keep a control on the output, we will then need to track the changes in this file. This can be cumbersome if we want to update or refresh a model frequently.

We can instead write production code with objects that can **learn** these parameters from data and store them as part of their attributes. That how **OOP** comes into play.

## Object Oriented Programming - OOP

In **Object Oriented Programming (OOP)**, we write code in the form of objects.

These "objects" can store **data**, and can also store instructions or **procedures** to modify that data

- The **data** is an **attribute** of the object
- **Instructions** or **procedures** are methods of the object

## Custom ML Pipeline

In OOP the "objects" can learn and store these parameters.

- Parameters get automatically refreshed every time the model is retrained.

- No need of manual hard-coding

- The **methods** widely used in the field of ML are:
    - **Fit**: to learn parameters 
        - Saves the parameter in object attribute
    - Transform: to transform data with the learnt parameters
        - Calls to the object attribute to recall the parameters
- The **attributes** and variables in which are stored the learnt parameters.

A **pipeline** is a set of data processing steps connected in series where typically, the output of one element is input of the next one until we make our prediction.

The elements of the pipeline can be executed in parallel or in time sliced fashion. This last method is useful when we require the use of big data, or high computing power, e.g., for neural networks.

A **Custom ML Pipeline** is therefor a sequence of steps, aimed at loading and transforming the data to get it ready for training or scoring. 

In custom ML pipelines:
- we write the **preprocessing steps** as objects (OOP)
- we write **the sequence**, i.e., the pipeline objects (OOP)

We save one object, the pipeline, as a Python pickle, with all the information needed to transform the raw inputs and get the predictions.

***Note:*** *There is no standard way to custom a pipeline and each organization can make the pipeline the way it will best suit their needs.*

## Advantages

The custom pipeline is well designed from the start so:
- it can be tested, versioned, tracked and controlled
- we can build additional code on top of it for future models
- it is a good software developer practice
- it can be built to satisfy different business needs

## Disadvantages

- Requires a team of software developers to build and maintain the code
- it can cost time for DS to familiarize  with the code for debugging or adding on future models
- it may not be reusable and would require to re-write Processor class for each new ML model 








