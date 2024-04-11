# FastTrack Bike Park

[MOCKUP]

[DEPLOYED SITE](https://fasttrack-bike-park-415cb30571a3.herokuapp.com/)

## Introduction

FastTrack is a fictional bike park invented to act as a subject for an e-commerce site that offers services to a user. This site introduces visitors to the park, providing all the information they would need to visit, as well as allowing them to book activities for their visit. Users can pay for their chosen activities with secure payment through Stripe and receive confirmation emails after completing each order.

The user has the option to create an account before completing an order, which allows them to keep track of their bookings and save personal details to speed up the booking process in the future.

The site offers activities in 4 categories: Day Passes, Courses, Private Coaching and Events. The activities are managed by the admin who has full CRUD capabilities for activities and their timeslots.

I decided to create an e-commerce that provided a service rather than a product, as I wanted to have a go at building a booking system to support the e-commerce site. The admin can set the capacity of each activity, and therefore the available capacity of the timeslot, which updates after each order and ensures timeslots aren't overbooked!


## Project Planning
Planning for this e-commerce site project followed the 5 planes framework for designing and developing a user-centric product.

### **Strategy Plane:** _The Big Picture_
The first step of planning was to decide on a topic for the project. I wanted to create a booking system to practice the concepts and methods that it requires in readiness for a future project I hope to complete. I'm also a keen mountain biker so thought creating a booking website for a mountain bike park would be appropriate and enjoyable!

#### Goals

Once decided on a topic and rough idea, I built on this by identifying my target user and identifying basic goals for them and the business.

##### User Goals 
The target users are mountain bikers who are looking for somewhere to ride downhill trails. Their goal is to visit this e-commerce site and gain information about the bike park to decide if they want to visit. If they find it an appropriate place it visit they should be able to make a booking to secure their position. There should also be a way that they can look up the details of that booking. 

##### Business Goals
Without some benefit to the business there wouldn't be much of a point to developing the site at all. Therefore, I have outlined what the business (the mountain bike park) should be getting from the site.

The site should encourage customers to visit the bike park and reserve spaces through the booking system. This should be a low-intervention way for the business to plan their activity schedule and get an idea of how busy the park will be on certain days. This can help them to organize their staff and make preparations to run their park efficiently.

#### User Stories
With the goals of the project identified, I was able to create user stories that were instrumental in the development of the project.


| As a...| I would like...| so that I can ... | 
|----| ---- | ---- |
| First Time User | to see a navbar with clear and intuitive navigation links | easily navigate the site to find relevant products and information. | 
| | to see information about activities the park offers | identify if the park meets the criteria of a visit. |
| | to be able to add activities to my basket | checkout at any time after identifying interesting products. |
| | to be able to create an account | see my order history and bookings. |
| | to be able to sort, filter and search products | find the most suitable products for me easily and quickly. |
| | to see items added to my basket, edit them, and remove them individually | checkout with exactly the products I would like to buy, without having to create a whole new basket. |
| | to checkout with the current basket | be sure my space is reserved on the specified activity. |
| | the checkout process to be secure | be confident and comfortable making the payment. |
| | to know what abilities the park caters for | look forward to my visit knowing the park is suitable for my skill level.|
| | to know details about the park that could affect my visit (eg. contact, hours, trails, location) | be sufficiently prepared for my visit.|
| | to receive confirmation of any orderS | be sure that they were completed successfully. |
| Registered User | to see my upcoming bookingS | check I have remembered the details correctly. |
| | to see my previous purchaseS | order the same product again or find out the details of a booking.|
| | to edit my account details | keep using my account with the correct personal information.|
| | save my checkout detailS | checkout more efficiently next time. |
| | to sign into an account I have previously created| keep track of purchases and continue to purchase products. |
| Site Admin| to have the ability to add, edit and delete activities | ensure users have accurate and up to date information about the activities. |
| | to have the ability to add, edit and delete timeslotS | manage the number of people on site in advance. |
| | to see a calender of bookings | prepare staff numbers and equipment in advance. |



### **Scope Plane:** _Defining boundaries and features_

#### Agile Methodology
I have approached this project with [agile methodology](https://asana.com/resources/agile-methodology) as I am aware it has a large scope relative to my previous projects and, despite careful planning, I'm not certain of how long it will take to create the MVP and additional features. At least by working in this way, I know I will have a functional product to submit at an early stage of development. This required identifying an MVP before starting the project. My user stories highlight the minimum that I would like to achieve with the site so the MVP was built around these. 


#### 'MoSCoW' Prioritization 
Below you can see a table highlighting the features that I wanted to include in the project. In an attempt to limit scope creep and clearly define the MVP I have prioritized which to include using the [MoSCoW](https://www.techtarget.com/searchsoftwarequality/definition/MoSCoW-method) method. 

- **M**ust have
This will outline the MVP for this project. Anything in the category with be the priority and developed before anything in other MoSCoW categories. 
- **S**hould have
Anything in this category would be beneficial to the project but without it, I would still have a functional site that meets the pass criteria.
- **C**ould have
This category will include the features that I would like to include in the site but have a smaller impact and generally aren't that important. These features will be added at the end of the project if there is enough time. Anything in the category will be noted as a future feature.
- **W**ill not have
I'm including this category so that I can control scope creep. It will help to set the boundaries of the project. 

| Item | Location | Feature | MoSCoW | User |
| --- | --- | --- | --- | --- |
| 1  | Allauth | Register | M | All |
| 2  | Allauth | Login| M | All |
| 3  | Profile Page | Logout | M | All|
| 4  | Allauth | Forgotten Password| M | All |
| 5  | Allauth | Change email | S | All |
| 6  | Activities | Sort Activites | M | All |
| 7  | Activities | Filter ActivitieS | M | All |
| 8  | Activities | Product Cards | M | All |
| 9  | Activities | Rating display on cards | S | All |
| 10 | Activities | Image link to details | M | All |
| 11 | All Pages | Navbar | M | All |
| 12 | Navbar | Access User/Admin Profile | M | Visitor |
| 13 | Navbar | Search Across site | S | All |
| 14 | Navbar | Access Basket| M | Visitor |
| 15 | Navbar/basket icon | Basket display item count | S | Visitor |
| 16 | Navbar | Category Dropdown| S | All |
| 17 | All Pages | Navigation Buttons | M | All |
| 18 | Activity Details | Timeslot selection | M | Visitor |
| 19 | Activity Details | Timeslot as calander | S | Visitor |
| 20 | Activity Details | Select Quantity | M | Visitor |
| 21 | Activity Details | Add to basket| M | Visitor |
| 22 | Activity Details | Rider DetailS | C | Visitor |
| 23 | Basket | Accumulate common items | M | Visitor |
| 24 | Basket | Update quantity| M | Visitor |
| 25 | Basket | Remove from basket| M | Visitor |
| 26 | Activity Details | Check availability before adding to basket | M | Visitor |
| 27 | Basket | Secure checkout button| M | Visitor |
| 28 | Checkout | Billing details forM | M | Visitor |
| 29 | Checkout | Remember Details | M | Visitor |
| 30 | Checkout | Secure checkout with stripe | M | Visitor |
| 31 | Checkout | Loading wheel| S | Visitor |
| 32 | Checkout | confirmation email and toast | M | Visitor |
| 33 | Checkout | Redirect to checkout success | M | Visitor |
| 34 | Checkout Success | Order detial summary | M | Visitor |
| 35 | Checkout Success | Navigation buttons to continue shopping | M | Visitor |
| 36 | User Profile | Upcoming Bookings table | M | Visitor |
| 37 | User Profile | 'Order History' navigation button | M | Visitor |
| 38 | User Profile | 'My Details' navigation button | M | Visitor |
| 39 | All Lists | Empty list messages | M | All |
| 40 | User Profile | Sign Out button | M | All |
| 41 | 'About' dropdown | Minimum requirements page | S | All |
| 42 | 'About' dropdown | Opening Hours | C | All |
| 43 | 'About' dropdown | Contact Info | C | All |
| 44 | 'About' dropdown | Location | C | All |
| 45 | 'About' dropdown | Trail Condition | C | All |
| 46 | 'About' dropdown | Trail Map | C | All |
| 47 | Admin Profile | Manage Activities button| M | Admin |
| 48 | Admin Profile | Manage Users Button | C | Admin |
| 49 | Admin Profile | Manage Bookings Button| C | Admin |
| 50 | Manage Activities | Table of activities | S | Admin |
| 51 | Manage Activities | Filter table by category| S | Admin |
| 52 | Manage Categories/Activities | Edit Category| C | Admin |
| 53 | Manage Activities/Activity Details | Edit Activity| M | Admin |
| 54 | Manage Activities/Activity Details | Delete Activity| M | Admin |
| 55 | Manage Activities/Activities | Add Activity | M | Admin |
| 56 | Manage Activities/Activity Details | Add Timeslot | M | Admin |
| 57 | Activity Details | Delete Timeslot | M | Admin |
| 58 | Activity Details | Edit Timeslot | M | Admin |
| 59 | Throughout | Toasts | M | Admin |
| 60 | Throughout | Tooltips | M | Admin |
| 61 | Throughout | Delete confirmation | M | Admin |
| 62 |  |  |  |  |



#### Time Management with Sprints
I have also broken the project into sprints with soft deadlines to guide me through development. You can see these sprints and a timeline below. The intention is that at the end of a sprint, I will review the work I have completed and test it for bugs and poor UX. I aimed to complete each sprint in full before moving on to the next. 

[INSERT SCHEDULING TABLE HERE]

### **Structure Plane:** _Organizing information and functionality_
For this phase of planning, I thought about the user journey through the site and split the site into 4 categories which I felt needed attention at this stage:

1. Finding the product
2. The checkout process
3. User's Account
4. Admin features

I considered how each of these would work for the user journey and created a flow diagram to illustrate my idea and better understand how it may translate on the site. Here is a summary of my thoughts on each category and you can see how I interpreted them in the flow diagram.

#### 1. Finding the Product
I used the [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) walkthrough project from [Code Institute](https://codeinstitute.net/) as inspiration for many aspects of this project but something that I knew would differ was what the user would be purchasing. As I decided to create a booking system, the user would have to buy a timeslot within an activity. I decided the best way to structure this would be to allow the user to navigate to the activity they wanted to book and then see what timeslots were available. 

#### 2. The Checkout Process
The checkout process in the Boutique Ado project seemed logical and efficient with good UX; it also was very similar to lots of other e-commerce sites I have used so I felt that this was a good structure and sequence of events for my project. 

Something I wanted to consider at this stage was how the user would access their basket to view it. The most intuitive way would be through the navbar so I decided that would be implimented in this project, but I also considered whether it would improve UX by adding a button to naviagte to the basket after adding an activity.

#### 3. User's Account
The user's profile page needs to be straightforward and functional so the user can easily do what they need to. So I thought the clearest way to highlight the different features would be to present the options such as adjusting the profile and viewing bookings as a list with each item navigating to a separate page dedicated to that feature's purpose.

#### 4. Admin features
I had some trouble determining the scope of the admin page due to the excistance of Django's built in admin backend and the full control that offers. But I have decided to limit the admin's control to managing activities and timeslots for the MVP. Similar to the user's account page I decided this should be a navigation page that directs the user to different pages which focus on a specific feature. I think this navigation page is intuitive for the user so should make it easier for them to achieve their goals. 

Both the admin and user pages are available through the main navigation by selecting the user icon. Even the sign out button is located on this page as I felt that adding another drop down in the navbar would be a negative user experience. 

[INSERT FLOW DIAGRAM OF USER JOURNEY HERE]

Take note of the key in the diagram to identify the MVP pages and features compared to extra pages and features.

### **Skeleton Plane:** _Wireframes and Database Schema_

#### Database Schema
I used the [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) project for guidance on the structure of my database schema; I also considered projects by other current and previous [CI](https://codeinstitute.net/) students for inspiration, including:
- [FreeFido by Amy Richardson](https://github.com/amylour/FreeFido_v2)
- [Everneed by Amy Richardson](https://github.com/amylour/everneed)
- [Draw with light by Maria](https://github.com/mariamar95/ms4)
- [Island Bees by Emma Hewson](https://github.com/emmahewson/island-bees/tree/main)
- [Taco y Tequila by Gethin Davies](https://github.com/GethinDavies1990/CI_MS4_DTR)
- [WoWder by my mentor Iuliia Konovalova](https://github.com/IuliiaKonovalova)

I found these projects incredibly useful for seeing different ways of designing a database and also for identifying recurring design features. I found that FreeFido was particularly insightful as it also implements a booking system. 

Having considered my user stories and possible ways to design the database, I decided on the following.

[INSERT DATABASE SCHEMA HERE]

I designed the database to contain the following models:

Categories

Activities

Timeslots

User 

UserProfile

Order

OrderLineItem

Reviews 


#### Wireframes

[INSERT WIREFRAMES HERE]

### **Surface Plane:** _The final look and feel_

#### Design Inspiration
#### Colour Scheme
#### Typography

## Credit
- [FreeFido by Amy Richardson](https://github.com/amylour/FreeFido_v2)
- [Everneed by Amy Richardson](https://github.com/amylour/everneed)
- [Draw with light by Maria](https://github.com/mariamar95/ms4)
- [Island Bees by Emma Hewson](https://github.com/emmahewson/island-bees/tree/main)
- [Taco y Tequila by Gethin Davies](https://github.com/GethinDavies1990/CI_MS4_DTR)
- [WoWder by my mentor Iuliia Konovalova](https://github.com/IuliiaKonovalova)
- [Boutique Ado by Code Institute](https://github.com/Code-Institute-Solutions/boutique_ado_v1)

## Useful links
Saving Env variables in VSCode
https://www.makeuseof.com/django-secret-key-generate-new/

[Stack Overflow Solution](https://stackoverflow.com/questions/49416042/how-to-write-an-f-string-on-multiple-lines-without-introducing-unintended-whites)

[thread on stack overflow](https://stackoverflow.com/questions/52311724/500-error-when-debug-false-with-heroku-and-django)

[DEV](https://dev.to/learndjango/django-static-files-tutorial-1fg7)

[Whitnoise](https://whitenoise.readthedocs.io/en/latest/)


## Images
Private Coaching - Photo by Paige Thompson: https://www.pexels.com/photo/man-wearing-a-green-helmet-sitting-on-a-mountain-bike-13923545/

Group Of bikers - Photo by Mark Soetebier: https://www.pexels.com/photo/group-of-mountain-bikers-parked-near-the-mountains-10743835/


Private Coaching 2 - Photo by Andrew LaBonne: https://www.pexels.com/photo/men-riding-off-road-bicycles-7476445/

Race Shot - Photo by Crys Jardim Fotografia: https://www.pexels.com/photo/man-in-black-and-white-helmet-riding-bicycle-6937088/

Photo by Darcy Lawrey: https://www.pexels.com/photo/photo-of-boy-riding-a-bike-735691/

Photo by Danny Bor: https://www.pexels.com/photo/man-mountain-biking-in-forest-9994278/

Photo by Danny Bor: https://www.pexels.com/photo/man-mountain-biking-in-forest-9994208/

Photo by Amar Preciado: https://www.pexels.com/photo/a-man-riding-bicycle-in-a-forest-12031126/

Photo by Anastasia Shuraeva: https://www.pexels.com/photo/cyclist-jumping-on-ramps-in-the-forest-8926944/

Photo by Jody Parks: https://www.pexels.com/photo/photo-of-person-riding-bicycle-4668487/

Photo by Thomas K: https://www.pexels.com/photo/downhill-cyclist-jumping-in-forest-14625016/

Photo by Javier Piva Flos: https://www.pexels.com/photo/photograph-of-a-man-wit-a-green-helmet-riding-a-bicycle-11049373/

Photo by Sergio Benavides: https://www.pexels.com/photo/cyclist-at-mountain-bike-racing-16066068/

Photo by <a href="https://unsplash.com/@tecreate?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Tom Conway</a> on <a href="https://unsplash.com/photos/four-multicolored-mountain-bikes-parked-beside-brown-wooden-railing-dU2HDmE_tgw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
 
Photo by <a href="https://unsplash.com/@dhika88?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Andhika Soreng</a> on <a href="https://unsplash.com/photos/man-riding-bike-doing-stunt-near-green-trees-during-daytime-US06QF_sxu8?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

Photo by <a href="https://unsplash.com/@lorenzocerato?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Lorenzo Cerato</a> on <a href="https://unsplash.com/photos/two-person-riding-hardtail-bikes-on-trail-1Mdth1sVDbg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
 
Photo by <a href="https://unsplash.com/@timberfoster?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Tim Foster</a> on <a href="https://unsplash.com/photos/man-riding-bike-qrIy8dBzCVU?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
 
Photo by <a href="https://unsplash.com/@nathanael240606?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Nathanaël Desmeules</a> on <a href="https://unsplash.com/photos/man-in-black-helmet-riding-on-bicycle-on-green-grass-field-during-daytime-c7f03aFW5gg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
 
Photo by <a href="https://unsplash.com/@chownyt?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Trevor Chown</a> on <a href="https://unsplash.com/photos/man-riding-on-bicycle-pSq_6oM3rTI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
 
Photo by <a href="https://unsplash.com/@norv952?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Mark Northern</a> on <a href="https://unsplash.com/photos/man-riding-on-gray-full-suspension-mountain-bicycle-during-daytime-qvk8QFyGfWA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
 
Photo by <a href="https://unsplash.com/@pigiama?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Luca Beani</a> on <a href="https://unsplash.com/photos/man-in-black-jacket-riding-on-motocross-dirt-bike-uf9UiWOpYtk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
 
Photo by <a href="https://unsplash.com/@clementdelhaye?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Clement Delhaye</a> on <a href="https://unsplash.com/photos/man-in-red-helmet-riding-on-bicycle-during-daytime-NJQv0W6DHaM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

<a href="https://www.freepik.com/free-photo/young-adult-using-electric-bike-country-side_19124510.htm#fromView=search&page=1&position=18&uuid=332fd06c-baf1-47f9-9d7b-cae53bbd304a">Image by freepik</a>
<a href="https://www.freepik.com/free-photo/man-riding-mountain-bike_11383484.htm#fromView=search&page=1&position=32&uuid=332fd06c-baf1-47f9-9d7b-cae53bbd304a">Image by freepik</a>

Photo by Anastasia Shuraeva: https://www.pexels.com/photo/a-person-riding-a-mountain-bike-in-the-woods-8926958/

Photo by Jonathan Cooper: https://www.pexels.com/photo/a-man-riding-a-bike-in-the-forest-12328608/

Photo by Andrea Crabbi: https://www.pexels.com/photo/person-riding-bicycle-on-dirt-road-5778445/

Photo by Anastasia Shuraeva: https://www.pexels.com/photo/a-person-on-a-mountain-bike-mid-air-8927285/

Photo by Anastasia Shuraeva: https://www.pexels.com/photo/a-person-on-a-mountain-bike-mid-air-8927285/

Photo by Thomas K: https://www.pexels.com/photo/a-man-doing-tricks-using-mountain-bike-15049833/

Photo by Jonathan Cooper: https://www.pexels.com/photo/man-using-a-mountain-bike-in-the-forest-11715051/

Photo by Lars Mai: https://www.pexels.com/photo/man-in-green-helmet-riding-a-bicycle-in-the-forest-3880623/

Photo by Dó Castle: https://www.pexels.com/photo/three-men-riding-on-bicycles-2158963/

Photo by <a href="https://unsplash.com/@thelifeofdev?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Devon Hawkins</a> on <a href="https://unsplash.com/photos/man-riding-motorcycle-on-dirt-road-during-daytime-j5EFEaF4rrk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
 
Photo by <a href="https://unsplash.com/@marcsm?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Marc Sendra Martorell</a> on <a href="https://unsplash.com/photos/man-riding-mountain-bike-ramping-on-forest-gjTiRjM9MFg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
 

## Deployment

### Database
#### Set up your database
I used the free tiny turtle plan with ElephantSQL for this project, but other DBMS can be used. Here is a guide on how to set up a database with ElephantSQL for this project.
1. Create an account or log in at [ElephantSQL.com](https://www.elephantsql.com/)
2. Click 'Create New Instance'.
3. Name your plan and choose your plan. I used Tiny Turtle (Free).
4. Click 'Select Region'.
5. Select the nearest available data center.
6. Click 'Review'.
7. Check the details of the instance you are creating, then click 'Create Instance'.
8. Return to the dashboard to view your instances. 

By clicking on the hyperlinked name of the instance you will be able to see the information required to link this to your project.

#### Connect your database to the project
1. In the terminal, use the command:

 pip3 install dj_database_url==0.5.0 psycopg2

 to install dj_database_url and psycopg2 which are required to connect to the database you have set up. 

2. Update the requirements.txt with:

 pip freeze > requirements.txt

3. In 'settings.py', import dj_database_url below 'import os'.
4. Add your database_url in the 'DATABASES' section, being careful not to commit any secret information.

 [Image of the DATABASES code]

5. In the terminal run the command:

 python manage.py showmigrations

 This should show a list of migrations. If it does, it means you are connected to your database!

6. Migrate to the new database using:

 python manage.py migrate

7. You can then create a new superuser using:

 python manage.py createsuperuser

 Follow the instructions in the terminal to finish creating your superuser.

8. You can check this has been successful by going to your ElephantSQL dashboard, selecting the relevant instance, opening the 'BROWSER' tab and executing options from the table queries dropdown.

### Heroku

#### Create your app in Heroku
1. Log in or create an account on Heroku.
2. Click 'New'.
3. Click 'Create New App'.
4. Name the app and set the region to the closest of the options.
5. Click 'Create App'.
6. When the app is created you can click on it (it should be listed with other apps in your profile page).
7. Go to the 'Settings' tab.
8. 

#### Connecting with Heroku

1. Create a Procfile with the contents:

 web: gunicorn bike_park.wsgi:application

2. In the terminal run the command:

 heroku login

 make sure you have Heroku installed by this point.

3. You should be given a link to open the browser and log in. Follow the instructions in the browser window.
4. Then in the terminal, run:

 heroku config:set DISABLE_COLLECTSTATIC=1 -a 'whatever you named the app in Heroku'

if you would like to temporarily disable 'collect static' when you deploy.

5. In 'settings.py', navigate to the 'ALLOWED_HOSTS' section and add:

 ALLOWED_HOSTS = ['deployed link', 'localhost']



### Cloudinary
useful link: [medium](https://medium.com/@carolgitongaofficial/how-to-use-cloudinary-with-django-cdc998393204)

### Whitenoise
[medium](https://medium.com/@naufal.ihsan21/how-to-serve-static-files-in-django-using-whitenoise-cda11f9bb643)

### Gmail
[Setting up gmail in Django](https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab)