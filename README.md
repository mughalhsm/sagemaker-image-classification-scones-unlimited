# Scones Unlimited Image Classification Model

## Overview

The Scones Unlimited Image Classification Model is a machine learning project that aims to classify vehicles (bicycles and motorcycles) in order to optimize operations and routing for a scone-delivery-focused logistics company. The model was built using AWS Sagemaker, and it was deployed using AWS Lambda functions and Step Functions. This project was developed as part of the Udacity AWS Machine Learning course and demonstrates the application of concepts learned in the course, such as data preparation and staging, model training and deployment using AWS Sagemaker, AWS Lambda functions, and Step Functions. The goal of this project is to showcase the ability to build and compose scalable, ML-enabled AWS applications.

## Background

Image Classifiers are used in the field of computer vision to identify the content of an image, and it is used across a broad variety of industries, from advanced technologies like autonomous vehicles and augmented reality, to eCommerce platforms, and even in diagnostic medicine.

As a Machine Learning Engineer for Scones Unlimited, the goal was to build a model that can detect which kind of vehicle delivery drivers have, in order to route them to the correct loading bay and orders. Assigning delivery professionals who have a bicycle to nearby orders and giving motorcyclists orders that are farther can help Scones Unlimited optimize their operations.

In addition to the notebook, code is also provided for AWS Step Functions and AWS Lambda functions. These components are used to compose the model and supporting services into an event-driven application that can be deployed and scaled to meet demand.

## Real-world Applications

Image classifiers have numerous real-world applications. For instance, in the field of autonomous vehicles, image classifiers are used to identify road signs, traffic lights, pedestrians, and other vehicles, which are critical for the vehicle to make safe driving decisions. In healthcare, image classifiers are used to identify and diagnose medical conditions in medical images, such as X-rays and MRI scans. In e-commerce, image classifiers are used to improve product search and recommendation systems. In general, image classifiers have numerous applications in industries where identifying the content of an image is important.

## Project Steps Overview

1. Data staging: We'll use a sample dataset called CIFAR. Extract the data from a hosting service, transform it into a usable shape and format, and load it into a production system. In other words, we're going to do some simple ETL!
2. Model training and deployment using S3 storage and AWS Sagemaker endpoints and deployment: Build and train the image classification model using AWS Sagemaker, and then deploy the model using AWS Lambda functions and Step Functions.
3. Lambdas and Step Function workflow: Use AWS Lambda and Step Functions to create a workflow that allows the model to be composed with other supporting services into an event-driven application.
4. Testing and evaluation: Test and evaluate the image classification model, and visualize the data to get insights into the model's performance.
5. Cleanup cloud resources: Get rid of all the cloud services that were used in the project to avoid incurring unnecessary costs.

## Conclusion

The Scones Unlimited Image Classification Model is a valuable tool for logistics companies looking to optimize their operations. This project demonstrates how to build and deploy an image classification model in a production environment using AWS services. Image classifiers have numerous applications in various industries, and this project serves as a useful reference for building similar applications in the future.
