# Section 10: Deploying to a PaaS (Heroku) without Containers

## What is a Platform as a Service (PaaS)?

**Paas:** A cloud-based service that provides a platform allowing customers to develop, run, and manage applications without the complexity of building and maintaining the infrastructure typically associated with developing and launching an application

### Range of Possibilities


1. **On-Premises:** you manage everything on your own

**Situation:** you go out and buy a computer that you turn into servers, you plug the cables in, you install the Operating System (OS), the middleware...

This solution is getting rarer and rarer these days. Nowadays, it is really the realm of companies operating legacy software or with very high security requirements.

#### Cloud options

2. **Infrastructure as a Service (IaaS):** Dealt with in section 12

3. **Platform as a Service (PaaS):** It requires that you manage less. The Operating system or the middleware are managed by someone else. You just need to focus on your **application code** and your **data**

4. **Software as a Service (SaaS):** Everything is managed somewhere else

### PaaS Pros and Cons

#### Pros

- Simple to set up, maintain and deploy
- Easy to scale to moderate size. It's just a question of setting up th platform, scaling options or manually adding more instances
- Allows Developers to focus on apps. They don't have to do any sys/admin tasks 
- Easy creation of dev/test environments that exactly match you production environment

#### Cons

- Hard/Impossible to scale to a very large size
- Tends to be more expensive than IaaS
- Vulnerable to PaaS downtime
- Limitations on configuration

### Examples of PaaS

- AWS Elastic Beanstalk
- Windows Azure
- Heroku
- Force.com
- Google App Engine
- Apache Stratos
- PythonAnywhere
- ... and many more

In this course, we are going to choose **Heroku**

### Why Heroku in the Course?

***Note:*** *In the IaaS section, we will use AWS ECS*

- Heroku is very easy to use
- We can use one Heroku Dyno (Virtual Machine Instance) for free
- Nice 3rd Party add-on options
- Works with Docker
- Great Documentation
- Supports multiple languages not only Python

## Key Learning Points

- Integrate your deployment steps into the CI pipeline
- Deployments can be easy
- Get used to checking deployments and logs: debugging in production is an important skill

## Heroku scaling

- On a paid plan, you can manually change the number of Heroku "dynos" to scale your app
- On Performance Tier Dynos, you can enable and configure autoscaling

## Heroku next steps

- You can add databases, message queues and caches very easily
- It's worth exploring the heroku add-ons
- If you want to deploy multiple services from a monorepo, this is also possible with Heroku
