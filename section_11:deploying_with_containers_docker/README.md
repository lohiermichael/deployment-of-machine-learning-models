# Section 11: Deploying with Containers (Docker)

## Plan

In this section, we are going to cover:
- What are containers? What is Docker?
- Why do we use Containers and Docker?
- Installing Docker
- Configuring Docker
- Basic Docker Demo Locally
- Deploying Docker Images to Heroku to enhance our already existing deployment process

## What is a Container?

A container is a standard unit of software that packages up code andd all its dependencies so the application runs quickly and reliably from one computing environment to another.

It is a sort of Operating System virtualization. The container includes everything we need to run our application.

## What is Docker?

- Docker is a tool to make creating, deploying, and running containers easy

- Docker is open source

-  It has been released in 2013

- A Docker container is a standardized unit of software development, containing everything that your software application needs to run: code, runtime, system tools, system libraries, etc...

- Containers are created from a read-only template called an **image**: first we set up the instructions to create the image and then from that image, we create and run containers

## Containers VS Virtual Machines

The main difference between those two is that containers are more light-weight. You can more easily run many containers on your own operating machine.

## Why do we use containers

We use them for:
- **Reproducibility:** you know the steps for creating a given container, because of its **image** and the **Docker file** that gives us information about the dependencies, how the run time was created and what the settings are

- **Isolation:** you can easily tear down and speed back up containers


- **Simplicity of environment management:** Great for making staging and to check if UAT (User Acceptance Testing) matches production.

- **Continuous integration**: deploy quickly taking down existing containers, replacing them on a rolling basis

- Much faster and more **lightweight** than a Virtual Machine: Easy to speed them up

- **Container orchestration options**: for example Kubernetes. It allows to move containers in response to auto scaling events in response to deployment and if you have failures. In section 12, we will be working with AWS managed orchestration solution: the **elastic container service**

- Docker is the most popular tool for creating and running containers

## Key Learning Points

- Containerizing your applications brings a number of benefits: reproducibility, isolation, ease of environment management and more
- Containerization is not a silver bullet - not suitable for every use case (e.g. complex multiple OS requirements)
- Integrate your image building and deployments into you CI pipeline is important


## Resources

**DockerHub**: Docker platform with open source images
- We need to create an account
- We can check how the images are built

