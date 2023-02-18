# DSI Course for Statistical Learning

## Contents:
1. [Description](https://github.com/rachaellam/dsi-workshop#description)
2. [Learning Outcomes](https://github.com/rachaellam/dsi-workshop#learning-outcomes)
3. [Logistics](https://github.com/rachaellam/dsi-workshop#logistics)
4. [Marking Scheme](https://github.com/rachaellam/dsi-workshop#marking-scheme)
5. [Policies](https://github.com/rachaellam/dsi-workshop#policies)
6. [Folder Structure](https://github.com/rachaellam/dsi-workshop#folder-structure)
7. [Acknowledgements and Contributions](https://github.com/rachaellam/dsi-workshop#acknowledgements-and-contributions)

## Description:
The course was created by the University of Toronto's Data Science Institute. This course provides the intuition and skills required to design, implement, test and validate a variety of models for supervised learning. To introduce the course, we will cover the basics of statistical learning including modelling with the goal of prediction versus inference, prediction accuracy and model interpretability trade-off, and the all-important bias-variance trade-off. Each section of this course will cover a unique set of methods used for supervised learning on a data set.

This course is designed for those who have a degree in something other than Computer Science/Statistics who are looking to enhance their data science skills for their career.

## Learning Outcomes
Students will know how to...
1. Understand, implement and interpret the results from several supervised learning approaches for regression and classification
2. Utilize resampling methods when appropriate to extract more information from a data set and to choose the best model
3. Perform exploratory data analysis for unsupervised learning
4. Understand what is required for reproducible machine learning
5. Appreciate the uncertainties associated with model results and the ethical consequences of acting on these results
6. recognize who matters in our models

## Logistics

### Course Contacts
* Instructor: Navona Calarco (she/her) [navona.calarco@mail.utoronto.ca](navona.calarco@mail.utoronto.ca)
* TA: Julia Gallucci (she/her) [julia.gallucci@mail.utoronto.ca](julia.gallucci@mail.utoronto.ca)

### Delivery instructions
The course runs synchronously over Zoom. It consists of three classes a week for three weeks (nine classes total). Classes are 6 PM - 8 PM EST on Mondays (with the exception of the first class, moved to Tuesday) and Thursdays, and 9 AM - 12 PM EST on Saturdays. Being mindful of online fatigue, there will be one or two breaks during each class where students are encouraged to stretch, grab a drink and snacks, or ask any additional questions.

Tutorial sessions  will also be offered over Zoom. These will take place from 5 PM - 6 PM EST on Mondays and Thursdays, and 8:30 AM - 9 AM EST and 12 PM - 12:30 PM EST on Saturdays.

### Technology Requirements
1. Computer with internet access
2. R and RStudio installed (preferred), or accessed via the [Posit Cloud](https://posit.cloud/). 
3. Camera is optional although encouraged. 


### Lesson Schedule
| Lesson | Topic                                                                                        | Assignments      | Resources  |
|--------|----------------------------------------------------------------------------------------------|------------------|------------|
| 1      | Unix Shell I <br>(introducing the Shell, introductory commands, files and directories)       | [Assignment 1]() | [Slides]() |
| 2      | Unix Shell II<br>(input/output and pipes/filters)                                            | [Assignment 1]() | [Slides]() |
| 3      | Unix Shell III<br>(shell scripts, shell functions, parameters, flow control)                 | [Assignment 1]() | [Slides]() |
| 4      | Version Control and GitHub I<br>(introducing version control and GitHub, basic Git commands) | [Assignment 2]() | [Slides]() |
| 5      | Version Control and GitHub II<br>(remote repositories; branching)                            | [Assignment 2]() | [Slides]() |
| 6      | Version Control and GitHub III <br>(collaborating, dealing with conflicts)                   | [Assignment 2]() | [Slides]() |
| 7      | Problem solve, reproducibility, ethics, inequity                                             | [Assignment 1]() <br> [Assignment 2]() | [Slides]() |
| 8      | Professional Skills - Industry Case Study                                                    | [Assignment 2]() | [Slides]() |
| 9      | Data Science Foundations - Review and Practice                                               |                  | [Slides]() |

## Marking Scheme
| Assessment       | Weight | Description | Due Date |
|------------------|--------|-------------|----------|
| [Assignment 1]() |        |             |          |
| [Assignment 2]() |        |             |          |
|                  |        |             |          |

## Policies
The course is a live-coding class. Students are expected to follow along with the coding, creating files and folders to navigate and manipulate. Students should be active participants while coding and are encouraged to ask questions throughout. Although slides will be available for students to reference, they should be referenced before or after class, as during class will be dedicated to coding with the instructor.

**How to submit assignments, late policy, academic integrity.**

## Folder Structure
Below are the folders contained in this repo with a description of what they contain and information on how to use them.

### 1 *assignments*:
This folder contains the assignments for the workshop. Students are expected to complete them one week after the content has been delivered.

### 2. *homework*:
This folder contains homework for students to practice Unix and Git/GitHub workshops. Please complete the Unix Shell homework in the first week, and the Git/GitHub homework in the second.

There are pdf copies of the homework and markdown files, which can be edited. The homework can change based on the amount of content that was completed each day.

Homework is just a suggestion but will help students throughout the workshop, as content is cumulative and will only get more difficult. Unfortunately, there is not enough time to review previous content each class so while this homework is **not** graded, it is highly recommended.

### 3. *lessons*:
This folder contains the pdf and html version of the slides. Either the pdf slides or the html slides can be used when teaching. If slides are edited to contain any gifs, the instructor will need to use the html slides so that the gifs are active.

pdf slides should be referenced before class to prepare or after class to review. During class will be live-coding, therefore, there is no need to follow them during class. They contain all information that was discussed in class and are a great resource in the future if students need to reassess their knowledge.

### 4. *post-course*:
This folder contains the exit surveys for students to complete. It holds both the md and docx versions of the survey.

### 5. *slides-resources*:
This folder contains all editable slides. To edit, download the entire folder, including the *pics* folder as this folder contains the pictures which are relationally referenced in the markdown files.

To change a photo, edit the markdown where photos are referenced.

Example: 

Change `![w:1150 center](pics/github.png)` to `![bg](pics/github.png)`

To add a photo, add photo to the *pics* folder and reference it within the markdown file.

Example:

Added photo labelled "git_commit.png" will be referenced in markdown file as `![w:1000 left](pics/git_commit.png)`

## Acknowledgements and Contributions
## Achnowledgements
* Who helped make theses slides
* We wish to acknowledge this land on which the University of Toronto operates. For thousands of years it has been the traditional land of the Huron-Wendat, the Seneca, and most recently, the Mississaugas of the Credit River. Today, this meeting place is still the home to many Indigenous people from across Turtle Island and we are grateful to have the opportunity to work on this land.
### Contributions 
* `bash-git-github` welcomes issues, enhancement requests, and other contributions. To submit an issue, use the [GitHub
issues](https://github.com/anjalisilva/bash-git-github/issues).
