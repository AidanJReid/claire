[![Build Status](https://travis-ci.org/AidanJReid/claire.svg?branch=master)](https://travis-ci.org/AidanJReid/claire)

# Lavender Blue - Full Stack eCommerce site offering a range of massage and alternative therapy treatments.

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
    - [**General**](#general)
    - [**Validators**](#validators)
    - [**Issues**](#issues)
6. [**Deployment**](#deployment)
7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Conclusion**](#conclusion)
    - [**Acknowledgements**](#acknowledgements)

---

## About

This is an ecommerce website (app) for a massage service that enables clients to book and pay for a range of treatments.
This has been conceived with a real-world application in mind - my sister's fledgling startup side-business.

### Purpose

This is the fourth milestone project (of four) of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development studies.
The requirement was for a 'full-stack site based around business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.'

The external user's goal is to receive a treatment following payment.
The site owner's goal is to earn money for services rendered.

The front end uses HTML, CSS and Javascript. The back end uses Python and Django.

## UX

![Responsiveness Test](/static/assets/img/lb.PNG)

### User Stories

As a *guest* I want to be able to:
- register an account :white_check_mark:
- view the selection of treatments :white_check_mark:
- make a manual search for treatments :white_check_mark:

As a *registered user* I want to be able to:
- do all the above, and
- maintain a record of my carted items (in local storage or other) :white_check_mark:
- reset my password if forgotten
- view profile :white_check_mark:
- make booking in calendar :white_check_mark:
- add treatment to shopping cart :white_check_mark:
- purchase treatment :white_check_mark:

### Design

I wanted the style of the site to be 'light' and reflect the nature of the business which is massage therapy. I researched other sites ([1](https://www.dublinwellnesscentre.ie/ "Dublin Wellness Centre"), [2](https://www.thebodywiseclinic.ie/ "BodyWise"), [3](https://dublinholisticmassage.com/ "Dublin Holistic Massage")) throughout this process for style tips and colour patterns and adopted the scheme I did after discussion with the eventual site owner.

- The primary font 'Libre Franklin' was chosen because of its aesthetic appeal and I felt it complemented the headings quite well. I also like how the font appeared in the buttons, especially when I applied letter spacing.
- The font 'Bellota' was chosen for the headings because I felt it was stylish and elegant - much like the intended customer market!

### Wireframes

I used **Balsamiq for desktop** wireframes for two reasons:
- Students have free access to the desktop version until the end of 2020.
- I really enjoyed how simple and easy it is to use for mockups especially in conversations with my assigned mentor for brainstorming. The following mockup was created before a single line of code was written. It evolved from there!

- [Home - no user logged in (xs, sm and md)]()
- [Home - no user logged in (lg and xl)]()
- [Home - user logged in (xs, sm and md)]()
- [Home - user logged in (lg and xl)]()
- [Profile - user logged in (xs, sm and md)]()
- [Profile - user logged in (lg and xl)]()
- [Treatments - user logged in (xs, sm and md)]()
- [Treatments - user logged in (lg, xl)]()
- [Cart - user logged in - something in the cart (xs, sm and md)]()
- [Cart - user logged in - something in the cart (lg, xl)]()
- [Checkout - user logged in (xs, sm and md)]()
- [Checkout - user logged in (lg and xl)]()

## Features

### Existing features

- Deployed a **Sticky navbar | Sidenav** making navigation easier for the user, especially on mobile. This displays various links based on user profile, .e.g. If not logged in (Register, Login, Treatments, Cart); logged in (Logout, Treatments, Cart). Sidenav pops out on small to medium devices (max-width 992 px) 
and contain the aforementioned nav links.
- **Login** - enables registered users to login. Username and password are cross-checked against account for verification against details stored in the database.
- **Register** - Allows visitors to register for a free account. Checks included to ensure username and email address don't already exist in the database before users are successfully registered. Passwords stored in the database are hashed for security reasons.
- **Logout** - Logged-in users can logout by clicking on appropriate button in the nav/sidenav, thereby ending their session.
- **Reset Password** - Registered users having difficulty recalling their password can reset it on the login page, whereby the email address associated with their profile will receive an email with corresponding link to confirm that they want to reset their password (and subsequently choose a new password to overwrite old on in the database).
- **Profile Page** - Unique page detailing user name, email address of account and shopping cart details.
- **Search** - Search for treatment by keyword.

### Features Left to Implement

- **Filter** - Particularly useful for certain symptoms or for specific aches. This would be added as the number of available treatments grow. Now, it's relatively manageable.
- **Product Drill** ability to 'zoom' into treatment, see the various health benefits and perhaps a youtube tutorial showcasing treament.


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
- **Amazon S3**
    - [Amazon S3](https://aws.amazon.com/) - Storing images entered into the database.
- **Boto S3**
    - [Boto S3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Creation, configuration and management of AWS S3.
- **Stripe API**    
    - [Stripe](https://stripe.com/gb) - As project required ecommerce functionality, Stripe was used for securing payments.
- **PostgreSQL**    
    - [PostgreSQL](https://www.postgresql.org/) - Relational database for storage of backend data.
- **Gunicorn**    
    - [Gunicorn](https://pypi.org/project/gunicorn/) - WSGI HTTP Server to help with deployment of Django project to Heroku.
- **Pillow**    
    - [Pillow](https://pillow.readthedocs.io/en/stable/) - Python Imaging Library to process image files for database storage.
- **Psycopg2**    
    - [Psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for Python.
- **Whitenoise**    
    - [Whitenoise](http://whitenoise.evans.io/en/stable/) - Enables web app to serve its own static files.
- **Google Fonts**    
    - [Google Fonts](https://fonts.googleapis.com/) - Custom font (Bellota and Libre Franklin) chosen for styling.
- **Font Awesome**
    - [Font Awesome (4.7.0)](https://fontawesome.com/) library used primarily because of the wide selection of free options available,
and the ease of inserting them into this project to make the style changes I wanted.
- **Gitpod**
    - [Gitpod](https://www.gitpod.io/) - Used as the dev environment to write code.

## Testing

### General

Regular testing was conducted throughout the course of this project, especially before commits to Github.

**Responsive/Mobile-first design** was tested using Chrome developer tools to ensure desired layout was achieved. 
As well as Chrome, I also used Safari (12.0) and Firefox (68.0.2) which collectively successfully affirmed my project's responsiveness.
To test responsiveness, the following mobiles were tested Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 5/SE 6/7/8 Plus X, iPad and iPad Pro. All successfully passed in mobile responsiveness of the page.

### Validators

**HTML**
- [HTML Checker](https://validator.w3.org/) to validate my HTML code.

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate my CSS code.

**TRAVIS**
- I used [Travis Continuous Integration](https://travis-ci.org/) to test my code. The subsequent success of this test can be noted at the top of this README.

### Issues


| Number | Issue            | Resolution   |
|--------|------------------|--------------|
|  1  | Security vulnarability with Django 1.11.24  | Fixed - Upgraded Django to 1.11.27  |
|  2  | Pagination  | Not needed with relative few treatments proferred  |
|  3  | Stripe Confirmation Payment  | This now works after using a sixteen digit number '4242424242424242'. In the tutorial we were advised to use the 11 digit number which, in fact, threw a 402 error. CVV left blank will also permit payment.  |
|  4  | Email password reset  | Not connected to host email  |
|  5  | Booking treatments restricted  | Initially, my 30 day trial using Calendly (API integrated) included all the listed treatments on offer. However, this has expired prior to submitting project. One remains, and at this stage, it should be considered more of a 'nice to have' feature.  |
|  6  | Blank line at top of carousel in mobile  | Adjusted margin-top accordingly  |


## Deployment

### Github

Deployed using the Master Branch on hosting platform GitHub Pages. 

The following steps were taken:

  1. Create a `master` branch in Github repository 
  2. Use Gitpod IDE to build the site
  3. Commit files to the staging area using bash terminal commands: `git status`; `git add (specify directory)`; `git commit -m "add message"`
  4. Push files to the working environment using `git push`, which updates the repository
  5. Publish site from `master` branch using `settings` tab in the main page of the repository, select `source` as `master branch`, then `save`

### Heroku

Deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. To implement this project on Heroku, the following steps were taken:

1. Create a **requirements.txt** file so Heroku can install the required dependencies to run the app.
    - `sudo pip3 freeze --local > requirements.txt`
    - My file can be found [here](https://github.com/AidanJReid/claire/blob/master/requirements.txt).
2. Create a **Procfile** to tell Heroku what type of application is being deployed, and how to run it.
    - `echo web: python run.py > Procfile`
    - My file can be found [here](https://github.com/AidanJReid/claire/blob/master/Procfile).
3. Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
4. In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables as follows:

| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | `<your secret key>`
AWS_SECRET_ACCESS_KEY | `<your secret key>`
AWS_STORAGE_BUCKET_NAME | `<your AWS S3 bucket name>`
DATABASE_URL | `<your postgres database url>`
EMAILJS_USER_ID | `<your secret key>`
HOSTNAME | `<your heroku app hostname>`
SECRET_KEY | `<your secret key>`
STRIPE_CANCEL_URL | `<link to all-products page in your app>`
STRIPE_PUBLISHABLE | `<your secret key>`
STRIPE_SECRET | `<your secret key>`
STRIPE_SUCCESS_URL | `<link to checkout/confirm page in your app>`

5. App should be successfully deployed to Heroku at this point.

6. From the command line of the IDE:
    - Enter heroku postres shell 
    - Migrate the database models 
    - Create a superuser account in the new database
    
     Instructions can be found in the [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql).

7. In the heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch and click "Deploy Branch".

8. Once the build is complete, click the "View app" button.

9. From the (Heroku) link add `/admin` to the end of the url, which gives you key to the Django Admin castle. Log in with your superuser account and create as many instances of Product/Treatments as your heart is content. All stored within the new database 'course.

10. Once these are stored in your database your site will pull on these resources, (hopefully) showing them in the product page.


## Credits

### Content

*  Created with the help of Claire Reid - eventual site owner and masseuse.


### Media

* Responsiveness and device images from [Responsive Design](http://ami.responsivedesign.is/)
* Favicon created at [Favicon.io](https://favicon.io/)
* Image Gallery:
    - Carousel homepage images 
    [1](https://pixabay.com/images/id-1929064/)
    [2](https://pixabay.com/images/id-2768833/)
    [3](https://pixabay.com/images/id-3084952/)
    - [Jumbotron (booking) image](https://unsplash.com/photos/n7a2OJDSZns)
    - Treatments
        - [Back Massage](https://unsplash.com/photos/CEM52sAHR80)
        - [Lymph Drainage](https://unsplash.com/photos/hBLf2nvp-Yc)
        - [Foot and Leg](https://unsplash.com/photos/qeuJczNo54w)
        - [Oncology](https://unsplash.com/photos/0MoF-Fe0w0A)
        - [Pregnancy](https://unsplash.com/photos/NIZeg731LxM)
        - [Neck and Face](https://unsplash.com/photos/RJCslxmvBcs)
        - [Holistic](https://unsplash.com/photos/mCb06TSaab0)

### Conclusion

I learnt a valuable lesson in this milestone. When I started this project I was 6 months into the course and had build much of the back-end which was working successfully. I decided to park the project and spent more time exploring front-end technologies on other mediums. I revisited this project in the final month of my diploma and it was a considerable struggle to 'plug' back into the code again.

In fact, many of the features that were working, in the back end, no longer did! Going back over the tutorials that had guided me effectively
the first time, was to no avail. Those videos that I had built my code on had been replaced by a newer CI project.

Considering the timeframe and work I had already put in, I felt it more prudent to share what I have managed to complete - warts and all.

I've enjoyed the course immensely and it has given me lots of valuable insights which I will carry with me into my coding career.

### Acknowledgements

* Inspiration and structural format for this README from [Travel Tim's oustanding project](https://github.com/TravelTimN/ci-milestone04-dcd), and [AJGreaves mousetastic's project](https://raw.githubusercontent.com/AJGreaves/thehouseofmouse).
* Brian Macharia, my CI mentor, for his support and patience.