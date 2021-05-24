# Fundamental CRUD Project
## Workoutlist App
# 


* [Brief](#Brief) 
  * [Objetives & Requirements](#)
  * [Project Propsal](#)
* [Architecture](#architecture)
  * [Risk Assessment](#risk-assessment)
  * [Project Management](#trello-board)
  * [Database Structure](#entity-relationship-diagram)
  * [Continuous Integration pipeline](#continuous-integration)
* [Frontend & Testing](#developmentandtesting)
  * [Unit Testing](#unit-testing)
  * [Integration Testing](#unit-testing)
  * [Front-End Design](#front-end)


* [Jenkins](#Jeknins)
  * [Testing with jenkins](#Testing)
* [Future Improvements](#FutureImprovements)

## Brief

### Objective & Requirements
To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

The project requirements are as follows:

* Functioning CRUD application created in Python
* Functioning front-end to website using Flask
* Use of Trello board recording user stories, etc.
* Relational database
* Clear documentation 
* Risk assessment
* Automated tests 
* Fully integrated into a version control system

### Project Proposal
The project idea that i designed is a workoutlist. This will be a one to many relationship with a user and their workouts. Within this application they will be able to implement the CRUD features. I have two databases; User and Workout.

The function of the table (User) allows users to :
* Insert their first name, second name, age and weight


The function of the second table (Workout) allows users to :

* Select a workout from a SelectField and complete the workout through a BooleanField
* They will be able to select from a list of different workouts and complete their workout

The users will also be able to update and delete from their workoutlist


## Architecture

### Risk Assessment
A picture of a detailed risk assesment can be found below. 

![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/RiskAssessmentPic.png)




### Project Managment
I initially started off using Jira to track my progress. I found Jira very hard to use and add userstories, so idecided to switch ovver to Trello which was very simple and effective. Trello board had further advantages aswell as its ease of navigation such as it being very user friendly and free to use.
![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/trelloscreenshot.png)

### Entity Relationship Diagram
I have included teo pictures of a ERD diagram showing the structure of the database.The first picture is a many to many relationship. This was my initial plan however, I found it very difficult to deploy this therefore I instead went for a one to many relationship. The second  picture shows a relationsip with to tables which one a one to many relationship with the foreign key in the workout table. This means that a user is able to have many workouts however a workout can one user.

![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/erd.png)
![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/erd2.png)


### Continous Integration pipeline

The image below is a CI pipeline with nessesary frameworks and services that are assocaited to them. Through automating the inegration process, this allows a quick development to deployment. In other words this usues a visual studio code software on a local repositary which can be easily pushes on to a GitHub.The following code is recieved in Jenkins via  Webhook which can then test for coverage and allows it to be created on the cloud virtual machine. From here, Unit and Integration tests are automatically run and test reports are produced. The programmer can can evaluate assess the report and make any adjustments to the softare where needed.

![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/CIPIPELINE.png)

## Frontend 

A functioning front-end website and integrated API's, using Flask was used in the project to create a CRUD website.

Home Page
![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/HOME.png)
</br>
Create page

![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/CREATE.png)
</br>
Addworkout page

![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/WORKOUTLIST.png)

</br>
Update Page

![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/WORKOUTLIST.png)

</br>
Delete Page

![pic]()


## Testing Through Jenkins

### Unit Testing
Unit testing allows for a multiple of individual functions to be put to test in various scenarios.




### Integration Testing
Integration testing  is a level of software testing where individual units / components are combined and tested as a group. The purpose of this level of testing is to expose faults in the interaction between integrated units.


###  Test Results
Below is a image of my unit test where 6 tests passed out of a total 8.

I was unable to pass any tests for integration testing.

![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/83%25%20unit%20test%20pass.png)



### Testing with Jenkins
Below i have attatched multiple images showing of me trying to deploy and test my app through Jenkins.

The test build here will trigger the running of my workoutlist app.

My unit testing failed by two test, so I forced the workoutlist app to build. Through a IF statment. This is a screenshot of my a 78% test pass and build passing sucessfully.

This image shows Jenkins build "workoutlist_app" is running on the Jenkins IP on port 5000 successfully. When the build is cancelled, the app will stop running as exppected.

![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/jenkins1.png)

![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/JENKINS2.png)

![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/JENKINS3TESTREPORT.png)

![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/JENKINSIP5.png)

![pic](https://github.com/armankhanx14/QAPROJECT/blob/master/images/JENKINSTESTREPORT6.png)

## Future Improvements

Throughout this whole project there are several improvements which could be made. Right from the beginning such as having a one to many relationship database to the front/back end and testing of the app. I believe a many to many relationship would habe suited this idea better and I coud have included several variables. Also, I believe I could have improved the back end of the application. For example allowing the 'User' to be able to update and delete the 'UserForm'.

### Acknowledgements
* Ben Hesketh
* Raji Kolluru
