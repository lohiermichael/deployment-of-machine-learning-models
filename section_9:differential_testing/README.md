# Section 9: Differential Testing

## Introduction

In the context of Machine Learning applications, **differential tests** are particularly useful

## What is Differential Test?

It is a type of test that compares the differences in execution from one system version to the next (two successive versions of the work) when the inputs are the same.

- They are sometimes called **"back-to-back"** testing
- They are very useful for detecting machine learning subtle system errors that do not raise exceptions
- Turning them is a balancing act: it depends on business requirements
- It can prevent very painful mistakes that are not detected for long periods of time

Example of mistakes that differential tests can spot:

1. You forget to include a preprocessing step to your data transformation pipeline
2. You have an incorrect feature

If you release your code as is, some tests will pass without raising any system errors. But the predictions that we make will change. **Differential Tests** will catch these changes and alert us before the code goes to production.

## Key Learning points

- Differential tests can protect you from costly mistakes
- Run them like any other tests in your CI pipeline
- Accessing the ol version with the model required a sort of hacking. Once we use Docker, things will become easier. It will just be comparing images

## Other kinds of tests

- If a prediction and/or training speed is a key metric for you, consider implementing **benchmark tests** to compare the speed of functions from one system version to the next. 
    - A great framework for doing this is **pytest-benchmark**

- In complex microservice environments, you may also wish to consider **API contract testing**
    - A great framework for this is **Pact**






