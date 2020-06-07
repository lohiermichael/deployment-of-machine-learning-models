# Section 8: Continuous Integration and Deployment (CI/CD)
CD also referred to as **Continuous Delivery**

## What is CI/CD?

Fundamentally it is about **automating the stages of development** The different stages built refer to preparing everything needed to run your code. So in the case of Python, that's:
1. **CI (Continuous integration)**: 
    - **Build**
        - Installing dependencies in your requirements
        - Making sure that the operating system which is going to run your code is set up
        - The virtual machine or docker container is built and ready to go
    - **Test**: Automatically testing your code
    - **Merge**: merge in a feature branch
2. **CD (Continuous delivery)**: as soon as the code is merged, automatically release to either production or a testing environnement

## Why does this matter?

Testing and deploying our applications according to the CI/CD method means:
- The system is always in a releasable state
- Faster, regular release cycles
- Building and testing is automated
- Delivery and deployments are automated (at least to some extent)
- Visibility across the company (and audit log)

In our architecture, we will refer to CI/CD as a pipeline.


## Why CircleCI?

In this course, we are going to use a CI/CD platform called: **CircleCI**

We chose **CircleCI** because:
- They have a hosted platform: we don't have install and set up CircleCI on our own servers
- They have a fairly easy GitHub integration to set up
- They offer one free project: a GitHub repo
- Many great features
- Used by many top companies

## Alternatives to CircleCI

There are many awesome CI/CD platforms:
- Jenkins
- Travis CI
- Bamboo
- Gitlab CI
- Team City
- etc.

We must use on CI/CD platform, it doesn't matter which one...


