# HackWSU 2017

This repository was created to house the details of the #CodeDetroit challenge at HackWSU 2017

## Goal of the Challenge

The goal is to create a web application that will allow a student or staff to report suspicious activity. The application should have 4 main sections:

- Login Page
- User Registration Page
- Report Suspicious Activity
- Review Suspicious Activity

Each page will leverage an Application Programming Interface (API). That's located at http://wsuhack.flyballlabs.com.

The Login Page has been created for you, which will provide you an example of how to invoke (aka use) the API.  
The API has a set of users and suspicious activity data.

The Graphical User Interface (GUI) for the application can be designed anyway you want.  However, application must do the following: 

- Allow a user to register.  
- Allow a user to login with the username and password they used to register
- Allow a user of type student to report suspicious activity
- Allow a user of type principal to review actvity and to trigger a lockdown of the school, which will notifiy all students and staff of the problem via email

Bonus (gives you a higher probablity to win):

- Use the Twillio API to send SMS (test messages) that notifies students and staff that the school is in lockdown

Tips:

- The data fields have already been defined by the API.  Use the API dashboard at https://wsuhack.flyballlabs.com to look at the data field definitions (aka the schema)


## [The Challenge Details](./challenge)
