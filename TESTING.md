# Testing

This file contains evidence and details of the thorough testing process undertaken for this project.

You can access the [README.md file here](README.md)

## Validation
## Manual Testing (feature testing)
I used the feature section from the README as a guide for the structure for this section. So if you would like to reference any features with the README.md you should be able to do so easily.


### Authentication:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Sign in | Enter valid username and password, click 'Sign in'. | Directed to welcome page. Toast confirming that sign in was successful | ✅ Pass |  |
|  | Enter invalid username or password, click 'Sign in'. | Error message inexplicitly prompts that one of them was incorrect | ✅ Pass |  |
|  | Clicks 'sign-up' | Redirected to the 'Sign Up' page. | ✅ Pass |  |
|  | Clicks 'Forgot your password?' | Redirected to the 'Password Reset' page. | ✅ Pass |  |
|  | Enters valid credentials and checks 'remember me'. | Credentials are prefilled next time user tries to sign in. | ✅ Pass |  |
| Sign up | Clicks 'sign-in' | Redirected to the 'Sign In' page. | ✅ Pass |  |
|  | Enters valid credentials, clicks 'Sign-up' | Verification email sent to user. Redirect to verification page. Toast message confirms verification email is sent to entered email address. | ✅ Pass |  |
|  | Clicks verification link in email | Opens a new 'Confirm Email' page. | ✅ Pass |  |
|  | Clicks 'confirm'. | Redirects to 'Sign-in' page. Toast confirms email address is verified.  | ✅ Pass |  |
|  | User uses knew credentials to sign in | Directed to welcome page. Toast confirming that sign in was successful | ✅ Pass |  |
|  | Clicks 'Sign-up' with empty form fields | Form validation indicates to fill in required fields. | ✅ Pass |  |
|  | Enters username that already exists | Error message explains that that username is taken. | ✅ Pass |  |
|  | Enters incorrect/invalid credentials | Error message explains the error | ✅ Pass |  |
| Sign out confirmation | Clicks 'Sign out'. | Redirected to 'Welcome page'. Toast confirms checkout was successful. | ✅ Pass |  |
 
### All Visitor Features

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Navbar - logo | Hover over logo | Cursor is pointer | ✅ Pass |  |
| --- | Clicks logo | Navigate to Home/Welcome page | ✅ Pass |  |
| Navbar - top section | Hover over search-bar | Cursor is text selector | ✅ Pass |  |
|  | Clicks Search-bar | Input field is highlighted | ✅ Pass |  |
|  | Enters vaid search request | Results matching search request are displayed. | ✅ Pass |  |
|  | Enters invalid search request (empty input field) | All activities displayed. Toast explains no search query was detected. | ✅ Pass |  |
|  | Hover over user icon | Cursor is pointer. Icon turns gold. | ✅ Pass |  |
|  | Clicks user icon (unauthenticated user) | Directed to 'Sign-in' page | ✅ Pass |  |
|  | Clicks user icon (authenticated user) | Directed to 'Profile' page | ✅ Pass |  |
|  | Hover over basket | Cursor is pointer. Icon turns gold. | ✅ Pass |  |
|  | Click basket | Directed to 'Basket' page. | ✅ Pass |  |
| Navbar - bottom section | Hover over lower-nav links | Cursor is pointer. Text turns gold. | ✅ Pass |  |
|  | Click 'Book' dropdown. | Dropdown with list of categories is displayed. | ✅ Pass |  |
|  | Click 'Book' dropdown list option | Directed to 'Activities' page with results for selected category. | ✅ Pass |  |
|  | Click About Link | Directed to 'About' page. | ✅ Pass |  |
|  | Click Trails Link | Directed to 'Trails' page. | ✅ Pass |  |
| Home - Book Visit Section | Hover over category image | Colour change and cursor is pointer | ✅ Pass |  |
|  | Click category image | Directed to 'Activities' page filtered to only display activities within the selected category. | ✅ Pass |  |
|  | Hover over category 'find out more!' button | Colour change and cursor is pointer | ✅ Pass |  |
|  | Click category 'find out more!' button | Directed to 'Activities' page filtered to only display activities within the selected category. | ✅ Pass |  |
| Home - 'First time here' section  | Hover over 'Show me the trails' | Colour change and cursor is pointer | ✅ Pass |  |
|  | Click 'Show me the trails' | Directed to 'Trails' page. | ✅ Pass |  |
|  | Hover over 'Find out more' | Colour change and cursor is pointer | ✅ Pass |  |
|  | Click 'Find out more' | Directed to 'About' page. | ✅ Pass |  |
|  | Hover over 'See the requirements' | Colour change and cursor is pointer | ✅ Pass |  |
|  | Click 'See the requirements' | Directed to 'Trails' page. | ✅ Pass |  |
| About | Interaction with embedded map | Expected behaviour as if using Google maps app. | ✅ Pass |  |
|  | No interaction | Marker is located by 'Talybont-on-Usk' and in the center of the map.  | ✅ Pass |  |
| Trails |  |  |  | No interactive features on this page |
| Activities (filtered by query) | Hover over 'sort by' or 'filter' features. | Cursor is pointer. | ✅ Pass |  |
|  | Hover over 'sort by' or 'filter' dropdown. | Cursor is pointer. | ✅ Pass |  |
|  | Click 'sort by' dropdown | Displays options for sorting | ✅ Pass |  |
|  | Click 'sort by' option | Displays activities that were previoulsy visible in selected order | ✅ Pass |  |
|  | Click 'filter' dropdown | Displays options for filtering | ✅ Pass |  |
|  | Click 'filter' option | Displays activities that were previoulsy visible and meet new filter criteria | ✅ Pass |  |
| Activities (unfiltered) | Click 'sort by' option | Displays all activities in selected order | ✅ Pass |  |
|  | Click 'filter' option | Displays all activities meet new filter criteria | ✅ Pass |  |
| Activities | Hover over activity image | Image fade, cursor is pointer, 'book now' button appears. | ✅ Pass |  |
|  | Click activity image | Redirects to appropriate activity details page. | ✅ Pass |  |
| Activity Details | Hover over 'Go Back' button | Colour change. Cursor is pointer. | ✅ Pass |  |
|  | Clicks 'Go back' | Navigate to activities page with same category displayed as before. | ✅ Pass |  |
|  | Hover over 'Equipment Requirements' button | Colour change. Cursor is pointer. | ✅ Pass |  |
|  | Clicks 'Equipment Requirements' | Navigate to Requirements page | ✅ Pass |  |
|  | Hover over 'Select a timeslot' dropdown | Cursor is pointer. | ✅ Pass |  |
|  | Clicks 'Select a timeslot' dropdown | List of timeslots is displayed (all in the future) | ✅ Pass |  |
|  | Fills in book your space form with valid inputs | selected timeslot and quantity added to basket. Toast confirms. Number next to basket increases by 1. | ✅ Pass |  |
|  | Submits form without selecting a timeslot | Prompted to select a timeslot | ✅ Pass |  |
|  | Selects quantity greater than available spaces for thattimeslot | Toast displays error message explaining there are not enough spaces. | ✅ Pass |  |
| Basket | Hover over 'update' button | Cursor is pointer. | ✅ Pass |  |
|  | Changes quantity to valid number and clicks 'update' | Qunatity updated and toast message confirms successful update. Line total and order total values increase. | ✅ Pass |  |
|  | Changes quantity to be higher than available capacity and clicks 'update' | Toast shows error message saying there aren't enough spaces. | ✅ Pass |  |
|  | Hover over 'X' button | Cursor is pointer. | ✅ Pass |  |
|  | Clicks 'X' button | Item is removed from the basket. | ✅ Pass | This would ideally have a delete confirmation but I ran out of time to impliment this. |
|  | Clicks 'Keep shopping' button | Redirect to activities page | ✅ Pass |  |
|  | Clicks 'Secure Checkout' button | Redirect to checkout page | ✅ Pass |  |
| Checkout (Unauthenticated user) | Clicks 'create an account' button | Redirect to sign up page | ✅ Pass |  |
|  | Clicks 'login' button | Redirect to sign in page | ✅ Pass |  |
|  | Fills in form with required fields left empty | Form validation prompts user to fill in required fields | ✅ Pass |  |
|  | Fills in form with invalid content (eg. non-email in email field) | Form validation prompts user to fill in fields correctly | ✅ Pass |  |
|  | Enters invalid card number | Form error message appears explaining the error. | ✅ Pass |  |
|  | Enters valid card number | Loading spinner appears during checkout process. Directed to 'Checkout success' page. Toast confirms the order was successfully processed. Basket is empty. | ✅ Pass |  |
|  | Clicks 'Adjust Basket' button | Directed to basket | ✅ Pass |  |
| Checkout (authenticated user) | Checks save info option after filling in details in form | Details appear in profile > My Details | ✅ Pass |  |
| Checkout Success | Hovers over 'keep shopping' | colour change, cursor is pointer | ✅ Pass |  |
|  | Clicks 'keep shopping' | Directed to 'activities' page | ✅ Pass |  |
| Footer | Hovers over any icon/link | colour change, cursor is pointer | ✅ Pass |  |
|  | Clicks any icon/link | Directs to relevant link in a new window | ✅ Pass |  |
| 404 | Hovers over 'home' button | colour change, cursor is pointer | ✅ Pass |  |
|  | Clicks 'home' button | Directs user to home page | ✅ Pass |  |
| 500 | Hovers over 'home' button | colour change, cursor is pointer | ✅ Pass |  |
|  | Clicks 'home' button | Directs user to home page | ✅ Pass |  |


### Authenticated Visitors

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Profile | Hovers over any of the buttons in 'Manage Accout' list. | Colour change & cursor is pointer | ✅ Pass |  |
|  | Clicks on 'My Details' | Directed to 'User Details' page. | ✅ Pass |  |
|  | Clicks on 'Order History' | Directed to 'Order History' page. | ✅ Pass |  |
|  | Clicks on 'My Reviews' | Directed to 'My Reviews' page. | ✅ Pass |  |
|  | Clicks on 'Sign out' | Directed to 'Sign out' confirmation page. | ✅ Pass |  |
| Manage Details | Clicks on form field | Colour change | ✅ Pass |  |
|  | Makes valid change and hovers clicks 'save and update' | Details are updated. Toast confirms details have changed. Directed to 'Profile' page | ❌ FAIL | Failed on first test. |
|  | Hovers over 'Back to profile' | Colour change and cursor is pointer | ✅ Pass |  |
|  | Clicks 'Back to profile' | Directs to profile page | ✅ Pass |  |
|  | Hovers over 'Change Password' button | Colour change and cursor is pointer | ✅ Pass |  |
|  | Clicks 'Change Password' | Directs user to 'Change Passwrod' page  | ✅ Pass |  |
| Your Orders | Hovers over order number link or review link | Colour change and cursor is pointer | ✅ Pass |  |
|  | Clicks order number link | Directs user to the checkout success screen they saw when completing the booking originally. 'Return to my profile' button should be displayed in checkout success. | ✅ Pass |  |
|  | Hovers over 'Go back' button | Colour change and cursor is pointer | ✅ Pass |  |
|  | Clicks 'Go back' button | Direct to profile | ✅ Pass |  |
|  | Clicks 'Review' button | Direct to 'Add review' page. Should say 'Reviewing: _selected activity_' | ✅ Pass |  |
| Add Review | Submits review without filling in required fields | Form validation error message | ✅ Pass |  |
|  | Submits valid review details and submits | Redirect to 'Your orders'. Toast confirming review was submitted successfully. | ✅ Pass |  |
|  | Clicks 'back to order history' | Redirects to order history page. | ❌ FAIL | Redirects to profile page |
| Reviews | Click delete review | Redirect to delete confirmation | ❌ FAIL | Ideally this would go to a delete confirmation but I ran out of time to impliment this. |
|  | Click 'Go back' | Redirected to profile page | ❌ FAIL | No change |

### Admin

| Page | User Action | Expected Result | PAss/Fail | Comments |
| --- | --- | --- | --- | --- |
| Activity Details | Hover Over any button or link | Colour change and cursor is pointer | ❌ FAIL | The colour of the 'Edit activity text isn't correct. Delete timeslot button doesn't change colour but cursor does change to a pointer. |
|  | Click 'Edit Activity' | Redirects to edit activity page. Activity name should be displayed on the page. Form should be prefilled with activity information. | ✅ Pass | --- |
|  | Click 'Delete Activity' | Redirects to delete activity confirmation page. Activity name should be displayed on the page. | ✅ Pass | --- |
|  | Click 'Go back' button | Redirects to the previous page. | ✅ Pass | --- |
|  | Click 'Add Timeslot' button | Redirects to 'Add timeslot' page with the current activity prefilled. | ✅ Pass | --- |
|  | Click 'Edit timeslot' button |  | ✅ Pass | --- |
|  | Click 'Delete Timeslot' button |  | ✅ Pass | --- |
| Edit Activity | Click 'Go back' button | Return to activity details page | ✅ Pass | --- |
|  | Submit with empty required field | Form validation prompts user to fill field | ✅ Pass | --- |
|  | Submit with invalid values | Error toast is displayed | ✅ Pass |  |
|  | Submit form with all valid fields | Redirect to activity details. Toast message confirms update. Changes appear to be applied in activity details. | ✅ Pass | --- |
|  | Click 'Cancel' button | Redirect to 'activity details' page without implimenting changes. | ✅ Pass | --- |
|  | Click 'Delete Activity' button | Redirect to 'Delete activity confirmation' page which has the details of the current activity. | ✅ Pass | --- |
| Delete Activity Confirmation | Click 'Delete' button | Activity is deleted. Toast confrimation. Redirect to activities page. | ❌ FAIL | Test this with disposable activity |
|  | click 'cancel' | Return to activity details without deleting the activity | ✅ Pass | --- |
| Add Timeslot | Submit with required fields empty | Form validation prompts user to fill empty fields. | ✅ Pass | --- |
|  | Click 'Go back' button | Redirects to the previous page. | ✅ Pass | --- |
|  | Submit with valid fields | Redirects to activity details page. Timeslot can be seen in timeslot list (as long as it is in the future). Toast confirms timeslot was created. | ✅ Pass | --- |
|  | Click 'cancel' | Return to activity details without creating the timeslot | ✅ Pass | --- |
| Edit Timeslot | Click 'Go back' button | Redirects to the previous page. | ✅ Pass | --- |
|  | Submit with valid fields | Redirects to activity details page. Timeslot is be seen to be updated. Toast confirms timeslot was Updated. | ✅ Pass | --- |
|  | Click 'cancel' | Return to activity details without changing the timeslot | ✅ Pass | --- |
|  | click 'Delete' | Redirects to delete timeslot confirmation page | ✅ Pass | --- |
| Delete Timeslot Confirmation | Click 'Go back' button | Redirects to the previous page. | ✅ Pass | --- |
|  | click 'Delete' | Redirects to activity details page. Toast message confirms timeslot is deleted. Timeslot doesn't appear in timeslot list. | ✅ Pass | --- |
|  | Click 'cancel' | Return to activity details without deleteing the timeslot | ✅ Pass | --- |
| Profile | Hovers over any of the buttons in 'Site Management' list. | Colour change & cursor is pointer | ✅ Pass |  |
|  | Clicks on 'Manage Activities' | Directed to 'Manage Activities' page. | ✅ Pass |  |
|  | Clicks on 'Bookings' | Directed to 'Bookings' page. | ✅ Pass |  |
|  | Clicks on 'Sign out' | Directed to 'Sign out' confirmation page. | ✅ Pass |  |
| Manage Activities | Hovers over any link | Colour change and cursor is pointer | ✅ Pass | --- |
|  | Click 'Go back' button | Redirects to the previous page. | ✅ Pass | --- |
|  | Click on activity link | Redirects to the relevant activity details page. | ✅ Pass | --- |
|  | Click 'Edit'link | Redirects to edit activity page. Activity name should be displayed on the page. Form should be prefilled with activity information. | ✅ Pass | --- |
|  | Click 'Add Activity' | Redirects to 'Add activity' page | ✅ Pass | --- |
| Add Activity | Click 'Go back' button | Redirects to the previous page. | ✅ Pass | These should always direct the user to 'Manage activities' page. Update this to do so. |
|  | Submit form with empty required fields | Prompted to fill required fields | ✅ Pass | --- |
|  | Submit with invalid fields | Form validation raises an error which is displayed appropriately. | ✅ Pass | --- |
|  | Submit valid form | Redirect to activity details page. Activity details match those in form. Toast confirms successful creation of an activity. | ✅ Pass | --- |
| Bookings | Click 'Go back' button | Redirects to the previous page. | ✅ Pass | --- |
|  | Select a date with no activity timeslots | No results message displayed | ❌ FAIL | Whole table and sort/filter toptions are removed. |
|  | Select a date that has activity timeslots | Displays timelsot for the selected date.  | ✅ Pass | --- |
|  | Click 'show all future bookings' | All bookings are displayed with the soonest first. | ✅ Pass | --- |
|  | Select an activity to filter by that has timeslots | Timeslots are displayed | ✅ Pass | --- |
|  | Select an activity with no timeslots booked | No results message displayed  | ❌ FAIL | Empty table displayed. |

## User Story Testing

| As a...| I would like...| so that I can ... | Relevant feature | Achieved? |
| ---- | ---- | ---- | ---- | ---- |
| First Time User | to see a navbar with clear and intuitive navigation links | easily navigate the site to find relevant products and information. | The navbar is uncluttered with clear links to key pages. | ✅ Pass |
| | to see information about activities the park offers | identify if the park meets the criteria of a visit. | Activities are displayed with plenty of details to help the user identify if hey meet their requirements. The skill level feature is particularly targetting this user story. | ✅ Pass |
| | to be able to add activities to my basket | checkout at any time after identifying interesting products. | Items are successfully added to the basket and the session. This means the user can come back later to finish their order. | ✅ Pass |
| | to be able to create an account | see my order history and bookings. | Django AllAuth provides user authentication successfully. In the user profile, previous orders and upcoming bookings are diplayed  | ✅ Pass |
| | to be able to sort, filter and search products | find the most suitable products for me easily and quickly. | There is a search bar at the top of the navbar to allow users to easily search for items. On the activity details page, there is the option to further filter and sort the items returned through the search. Furthermore, the 'Book' dropdown on the navbar allows the user to filter activities by category. | ✅ Pass |
| | to see items added to my basket, edit them, and remove them individually | checkout with exactly the products I would like to buy, without having to create a whole new basket. | The basket icon on the right side of the navbar, indicates the number of items in the basket. In the basket the user can see a list of the items they have added. They can also update the quantity and remove the item from their basket. | ✅ Pass |
| | to checkout with the current basket | be sure my space is reserved on the specified activity. | There are multiple checks throughout the ordering process that there are enough spaces for the quantity of a timeslot being booked. Additionally, when a booking is made, the available capacity is reduced by the quantity of that timeslot in the successful booking. All of this ensures that the user has a space reserved on their chosen activity. | ✅ Pass |
| | the checkout process to be secure | be confident and comfortable making the payment. | Stripe is used for secure payments. To ensure the booking process is successful even if the user leaves half way through, I used webhooks. Confirmation is sent to the user by email to further reassure them. | ✅ Pass |
| | to know what abilities the park caters for | look forward to my visit knowing the park is suitable for my skill level.| Activities are displayed with a skill level to reassure the user that it is suitable for them. Additionally, there is a trail map showing the different gradings of trails on offer. | ✅ Pass |
| | to know details about the park that could affect my visit (eg. contact, hours, trails, location) | be sufficiently prepared for my visit.| There is an about page which highlights all the important information for a user's visit. There is even an embedded map with a location pin dropped to help the user locate the park. | ✅ Pass |
| | to receive confirmation of any orders | be sure that they were completed successfully. | Confirmation emails are being sent successfully to the user's email after an order is completed successfully. | ✅ Pass |
| Registered User | to see my upcoming bookings | check I have remembered the details correctly. | Their upcoming bookings are displayed immediately on the profile page so it's easy for them to find. There are further details on the 'Order History' page. | ✅ Pass |
| | to see my previous purchases | order the same product again or find out the details of a booking.| The order history page shows previous bookings with the names of activities. The user is also able to leave a review and see their reviews to remind them what they thought of the activity. | ✅ Pass |
| | to edit my account details | keep using my account with the correct personal information.| Django AllAuth allows the user to change their password. The 'My Details' page allows the user to update their detais. | ❌ FAIL |
| | save my checkout details | checkout more efficiently next time. | If the user is authenticated they can check 'save my details' and their billing information will be saved for the next time they make an order. | ✅ Pass |
| | to sign into an account I have previously created| keep track of purchases and continue to purchase products. | Django's AllAuth ensures the user can sign in to an account they have already created. There is also a forgot password option which allows the user to regain access to an account they have forgotten the details for. | ✅ Pass |
| Site Admin| to have the ability to add, edit and delete activities | ensure users have accurate and up to date information about the activities. | The admin can add, edit and delete all activities. This can be done from the admin's manage activities page or from the activity details page of the relevant activity. | ✅ Pass |
| | to have the ability to add, edit and delete timeslots | manage the number of people on site in advance. | The admin can add, edit and delete all timeslots. This can be done from the admin's manage activities page or from the activity details page of the relevant activity. | ✅ Pass |
| | to see a calender of bookings | prepare staff numbers and equipment in advance. | The admin can see, sort and filter all bookings in the admin side of the site but they are not displayed as a calander. This is a feature I really wanted to implement but didn't have time in the end. | ✅ Pass |

## Lighthouse 
## Compatibility
## Responsiveness
## Bugs
## Assessment criteria checklist