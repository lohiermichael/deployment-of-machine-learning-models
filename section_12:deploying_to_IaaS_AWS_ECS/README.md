# Section 12: Deploying with (aaS (AWS ECS)

## What we will be covering

- Overview of IaaS/AWS
- Risks and costs of using AWS
- Overview of the Elastic Container Service (ECS)
- Create the AWS account and permissions: identity and access management
- Upload Docker images to the Elastic container registry (ECR)
- Configure your ECS Cluster
- Deploy your cluster
- Automate the CI pipeline

## What is Infrastructure as a Service (IaaS)?

Compared to the Platform as a Service (PaaS) (ex: Heroku), with the IaaS, we are going to manage more things:
- Run time 
- Middleware
- Operating System

Pros:
- Configure every aspect that is needed
- Scale to almost limitless size

Cons:
- Spend more time on configuration

## What is Amazon Web Services?

This is the cloud computing services owned by Amazon. It is the largest provider of cloud computing globally. They offer a vast range of services.

## AWS Elastic Container Service (ECS)

### What ECS?

"Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast, container management service that makes it easy to run, stop, and manage Docker containers on a cluster"

Docker encourages to split applications up into individual components and ECS is optimize for this pattern.

What are these components?
1. The **Container definition** inside
2. The **Task definition** inside
3. A **service** that manages it inside
4. A **cluster**

### ECS Task Definitions and Tasks

What is a task?

An instance of containers working together.<br>
A task definition is like a blueprint for your application (a bit like a Dockerfile). <br>
In this step, you will specify a task definition so that Amazon ECS knows:
- which Docker images to use for containers
- how many containers to use in the task
- the resource allocation for each container
- how much CPU and memory you want to use for each task
- the logging configuration to use
- whether a task should continue to run if the container finishes or fails
- the command the container should run when it is starts
- ...

You entire application stack does not need to exist on a single task definition, and in most cases it should not.

***Note:***
*Within th AWS free tier, you need to leave the number of tasks configured to the default value: 1. That will copy 1 copy of your task.*

### ECS Services 

Amazon ECS allows you to run and maintain a specified number of instances of a tak definition simultaneously, in an Amazon ECS cluster. That is called a **service**.

You can scale your application up and down by changing the number of containers you want your service to run.

You can update your application by changing its definition or using a new image.

If any of your tasks should fail or stop for any reason, the Amazon ECS service scheduler kills it and launches another instance of your task to replace it and maintain the desired count of tasks in the service depending on the scheduling strategy used.


## ECS Cluster

This is the parent grouping of **tasks** or **services**.

There are two main launch types:
1. **Fargate**: it allows you to run your containerized applications without the need to provision and manage the backend infrastructure. 
**Amazon ECS** uses containers by farget automatically scale, load balance and manage scheduling of your containers for availability. It provides an easier way to build and operate containerized applications.

When you're architecting your application using Farget launch type for your tasks, the main question is: **Should you put multiple containers into the same task definition OR deploy containers separately in multiple task definitions?**

2. **EC2**: it allows you to run your containerize.d application on a cluster of Amazon EC2 instances that you manage "manually"


To summarize, **Farget** tasks are more expensive but there is less to manage and configure. Whereas if your require greater control of your instances, perhaps a support compliance and governance requirements, **EC2** launch method is more appropriate.


### Why ECS?

#### What are your options

- Containerization has transformed how we deploy software. Container orchestration is all about managing the life cycles of containers especially in large dynamic environments

- Other Container orchestrion engine options: **Kubernetes**, **ECS**, **Docker Swarm**

- **Kubernetes** is the container orchestration engine of choice developed by Google.
    - it has the most complex setup and management
    - it is self-managed. You can deploy it on premises in private clouds or public clouds compared to **ECS** that is managed by **AWS**
- New player: **Amazon Elastic Container Service for Kubernetes (EKS)**

## Wrap-up

### Key learning points

We saw throughout the section that:

- There are a large range of container orchestration engines as well as manged or self-managed options to consider, each one with pros and cons

- Deploying to IaaS has far greater configuration complexity compared to PaaS: security, resource consumption for our containers

- IaaS can scale to virtually any needs our business may have

### IaaS Next Steps

- Explore other AWS services: S3, Load Balancing, new ELK. 

In this section, we didn't setup a custom domain or a fixed IP address. To do that on ECS, we need to work with the AWS Load Balancing Options

- Explore other IaaS Providers: MS Azure, Google Compute Engine.

- Explore other container orchestration engines: Kubernetes, Docker Swarm






