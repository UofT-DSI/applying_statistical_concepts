# Applying Statistical Concepts: Linear regression, classification, and resampling

## Content
* [Description](#description)
* [Learning Outcomes](#learning-outcomes)
* [Assignments](#assignments)
* [Contacts](#contacts)
* [Delivery of the Learning Module](#delivery-of-the-learning-module)
* [Requirements](#requirements)
* [Resources](#resources)
  - [Documents](#documents)
  - [Simple Linear Regression](#simple-linear-regression)
  - [Multiple linear regression, interactions, qualitative predictors](#multiple-linear-regression-interactions-qualitative-predictors)
  - [Classification (logistic regression, generative models)](#classification-logistic-regression-generative-models)
  - [Resampling methods (CV, bootstrap) and Linear model selection and regularization](#resampling-methods-cv-bootstrap-and-linear-model-selection-and-regularization)
  + [How to get help](#how-to-get-help)
* [Folder Structure](#folder-structure)

## Description

This module introduces the skills required to design, implement and test basic statistical learning methods including regression, classification, clustering as well as validate it with resampling. The module compares the differences between modelling for prediction purposes and inference. It explores the choices between prediction accuracy and model interpretability, and the bias-variance trade-off. 

## Learning Outcomes

By the end of the module, participants will be able to:
* Implement and interpret the results from several supervised learning approaches for regression and classification
* Use resampling methods to select a model
* Determine the requirements for reproducible learning
* Analyze the uncertainties associated with model results and the ethical consequences of acting on these results
* Explain the different trade offs and considerations for the statistical methods in their toolkit to both technical and non-technical audiences

## Assignments

Participants should review the [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md) for instructions on how to complete assignments in this module.

- Assignment 1: TBA
- Assignment 2: TBA
- Assignment 3: TBA

**Assignment Due-dates**

| Assessment        |  Due Date                         | 
| ------------------| ----------------------------------|
| Assignment 1      |   Sep 29    | 
| Assignment 2      |   Oct 6     |
| Assignment 3      |   Oct 13    | 

### Contacts
**Questions can be submitted to the _#cohort-4-help_ channel on Slack**
* Technical Facilitator: **Holly**. Emails can be sent to xhonglei2007@gmail.com
* Learning Support Staff: **Kasra**. Emails can be sent to vakiloroayaei.kasra@gmail.com
* Learning Support Staff: **Amanda**. Emails can be sent to waiyuamanda.ng@mail.utoronto.ca
* Learning Support Staff: **Vishnou**. Emails can be sent to vishnouvina@cs.toronto.edu

### Delivery of the Learning Module

This module will include live learning sessions and optional, asynchronous work periods. During live learning sessions, the Technical Facilitator will introduce and explain key concepts and demonstrate core skills. Learning is facilitated during this time. Before and after each live learning session, the instructional team will be available for questions related to the core concepts of the module. Optional work periods are to be used to seek help from peers, the Learning Support team, and to work through the homework and assignments in the learning module, with access to live help. Content is not facilitated, but rather this time should be driven by participants. We encourage participants to come to these work periods with questions and problems to work through. 
 
Participants are encouraged to engage actively during the learning module. They key to developing the core skills in each learning module is through practice. The more participants engage in coding along with the instructional team, and applying the skills in each module, the more likely it is that these skills will solidify. 

The technical facilitator will introduce the concepts through a collaborative live coding session using the Python notebooks found under `/01_materials/notebooks/`. Slides can be found under `/01_materials/slides/`.

### Requirements

* Participants are expected to have completed Shell, Git, and Python learning modules.
* Participants are encouraged to ask questions, and collaborate with others to enhance learning.
* Participants must have a computer and an internet connection to participate in online activities.
* Participants must not use generative AI such as ChatGPT to generate code in order to complete assignments. It should be use as a supportive tool to seek out answers to questions you may have.
* We expect participants to have completed the steps in the [onboarding repo](https://github.com/UofT-DSI/Onboarding/tree/tech-onboarding-docs).
* We encourage participants to default to having their camera on at all times, and turning the camera off only as needed. This will greatly enhance the learning experience for all participants and provides real-time feedback for the instructional team. 

## Resources
Feel free to use the following as resources:

### Documents
- Textbook: [Data Science: A First Introduction](https://python.datasciencebook.ca/index.html)
- Alternative textbook: [Introduction to Statistical Learning with Python Documentation (ISLP)](https://islp.readthedocs.io/en/latest/index.html)

### Videos 
- [Introduction to Statistical Learning with Python Video Playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rPP6braWoRt5UCXYZ71GZIQ)

#### Simple Linear Regression
- [Linear Regression, explained in 2 minutes](https://www.youtube.com/watch?v=CtsRRUddV2s)
- [Linear Regression, Clearly Explained!!!](https://www.youtube.com/watch?v=7ArmBVF2dCs&pp=ygUic2ltcGxlIGxpbmVhciByZWdyZXNzaW9uIHN0YXRxdWVzdA%3D%3D)

#### Multiple linear regression, interactions, qualitative predictors
- [Multiple Regression, Clearly Explained!!!](https://www.youtube.com/watch?v=EkAQAi3a4js&pp=ygUic2ltcGxlIGxpbmVhciByZWdyZXNzaW9uIHN0YXRxdWVzdA%3D%3D)

#### Classification (logistic regression, generative models)
- [Logistic Regression, explained in 3 minutes](https://www.youtube.com/watch?v=EKm0spFxFG4)
- [StatQuest: Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8&list=PLblh5JKOoLUKxzEP5HA2d-Li7IJkHfXSe)
- [StatQuest: Linear Discriminant Analysis (LDA) clearly explained.](https://www.youtube.com/watch?v=azXCzI57Yfc&pp=ygUNTERBIHN0YXRxdWVzdA%3D%3D)
- [StatQuest: K-nearest neighbors, Clearly Explained](https://www.youtube.com/watch?v=HVXime0nQeI&pp=ygUNa25uIHN0YXRxdWVzdA%3D%3D)
- [Naive Bayes, Clearly Explained!!!](https://www.youtube.com/watch?v=O2L2Uv9pdDA&pp=ygUaYmF5ZXMgY2xhc3NpZmllciBzdGF0cXVlc3Q%3D)
- [Generalized Linear Model](https://www.youtube.com/watch?v=SqN-qlQOM5A)

#### Resampling methods (CV, bootstrap) and Linear model selection and regularization
- [Linear Modelling](https://www.youtube.com/watch?v=-inJu1jHqb8)
- [Machine Learning Fundamentals: Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw&pp=ygUYdmFsaWRhdGlvbiBzZXQgc3RhdHF1ZXN0)
- [Bootstrapping Main Ideas!!!](https://www.youtube.com/watch?v=Xz0x-8-cgaQ&pp=ygUXYm9vdHN0cmFwcGluZyBzdGF0cXVlc3Q%3D)
- [Bootstrapping Method](https://www.youtube.com/watch?v=uGsf3spCM3Y)
- [k-fold Cross Validation](https://www.youtube.com/watch?v=TIgfjmp-4BA)

### How to get help
![image](./steps_to_ask_for_help.png)
Please remember to use the help channel to get help from the course support!

<hr>

## Folder Structure

```markdown
.
├── 01_materials
├── 02_activities
│   │   assignments
│   │   exercises
│   │   homework
├── 03_instructional_team
├── 04_cohort_4
├── LICENSE
├── README.md
└── steps_to_ask_for_help.png
```

Exercises and homework are **optional** additional resources for you to learn outside the live learning sessions. Only assignments are mandatory in order to successfully pass this module.