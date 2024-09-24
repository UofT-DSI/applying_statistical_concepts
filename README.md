# Applying Statistical Concepts: Linear regression, classification, and resampling

## Content
* [Description](#description)
* [Learning Outcomes](#learning-outcomes)
* [Assignments](#assignments)
* [Contacts](#contacts)
* [Delivery of the Learning Module](#delivery-of-the-learning-module)
* [Schedule](#schedule)
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

This module introduces the skills required to design, implement and test logistic regression and classification, as well as validate it with resampling. The module compares the differences between modelling for prediction purposes and inference. It explores the choices between prediction accuracy and model interpretability, and the bias-variance trade-off. 

## Learning Outcomes

By the end of the module, participants will be able to:
- Implement and interpret the results from several supervised learning approaches for **classification and regression**.
- Use **resampling methods** such as cross-validation and bootstrapping to select and evaluate models.
- Determine the **requirements for reproducible machine learning** and ensure consistency across model implementations.
- Analyze the **uncertainties and limitations** associated with model results and understand the **ethical implications** of applying these models in real-world decision-making.
- Effectively explain the **trade-offs and considerations** for various statistical methods to both **technical** and **non-technical** audiences.

## Assignments

Participants should review the [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md) for instructions on how to complete assignments in this module.

[Assignment 1](./02_activities/assignments/assignment_1.ipynb)

[Assignment 2](./02_activities/assignments/assignment_2.ipynb)

[Assignment 3](./02_activities/assignments/assignment_3.ipynb)

**Assignment Due-dates**

| Assessment   | Content                            | Due Date     |
|--------------|------------------------------------|--------------|
| Assignment 1 | Classification (Sessions 1, 2)     | Sep 29 |
| Assignment 2 | Regression (Sessions 3, 4)         | Oct 6    |
| Assignment 3 | Clustering & Resampling (Sessions 5, 6) | Oct 13   |

### Contacts
**Questions can be submitted to the _#cohort-3-help_ channel on Slack**
* Technical Facilitator: **Holly** (She/Her). Emails can be sent to xhonglei2007@gmail.com
* Learning Support Staff: **Kasra** (She/Her). Emails can be sent to vakiloroayaei.kasra@gmail.com
* Learning Support Staff: **Amanda** (She/Her). Emails can be sent to waiyuamanda.ng@mail.utoronto.ca
* Learning Support Staff: **Vishnou** (He/Him). Emails can be sent to vishnouvina@cs.toronto.edu

### Delivery of the Learning Module

This module will include live learning sessions and optional, asynchronous work periods. During live learning sessions, the Technical Facilitator will introduce and explain key concepts and demonstrate core skills. Learning is facilitated during this time. Before and after each live learning session, the instructional team will be available for questions related to the core concepts of the module. Optional work periods are to be used to seek help from peers, the Learning Support team, and to work through the homework and assignments in the learning module, with access to live help. Content is not facilitated, but rather this time should be driven by participants. We encourage participants to come to these work periods with questions and problems to work through. 
 
Participants are encouraged to engage actively during the learning module. They key to developing the core skills in each learning module is through practice. The more participants engage in coding along with the instructional team, and applying the skills in each module, the more likely it is that these skills will solidify. 

The technical facilitator will introduce the concepts through a collaborative live coding session using the Python notebooks found under `/01_materials/slides`. The technical facilitator will upload any live coding files to this repository for any participants to revisit under `./04_this_cohort/live_code`.

## Schedule

| Session | Date       | Topic                                                   | Key Concepts                          |
|---------|------------|---------------------------------------------------------|-------------------------------------|
| 1       | X 🚩     | Key Concepts of Classification                          | Overview of classification, KNN     |
| 2       | X 🚩    | Advanced Classification Techniques                      | KNN classification, cross-validation|
| 3       | X  🚩   | Introduction to Regression                              | Overview of regression, KNN         |
| 4       | X  🚩   | Linear Regression Models                                | Simple linear regression, multiple regression |
| 5       | X  🚩   | Clustering Methods                                      | K-means clustering                  |
| 6       | X  🚩   | Introduction to Statistical Inference                   | Bootstrap resampling |

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
<!-- - [Cheatsheet](./04_cohort_three/additional_resources/05_review_session_material/dsi_emlt_cheat_sheet_2.pdf)
- [Cross Validation - Basic Idea and Steps](./04_cohort_three/additional_resources/05_review_session_material/cross_validation_basic_idea_and_steps.pdf)
- [EMLT Tutorial](./04_cohort_three/additional_resources/05_review_session_material/emlt_tutorials.pdf) -->
- [Introduction to Statistical Learning with Python Documentation (ISLP)](https://islp.readthedocs.io/en/latest/index.html)

### Videos 
- [Introduction to Statistical Learning with Python Video Playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rPP6braWoRt5UCXYZ71GZIQ)

#### Simple Linear Regression
- [Linear Regression, explained in 2 minutes](https://www.youtube.com/watch?v=CtsRRUddV2s)
- [Linear Regression, Clearly Explained!!!](https://www.youtube.com/watch?v=7ArmBVF2dCs&pp=ygUic2ltcGxlIGxpbmVhciByZWdyZXNzaW9uIHN0YXRxdWVzdA%3D%3D)

#### Multiple linear regression, interactions, qualitative predictors
- [Multiple Regression, Clearly Explained!!!](https://www.youtube.com/watch?v=EkAQAi3a4js&pp=ygUic2ltcGxlIGxpbmVhciByZWdyZXNzaW9uIHN0YXRxdWVzdA%3D%3D)

#### Classification (logistic regression, generative models)
<!-- - [Logistic Regression, explained in 3 minutes](https://www.youtube.com/watch?v=EKm0spFxFG4)
- [StatQuest: Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8&list=PLblh5JKOoLUKxzEP5HA2d-Li7IJkHfXSe)
- [StatQuest: Linear Discriminant Analysis (LDA) clearly explained.](https://www.youtube.com/watch?v=azXCzI57Yfc&pp=ygUNTERBIHN0YXRxdWVzdA%3D%3D) -->
- [StatQuest: K-nearest neighbors, Clearly Explained](https://www.youtube.com/watch?v=HVXime0nQeI&pp=ygUNa25uIHN0YXRxdWVzdA%3D%3D)
<!-- - [Naive Bayes, Clearly Explained!!!](https://www.youtube.com/watch?v=O2L2Uv9pdDA&pp=ygUaYmF5ZXMgY2xhc3NpZmllciBzdGF0cXVlc3Q%3D)
- [Generalized Linear Model](https://www.youtube.com/watch?v=SqN-qlQOM5A) -->

#### Resampling methods (CV, bootstrap) and Linear model selection and regularization
<!-- - [Linear Modelling](https://www.youtube.com/watch?v=-inJu1jHqb8) -->
- [Machine Learning Fundamentals: Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw&pp=ygUYdmFsaWRhdGlvbiBzZXQgc3RhdHF1ZXN0)
- [Bootstrapping Main Ideas!!!](https://www.youtube.com/watch?v=Xz0x-8-cgaQ&pp=ygUXYm9vdHN0cmFwcGluZyBzdGF0cXVlc3Q%3D)
- [Bootstrapping Method](https://www.youtube.com/watch?v=uGsf3spCM3Y)
- [$k$-fold Cross Validation](https://www.youtube.com/watch?v=TIgfjmp-4BA)

Alternative Textbook: [Data Science: A First Introduction](https://python.datasciencebook.ca/classification1.html) (Chapters 5-10)

### How to get help
![image](./steps_to_ask_for_help.png)

## Folder Structure

```markdown
.
├── .github
├── .gitignore
├── 01_materials
├── 02_activities
├── 03_instructional_team
├── 04_this_cohort
├── LICENSE
├── README.md
└── steps_to_ask_for_help.png
```

* **.github**: Contains issue templates and pull request templates for the repository.
* **materials**: Module slides (.pdf) used during learning sessions.
* **activities**: Contains graded assignments.
* **instructional_team**: Resources for the instructional team.
* **this_cohort**: Additional materials and resources for this cohort.
* **.gitignore**: Files to exclude from this folder, specified by the Technical Facilitator
* **LICENSE**: The license for this repository.
* **README.md**: This file.
* **steps_to_ask_for_help.png**: Guide on how to ask for help.
