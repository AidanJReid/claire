NB. Still in Construction!

[![Build Status](https://travis-ci.org/AidanJReid/claire.svg?branch=master)](https://travis-ci.org/AidanJReid/claire)

# Claire's Massages - Full Stack eCommerce site offering a range of massage and alternative therapy treatments.

## Table of Contents
1. [**About**](#about)
    - [**Purpose**](#purpose)
2. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
    - [**Wireframes**](#wireframes)
3. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
4. [**Technologies Used**](#technologies-used)
    - [**Version Control**](#version-control)
    - [**Hosting**](#hosting)
    - [**Technologies**](#technologies)
5. [**Testing**](#testing)
    - [**User Journey**](#user-journey)
    - [**General**](#general)
    - [**Validators**](#validators)
    - [**Issues**](#issues)
6. [**Deployment**](#deployment)
7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)

---

## About

This is an ecommerce website (app) for an alternative massage service that enables clients to book and pay for a treatment of ther choosing.
This has been conceived with a real-world application in mind - my sister's fledgling startup side-business. It also is designed for clients
to leave their feedback about treatments and share with the wider community. 

### Purpose

This is the fourth milestone project (of four) of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development studies.
The requirement was 'full-stack site based around business logic used to control a centrally-owned dataset. You will set up an authentication 
mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.'

The external user's goal is to receive a treatment following payment.
The site owner's goal is to earn money for services rendered.

The front end uses HTML, CSS and Javascript. The back end uses Python and Django.

## UX

![Responsiveness Test]()

### User Stories

As a *guest* I want to be able to:
- register an account
- view the selection of treatments
- search for treatments
- filter search treatments

As a *registered user* I want to be able to:
- all the above
- reset my password if forgotten
- post/edit/delete a testimonial against a treatment
- view/edit profile
- make booking in calendar
- add treatment to shopping cart
- purchase treatment

### Design

I wanted the style of the site to be 'light' and reflect the nature of the business which is massage therapy. I researched other sites throughout this
process for style tips and colour patterns and adopted the scheme I did after discussion with the eventual site owner.

- The primary font 'Lato' was chosen because of its aesthetic appeal and I felt it complemented the headings quite well. I also like how the font appeared in the buttons, especially when I applied letter spacing.
- The secondary font 'Bellota' was chosen for the headings because I felt it was stylish and elegant - much like the intended customer market!

### Wireframes

I used **Balsamiq for desktop** wireframes for two reasons:
- Students have free access to the desktop version until the end of 2020.
- I really enjoyed how simple and easy it is to use for mockups especially in conversations with my assigned mentor for brainstorming.

![claire.png](/static/assets/img/claire.png)


## Features

### Existing features

- Deployed a **Sticky navbar | Sidenav** which makes navigation easier for the user, especially on mobile. This displays various links based on user profile,
.e.g. If not logged in (Register, Login, Treatments, Cart); logged in (Logout, Treatments, Cart).Sidenav pops out on small to medium devices (max-width 992 px) 
and contain the aforementioned nav links.
- **Flash message**
- **Login** - enables registered users to login. Username and password are cross-checked against account for verification against details stored in the database.
- **Register** - Allows visitors to register for a free account. Checks included to ensure username and email address don't already exist in the 
database before users are successfully registered. Passwords stored in the database are hashed for security reasons.
- **Logout** - Logged-in users can logout by clicking on appropriate button in the nav/sidenav, whereby their session is ended.
- **Reset Password** - Registered users having difficulty recalling their password can reset it on the login page, whereby the email address associated with their
profile will receive an email with corresponding link to confirm that they want to reset their password (and subsequently choose a new password to overwrite old on in the database)
- **Profile Page** - Unique page detailing user name, email address of account, profile pic and any testimonials that have been posted (with the ability to edit same)
- **Edit Profile** - update profile pic, edit testimonials (if any). (Modal?)
- **Filter** - Either using search for keyword, or by using the radio buttons which filter by body part (for massage).

### Features Left to Implement

- Introduce **blog** for administrator to publish posts in chronological order. Not super-pressing, but a nice-to-have.
- **Pagination** especially as the number of available treatments grow. Now, it's relatively manageable.

## Technologies Used

### Version Control
- [Git](https://git-scm.com/) - I've used Git as a version control system to regularly add and commit changes made to project in Gitpod before committing to Github (and Heroku).
- [GitHub](https://github.com/) - Used to store code in a remote repository, hosting and for successful deployment of site.

### Hosting
- [Heroku](https://www.heroku.com/) - Used as hosting platform to deploy app.

### Technologies
- **HTML**
    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used to structure pages, forms and associated content with user profiles as well as database. 
It also featured in the nav and footer sections of the page.
- **CSS**
    - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- **Bootstrap**
    - [Bootswatch - Cerulean theme](https://bootswatch.com/4/cerulean/bootstrap.min.css) - Apply responsive grid layout framework with associated components and plugins in
    conjunction with my own applied custom stylesheet.
- **JQuery**
    - [jQuery 3.4.1](https://code.jquery.com/jquery/) - Used to improve and simplify Javascript code.
- **Django**
    - [Django](https://www.heroku.com) used as primary Python web framework.
- **Python**    
    - [Python 3.6.7](https://www.python.org/) - Used as the back-end programming language.
- **Stripe API**    
    - [Stripe](https://stripe.com/gb) - As project required ecommerce functionality, Stripe was used for securing payments.
- **PostgreSQL**    
    - Using [PostgreSQL](https://stripe.com/gb) relational database for storage of backend data.
- **Font Awesome**
    - I used the latest [Font Awesome](https://fontawesome.com/) (4.7.0) library primarily because of the wide selection of free options available,
and the ease of inserting them into this project to make the style changes I wanted.
- **Gitpod**
    - [Gitpod](https://www.gitpod.io/) - Used as the dev environment to write code.

## Testing

### User Journey

Testing for each user scenario:

1. **User story 1**: :white_check_mark:


### General

Regular testing was conducted throughout the course of this project, especially before commits to Github.

**Responsive/Mobile-first design** was tested using Chrome developer tools to ensure desired layout was achieved. 
As well as Chrome, I also used Safari (12.0) and Firefox (68.0.2) which collectively successfully affirmed my project's responsiveness.
To test responsiveness, the following mobiles were tested Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 5/SE 6/7/8 Plus X, iPad and iPad Pro. All successfully passed in mobile responsiveness of the page.

### Validators

**HTML**
- [HTML Checker](https://validator.w3.org/).

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

**TRAVIS**
- I used [Travis Continuous Integration](https://travis-ci.org/) to test my code. The subsequent success of this test can be noted at the top of this README.

### Issues


| Number | Issue            | Resolution   |
|--------|------------------|--------------|
|  1  | Security vulnarability with Django 1.11.24  | Fixed - Upgraded Django to 1.11.27  |
|  2  | Pagination  | TBC  |
|  3  |   |   |
|  4  |   |   |
|  5  |   |   |
|  6  |   |   |
|  7  |   |   |
|  8  |   |   |

## Deployment

### Github

Deployed using the Master Branch on hosting platform GitHub Pages. 

The following steps were taken:

  1. 
  2. 
  3. 
  4. 
  5. 

### Heroku

Deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. To implement this project on Heroku, the following steps were taken:

1. Create a **requirements.txt** file so Heroku can install the required dependencies to run the app.
    - `sudo pip3 freeze --local > requirements.txt`
    - My file can be found [here]().
2. Create a **Procfile** to tell Heroku what type of application is being deployed, and how to run it.
    - `echo web: python run.py > Procfile`
    - My file can be found [here]().
3. Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
4. In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables as follows:
    - **IP** : `0.0.0.0`
    - **PORT** : `8080`
5. App should be successfully deployed to Heroku at this point.


## Credits

### Content

### Media

* Responsiveness and device images from [Responsive Design](http://ami.responsivedesign.is/)
* Favicon created at [Favicon.io](https://favicon.io/)
* Logo created at [Logohub.io](https://logohub.io/)
* Image Gallery:
    - 

### Acknowledgements

* Inspiration and structural format for this README from [Travel Tim's oustanding project](https://github.com/TravelTimN/ci-milestone04-dcd)
* Brian Macharia, my CI mentor, for his support and patience.