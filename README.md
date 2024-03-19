# Estimation, machine learning and testing

## Contents:
1. [Description](https://github.com/UofT-DSI/estimation_machine_learning_testing#description)
2. [Learning Outcomes](https://github.com/UofT-DSI/estimation_machine_learning_testing#learning-outcomes)
3. [Logistics](https://github.com/UofT-DSI/estimation_machine_learning_testing#logistics)
4. [Class Schedule](https://github.com/UofT-DSI/estimation_machine_learning_testing#class-schedule)
5. [Grading Scheme](https://github.com/UofT-DSI/estimation_machine_learning_testing#grading-scheme)
6. [Acknowledgements](https://github.com/UofT-DSI/estimation_machine_learning_testing#acknowledgements)

## Description
This course provides the intuition and skills required to design, implement, test and validate a variety of supervised learning models. We cover the basics of statistical learning including modelling with the goal of prediction versus inference, prediction accuracy and model interpretability trade-off, and the bias-variance trade-off. Each section of this course will cover a unique set of methods used for supervised learning on real data sets.

## Learning Outcomes
By the end of the course, students will:
1. Understand, implement and interpret the results from several supervised learning approaches for regression and classification
2. Utilize resampling methods to extract more information from a data set and to choose the best model
3. Perform exploratory data analysis for unsupervised learning
4. Understand what is required for reproducible learning
5. Appreciate the uncertainties associated with model results and the ethical consequences of acting on these results
6. Communicate different trade offs and considerations for the statistical methods in their toolkit to both technical and non-technical audiences

## Logistics

### Course Contacts
* Instructor: Kamilah Ebrahim [kamilah.ebrahim@mail.utoronto.ca](kamilah.ebrahim@mail.utoronto.ca)
* TA: Ananya Jha [ananya.jha@mail.utoronto.ca](ananya.jha@mail.utoronto.ca)
* TA : Vishnou Vinayagame [vishnouvina@cs.toronto.edu](vishnouvina@cs.toronto.edu)

### Textbook
This course is based largely on the second edition (2021) of *An Introduction with Statistical Learning with Applications in R* (ISLR2), written by Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani and *An Introduction with Statistical Learning with Applications in Python* (ISLP), written by Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani, and Jonathan Taylor (2023). Students should choose the language they are most familiar with to complete this course. Whether taken in R or Python, the underlying principles of this course remain the same. This course includes all essential materials from the textbooks in our slides and is not required; however, students may find it useful as a reference. The books can be downloaded for free, online, at the [companion website](https://www.statlearning.com/). If preferred, both the [R](https://librarysearch.library.utoronto.ca/discovery/fulldisplay?docid=alma991106106183406196&context=L&vid=01UTORONTO_INST:UTORONTO&lang=en&search_scope=UTL_AND_CI&adaptor=Local%20Search%20Engine&tab=Everything&query=any,contains,An%20Introduction%20to%20Statistical%20Learning&offset=0) and [Python](https://librarysearch.library.utoronto.ca/discovery/fulldisplay?docid=alma991107279624206196&context=L&vid=01UTORONTO_INST:UTORONTO&lang=en&search_scope=UTL_AND_CI&adaptor=Local%20Search%20Engine&tab=Everything&query=any,contains,An%20introduction%20to%20statistical%20learning%20:%20with%20applications%20in%20Python) verions of the books can be purchased, or borrowed from the University of Toronto library in print or online. 

### Technology Requirements
Lectures and tutorials are run synchronously over Zoom. We use R and RStudio and Juypiter Notebooks throughout the course. It is preferrable to have them installed; however, the RStudio IDE may be accessed via the 
the [Posit Cloud](https://posit.cloud/) if preferred (free account required). We will occasionally use [Posit Cloud](https://posit.cloud/) for collaborative coding. 

### Classes
We will have a total of 6 over three weeks, according to the schedule below. Classes are 6 PM - 8:30 PM EST on Tuesday, Wednesday and Thursday, and 9 AM - 11:30 AM EST on Saturdays. Being mindful of online fatigue, there will be one or two brief breaks during each class.

Classes will consist of instruction via prepared slides, and live-coding. All slides will be made available before lectures online. Students should perform coding in real-time, alongside the instructor. Students are encouraged to ask questions at any time. As required, we will use Zoom Whiteboard to work through 'pen and paper'-type questions, and Posit cloud to work through coding puzzles.

### Tutorial
Tutorial sessions are on the same date as each class. Tutorials will take place 30 minutes before and after each session. Tutorial attendance is optional, and organization is unstructured. The tutorial is the best place for questions/issues pertaining to software, homework, and assignments.

## Class Schedule

### Class Topics

| Class | Date                   | Topic                                                                               |  Resources | ISLR2/ISLP Chapter |
|--------|------------------------|-------------------------------------------------------------------------------------|------------| --------|
| 1      | Thursday March 7th    | Key Concepts of Statistical Analysis <br> Simple linear regression       | [Slides](https://github.com/UofT-DSI/06-statistical_learning/blob/main/lessons/6.1-Introduction_to_Statistical_Learning_slides.pdf) | 2
| 2      | Thursday March 14th   | Multiple linear regression, interactions, qualitative predictors <br>                         | [Slides](https://github.com/UofT-DSI/06-statistical_learning/blob/main/lessons/6.2-Linear_Regression_slides.pdf) | 3            
| 3      | Saturday March 16th   | Classification (logistic regression, generative models)                     | [Slides](https://github.com/UofT-DSI/06-statistical_learning/blob/main/lessons/6.3-Classication_slides.pdf) | 4                    
| 4      | Monday March 18th     |  Resampling methods (CV, bootstrap) and Linear model selection and regularization         | [Slides1/2](https://github.com/UofT-DSI/06-statistical_learning/blob/main/lessons/6.4-Resampling_Methods_slides.pdf)[Slides2/2](https://github.com/UofT-DSI/06-statistical_learning/blob/main/lessons/6.5-Linear_Model_Selection_and_Regularisation_slides.pdf)  | 5, 6               
| 5      | Tuesday March 19th      | Review of last session's content                                     | [Slides1/2](https://github.com/UofT-DSI/06-statistical_learning/blob/main/lessons/6.4-Resampling_Methods_slides.pdf)[Slides2/2](https://github.com/UofT-DSI/06-statistical_learning/blob/main/lessons/6.5-Linear_Model_Selection_and_Regularisation_slides.pdf)  | 5, 6       
| 6      | Wednesday March 20th        | Introduction to unsupervised learning                           | [Slides](https://github.com/UofT-DSI/06-statistical_learning/blob/main/lessons/6.10-Unsupervised_Learning_slides.pdf) | 12,13                           

## Grading Scheme

Grading is based on three components: 2 assignments (3rd one is now optional), 3 homework questions (completion only), and class participation. The grading scheme is as follows:

| Assessment       | Number |  Individual Weight | Cumulative Weight
|------------------|--------|--------------------|------------------|
| Assignments      | 2      |  30%               | 60%              |
| Homework         | 3      |  10%               | 30%              | 
| Participation    | NA     |  NA                | 10%              |

**Assignments**

Assignments will cover key statistical concepts and related code implementation. The assignments are to complete according to the schedule below, for a total of 3 assignments, where the 3rd one is optional. Assignments will be introduced in class, can be discussed in tutorial, and questions can be ask of the Instructor and/or TA over email. Assignments are due by 11:59PM on the day they are due. Please arrange for extensions *in advance* with the Instructor or the TAs. Assignments should be submitted through the correct Google Forms link found below following the naming convention `firstname_lastname_a#`.

Assignments can be found in the `Assignments` directory, above. We've included an .html file (knitted Markdown file) for easy reading, as well as Jupyter Notebook files, that can be edited for submission. (To download files, click Raw > Save as.)

Note: If the assignment requires some content we end up not covering in class (i.e., we've fallen behind), it will be removed from the assignment / not be graded (you're welcome to submit answers if you like). Any questions that are removed will be determined and clearly indicated in the class before the assignment is due.

**Assignment Due-dates**

| Assessment        | Content         | Due Date                         | Submission Link |
| ------------------| ----------------|----------------------------------| ------------------ |
| Assignment 1      | Classes 1, 2, 3   |  Sunday March 17, by 11:59PM | Your Drive Folder |  
| Assignment 2      | Classes 4, 5   |  Friday March 22, by 11:59PM     | Your Drive Folder |
| Assignment 3      | Classes 3, 4, 6     |  Optional    | Your Drive Folder |

**Homework**

For each class (with the exception of the first class), one homework question from the ISLR2 textbook will be assigned. The homework question is graded for **completion only** (i.e., an attempted solution receives full marks), and *only 3 questions* are required over the course (i.e., you do not have to submit 2 of them out of the 5 ones). The homework questions will require writing code in Python and are designed to take no more than 20 minutes. Individual feedback is not provided on the weekly homework question by default, but will be discussed in tutorials. Homework questions must be submitted before the beginning of the next class; late submissions will not be graded. Homeworks should be submitted through your Drive Folder following the naming convention firstname_lastname_hw#.  

Homework is as follows (<u>only 3 required, marked for competion only!</u>):

| Assessment        | ISLR2 Question       | ISLP Question       |           Due Date | Submission Link |
| ------------------| ---------------------|----------------------|---------------------| --------------- |
| Homework 1   | Ch 3, pg 123, q8    | Ch 3, pg 129, q8     | Wednesday, March 13 | Your Drive Folder | 
| Homework 2   | Ch 3, pg 123, q9, a-e | Ch 3, pg 129-130, q9, a-e | Friday, March 15 | Your Drive Folder | 
| Homework 3   | Ch 4, pg 193, q13    | Ch 4, pg 196-197, q13 | Sunday, March 17 | Your Drive Folder |
| Homework 4   | Ch 5, pg 221, q6     | Ch 5, pg 226-227, q6 | Tuesday, March 19 | Your Drive Folder |
| Homework 5   | Ch 6, pg ?, q?     | Ch 6, pg 286-287    | Thursday, March 21 | Your Drive Folder |

**Participation**

We hope all members in the course regularly participate. We define participation broadly, and include attendance, asking questions, answering others' questions, participating in discussions, etc.

## Acknowledgements
Rohan Alexander supervised the development of this course. The first slides were developed by Simone Collier. Slides have been created and modified by Navona Calarco and Julia Gallucci for Winter 2023. Materials were re-developed from R to Python by Inessa De Angelis in Fall 2023. This course draws extensively on *An Introduction to Statistical Learning with Applications in R* (2nd edition, 2021), by Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani and *An Introduction to Statistical Learning with Applications in Python* (2023) by Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani, and Jonathan Taylor. The structure of the repos were heavily organized and modified by Vishnou Vinayagame and Daniel Razavi in Winter of 2024.
