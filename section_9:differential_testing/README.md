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


