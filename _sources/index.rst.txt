================================
Vikram Rangarajan - Introduction
================================

About Me
=========

I am an undergraduate student at the University of Maryland at College Park.
I am a computer science major on the machine learning track, as well as a statistics minor.
My current experiences are related to my interest in going to graduate school, such as my
research experience.

Statement of Purpose (Work in Progress)
=======================================

My interest in computer science is related to computer vision and deep learning. 
To increase my knowledge on these topics, I chose the machine learning track in my
computer science major which requires me to take classes related to data science, 
machine learning, and in particular, deep learning. I also took a statistics minor 
to improve my knowledge of the base statistics which modern machine learning is built upon.

In particular, I took advantage of CMSC421 (Introduction to Artificial Intelligence). 
The final project was very flexible: create a project related to AI. I chose to create 
a reverse-mode automatic differentiation library with a syntax similar to PyTorch. 
The implementation is very simple and runs a topological sort on the computation graph 
of the network in order to determine the order in which the backward functions need to be called. 
I implemented the forward and backward functions for many of the base operations such as matrix 
multiplication, arithmetic operations, convolutions, indexing, and many element-wise operations. 
NumPy and CuPy were used for the underlying n-dimensional arrays and GPU acceleration. This project 
was noticed by Professor Ehrlich and as a result, I was asked if I wanted to work on research 
projects with Shishira Maiya relating to image and video compression using machine learning.

My research experience with Dr. Shahoveisi involves an application of transfer learning models 
to classify images of nematodes to their correct class. An unique aspect of this project was using 
both automatic hyperparameter tuning and gradual unfreezing in order to find the best model for 
the task. Many similar papers do a grid search over a space of human chosen hyperparameters but 
this ignores the possibility that an optimal value for a continuous hyperparameter such learning 
rate could be between such values. To avoid this, the BOHB (Bayesian Optimization and Hyperband) 
algorithm was used to find these hyperparameters. On top of model hyperparameters, image augmentation
parameters were also tuned. For example, the maximum number of degrees that an image could be 
randomly rotated during training was a hyperparameter which could be tuned. During the run of 
each trial, gradual unfreezing was used to ensure that the pre-trained parameters from the ImageNet
dataset were not erased immediately and could only be learned to fit the nematode image dataset
once an acceptable balanced validation accuracy threshold (50%) was achieved.


Artifacts
=========

.. card:: SimpleTensor Project
	:link: https://vikramrangarajan.github.io/SimpleTensor/

	The Purpose of this project was to create a full-featured automatic differentiation library
	which mimics PyTorch. I used my library to create a simple CNN, but it can also
	be used to create very complex models.

.. toctree::
	:hidden:

	portfolio
.. toctree::
	:hidden:

	publications
.. toctree::
	:hidden:

	resumes
.. toctree::
	:hidden:

	reflectiveessay