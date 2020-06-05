# Section 7: Serving the model prediction

In this section, we will be looking at serving our model prediction via a REST API.

In the previous sections, we looked at things like:
- Preparing our training data
- Feature extraction
- Building our model package

Now, we are going to see how to serve our model prediction and that where our **REST API** comes in.

## What is a REST API?

REST stands for ***Representational State Transfer***

API stands for ***Application Programming Interface***

A **REST API** means that the server will **send to the client a representation of the state of the requested result**. In our case, it will be a prediction from our model.

The client could be anything form a website to mobile device.

The **RESTs** are quite popular due to their simplicity

## Why does this matter?

Serving our model via a REST API allows us to:
- Serve predictions on the fly to multiple clients: requests from websites, mobile devises, other APIs...

- Decouple our model development from the client facing layer: it is a problem we can face with large apps. We tend to do all the packaging, training, making a REST API in one application. So, decoupling and having a thin REST API allows teams to work independently

- Potentially combine multiple models at different API end points

- Scale by adding more instances of the application behind a load balancer

## Flask overview

Throughout this section, we will be using the **Flask micro framework** to build our API.

- Popular choice for Python microservices (40K stars + on github)
 - Lightweight and flexible and has great documentation
 - Alternatives include: Django, Pyramid, Bottle, Sanic, Tornado, API Star...

 The steps of this section can be tracked in the following [repo](https://github.com/lohiermichael/public-repo-deployment-ml-models.git) that I forked from the course template.