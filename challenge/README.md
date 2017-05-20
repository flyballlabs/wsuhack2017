# WSU-Hackathon

## Setup Your Development Environment

There are a few steps that needs to be done to ensure that you can successfully start working on the challenge.

### Required Software:

- [node.js](https://nodejs.org/en/download/) 
- [git](https://git-scm.com/downloads)

### Instructions for Setting Up Your Environment

1. Firebase will be used to host your application.  Firebase is a Google product.  At least one of your teammates need to have a Google Account.  If not, at least one of your need to create a Google Account by going to [Google](http://google.com) and signing up for a free account.

2. Go to the [Firebase Console](https://console.firebase.google.com/) and create a new project 

- Name the project `suspicious-activity` and click `Add project`.
- Click on "Add App to Project"

3. Open up a Windows Command Window or a Apple Terminal Window and enter "npm"  If you get an error then you need to install node.js.  You can install it by downloading it from [node.js](https://nodejs.org/en/download/)  

4. Create the basic framework for your application by typing in the following commands into your Windows Command Window or Apple Terminal Window:

```
git clone https://github.com/flyballlabs/wsuhack2017/
cd wsu-hackathon/challenge/
mkdir suspicious-activity
npm install firebase -save
npm install -g firebase-tools
firebase login
firebase init
```

 - When you are prompted select `Hosting: Configure and deploy Firebase Hosting sites` make sure to press the "Space bar" to select it 
 - Select your project, which is `suspicious-activity`
 - Hit "Enter" when asked "What do you want to use as your public directory?"
 - Select "n" when asked "Configure as a single-page app (rewrite all urls to /index.html)?"


## Test your environment

```
 cd public
 mv index.html index.html.bak
 echo "<html><h1>Hello HackWSU</h1></html>" > index.html
 firebase deploy
```

Copy your "Project Console" and Hosting URL web address and save them in your browser favorites.

Go to your browser enter in the Hosting URL, which will look something like this: https://suspicious-activity-xxxx.firebaseapp.com.  You should see "Hello HackWSU" on the screen

