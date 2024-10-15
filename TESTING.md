
# Testing

Return back to the [README.md](README.md) file.

## HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files. All pages were validated on the live website. Were possible pages were validated by address. For pages only available to logged in users the html source code was copied from the browser and validated with the text input option in the validator. The same procedure was used  pages such as "cart" and "checkout" which could only be meaningfully validated were there is some user interaction with the page.

| Page | W3C URL | Screenshot/Validation Method |Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcommunity-appliances-3af27dd26db9.herokuapp.com%2F) | ![screenshot](documentation/testing/images/w3c-home.png) |no errors or warnings|
| Products | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcommunity-appliances-3af27dd26db9.herokuapp.com%2Fproducts%2F) | ![screenshot](documentation/testing/images/w3c-products.png) | no errors or warnings|
| Product Detail | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcommunity-appliances-3af27dd26db9.herokuapp.com%2Fproducts%2F7) | ![screenshot](documentation/testing/images/w3c-product-detail.png) |no errors or warnings|
| Checkout | n/a | text input | error to be investigated ![screenshot](documentation/testing/images/w3c-checkout.png)|
| Cart | n/a | text input | no errors or warnings|
| Checkout Success | n/a | text input | no errors or warnings|
| Profile | n/a | text input | no errors or warnings|
| Order History | n/a | text input | no errors or warnings|
| Volunteers | n/a | text input | no errors or warnings|

## CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot/Validation method | Notes|
| --- | --- | --- | --- |
| base.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcommunity-appliances-3af27dd26db9.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) |![screenshot](documentation/testing/images/w3c-css.png)| no errors, some bootstrap related warnings|
| product.css | n/a |text input| no errors|
| checkout.css | n/a |text input| minor warning about vendor extension|

## Python PEP8 Compatibility

I have used the [CI Python Linter](https://pep8ci.herokuapp.com/)  to check Python code for compatibility with the [PEP8 standard](https://peps.python.org/pep-0008/).

| Python File | Screenshot | Notes |
| --- | --- | --- |
| cart apps.py | ![screenshot](documentation/testing/images/pep-cart-apps.png) | No errors |
| cart contexts.py | ![screenshot](documentation/testing/images/pep-cart-contexts.png) | No errors |
| cart urls.py | ![screenshot](documentation/testing/images/pep-cart-urls.png) | No errors |
| cart views.py | ![screenshot](documentation/testing/images/pep-cart-views.png) | No errors |
| cart views.py | ![screenshot](documentation/testing/images/pep-cart-views.png) | No errors |
| checkout urls.py | ![screenshot](documentation/testing/images/pep-checkout-urls.png) | No errors |
| checkout apps.py | ![screenshot](documentation/testing/images/pep-checkout-apps.png) | No errors |
| checkout forms.py | ![screenshot](documentation/testing/images/pep-checkout-forms.png) | No errors |
| checkout models.py | ![screenshot](documentation/testing/images/pep-checkout-models.png) | No errors |
| checkout signals.py | ![screenshot](documentation/testing/images/pep-checkout-signals.png) | No errors |
| checkout admin.py | ![screenshot](documentation/testing/images/pep-checkout-admin.png) | No errors |
| checkout views.py | ![screenshot](documentation/testing/images/pep-checkout-views.png) | No errors |
| home views.py | ![screenshot](documentation/testing/images/pep-home-views.png) | No errors |
| home urls.py | ![screenshot](documentation/testing/images/pep-home-urls.png) | No errors |
| products admin.py | ![screenshot](documentation/testing/images/pep-products-admin.png) | No errors |
| products models.py | ![screenshot](documentation/testing/images/pep-products-models.png) | No errors |
| products urls.py | ![screenshot](documentation/testing/images/pep-products-urls.png) | No errors |
| products views.py | ![screenshot](documentation/testing/images/pep-products-views.png) | No errors |
| profiles admin.py | ![screenshot](documentation/testing/images/pep-profiles-admin.png) | No errors |
| profiles forms.py | ![screenshot](documentation/testing/images/pep-profiles-forms.png) | No errors |
| profiles models.py | ![screenshot](documentation/testing/images/pep-profiles-models.png) | No errors |
| profiles views.py | ![screenshot](documentation/testing/images/pep-profiles-views.png) | No errors |
| profiles urls.py | ![screenshot](documentation/testing/images/pep-profiles-urls.png) | No errors |
| volunteers admin.py | ![screenshot](documentation/testing/images/pep-volunteers-admin.png) | No errors |
| volunteers forms.py | ![screenshot](documentation/testing/images/pep-volunteers-forms.png) | No errors |
| volunteers models.py | ![screenshot](documentation/testing/images/pep-volunteers-models.png) | No errors |
| volunteers urls.py | ![screenshot](documentation/testing/images/pep-volunteers-urls.png) | No errors |
| volunteers views.py | ![screenshot](documentation/testing/images/pep-volunteers-views.png) | No errors |
| community-appliances custom_storages.py | ![screenshot](documentation/testing/images/pep-custom-storages.png) | No errors |
| community-appliances settings.py | ![screenshot](documentation/testing/images/pep-settings.png) | No errors |
| community-appliances urls.py | ![screenshot](documentation/testing/images/pep-urls.png) | No errors |

## JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.


| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![screenshot](documentation/testing/images/jshint-stripe-js.png) | Undefined Stripe variable from external library |

## Browser Compatibility

I have tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Products | Product Detail | Cart | Checkout | Checkout Success | Profile | Volunteers | Order History | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/images/browser-chrome-home.png) | ![screenshot](documentation/testing/images/browser-chrome-products.png) | ![screenshot](documentation/testing/images/browser-chrome-product-details.png)|![screenshot](documentation/testing/images/browser-chrome-cart.png)|![screenshot](documentation/testing/images/browser-chrome-checkout.png)|![screenshot](documentation/testing/images/browser-chrome-checkout-success.png)|![screenshot](documentation/testing/images/browser-chrome-profile.png)|![screenshot](documentation/testing/images/browser-chrome-volunteers.png)| ![screenshot](documentation/testing/images/browser-chrome-order-history.png)| Works as expected 
| Opera | ![screenshot](documentation/testing/images/browser-opera-home.png) | ![screenshot](documentation/testing/images/browser-opera-products.png) | ![screenshot](documentation/testing/images/browser-opera-product-details.png)|![screenshot](documentation/testing/images/browser-opera-cart.png)|![screenshot](documentation/testing/images/browser-opera-checkout.png)|![screenshot](documentation/testing/images/browser-opera-checkout-success.png)|![screenshot](documentation/testing/images/browser-opera-profile.png)|![screenshot](documentation/testing/images/browser-opera-volunteers.png)| ![screenshot](documentation/testing/images/browser-opera-order-history.png)| Works as expected 
| Firefox | ![screenshot](documentation/testing/images/browser-firefox-home.png) | ![screenshot](documentation/testing/images/browser-firefox-products.png) | ![screenshot](documentation/testing/images/browser-firefox-product-details.png)|![screenshot](documentation/testing/images/browser-firefox-cart.png)|![screenshot](documentation/testing/images/browser-firefox-checkout.png)|![screenshot](documentation/testing/images/browser-firefox-checkout-success.png)|![screenshot](documentation/testing/images/browser-firefox-profile.png)|![screenshot](documentation/testing/images/browser-firefox-volunteers.png)| ![screenshot](documentation/testing/images/browser-firefox-order-history.png)| Works as expected 

## Responsiveness

I have tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Products | Product Detail | Cart | Checkout | Checkout Success | Profile | Volunteers | Order History | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mobile (iPhone SE) Dev Tools| ![screenshot](documentation/testing/images/responsive-mobile-home.png) | ![screenshot](documentation/testing/images/responsive-mobile-products.png) | ![screenshot](documentation/testing/images/responsive-mobile-product-details.png)|![screenshot](documentation/testing/images/responsive-mobile-cart.png)|![screenshot](documentation/testing/images/responsive-mobile-checkout.png)|![screenshot](documentation/testing/images/responsive-mobile-checkout-success.png)|![screenshot](documentation/testing/images/responsive-mobile-profile.png)|![screenshot](documentation/testing/images/responsive-mobile-volunteers.png)| ![screenshot](documentation/testing/images/responsive-mobile-order-history.png)| Works as expected 
| tablet (iPad Mini) Dev Tools| ![screenshot](documentation/testing/images/responsive-tablet-home.png) | ![screenshot](documentation/testing/images/responsive-tablet-products.png) | ![screenshot](documentation/testing/images/responsive-tablet-product-details.png)|![screenshot](documentation/testing/images/responsive-tablet-cart.png)|![screenshot](documentation/testing/images/responsive-tablet-checkout.png)|![screenshot](documentation/testing/images/responsive-tablet-checkout-success.png)|![screenshot](documentation/testing/images/responsive-tablet-profile.png)|![screenshot](documentation/testing/images/responsive-tablet-volunteers.png)| ![screenshot](documentation/testing/images/responsive-tablet-order-history.png)| Works as expected 
| Laptop (real device 1366x768px)| ![screenshot](documentation/testing/images/responsive-laptop-home.png) | ![screenshot](documentation/testing/images/responsive-laptop-products.png) | ![screenshot](documentation/testing/images/responsive-laptop-product-details.png)|![screenshot](documentation/testing/images/responsive-laptop-cart.png)|![screenshot](documentation/testing/images/responsive-laptop-checkout.png)|![screenshot](documentation/testing/images/responsive-laptop-checkout-success.png)|![screenshot](documentation/testing/images/responsive-laptop-profile.png)|![screenshot](documentation/testing/images/responsive-laptop-volunteers.png)| ![screenshot](documentation/testing/images/responsive-laptop-order-history.png)| Works as expected 
| Desktop (dev tools)| ![screenshot](documentation/testing/images/responsive-desktop-home.png) | ![screenshot](documentation/testing/images/responsive-desktop-products.png) | ![screenshot](documentation/testing/images/responsive-desktop-product-details.png)|![screenshot](documentation/testing/images/responsive-desktop-cart.png)|![screenshot](documentation/testing/images/responsive-desktop-checkout.png)|![screenshot](documentation/testing/images/responsive-desktop-checkout-success.png)|![screenshot](documentation/testing/images/responsive-desktop-profile.png)|![screenshot](documentation/testing/images/responsive-desktop-volunteers.png)| ![screenshot](documentation/testing/images/responsive-desktop-order-history.png)| Works as expected 
| 4k (dev tools)| ![screenshot](documentation/testing/images/responsive-4k-home.png) | ![screenshot](documentation/testing/images/responsive-4k-products.png) | ![screenshot](documentation/testing/images/responsive-4k-product-details.png)|![screenshot](documentation/testing/images/responsive-4k-cart.png)|![screenshot](documentation/testing/images/responsive-4k-checkout.png)|![screenshot](documentation/testing/images/responsive-4k-checkout-success.png)|![screenshot](documentation/testing/images/responsive-4k-profile.png)|![screenshot](documentation/testing/images/responsive-4k-volunteers.png)| ![screenshot](documentation/testing/images/responsive-4k-order-history.png)| Works as expected 



## User Story Testing
[User stories](https://github.com/doctorandrewbrown/community-appliances/blob/main/README.md#user-stories) were used to specify a program of manual testing of the app functionality. The manual tests involved going through the steps required by the user stories to check correct functioning.
### [Making Purchases](https://github.com/doctorandrewbrown/community-appliances/blob/main/README.md#making-purchases)
| User Story | Tests |Video/Screenshot | Notes | Pass/Fail |
|:--- | :--- |----| --- | --- |
| As a user I want to view items by category, ordered by condition or price|for each item category order results by price (ascending and descending) or grade A-C (ascending and descending) |[video](https://github.com/user-attachments/assets/bdb8881c-a989-4dcb-b98e-eb9cdb22ecc9) |video shows ordering the "All Appliances" category by price and grade (ascending and descending). Similar tests were conducted for other appliance categories| Pass|
| As a user I want to view detailed information on selected items|for an item selected from the search results user can view enlarged image, product description, condition details and saftey details|[video](https://github.com/user-attachments/assets/cc1e2c15-501b-4106-9856-984904bf13f6) |video shows a product details view with the more detailed information including a product description, a dropdown with condition details, safety details (in this case electrical)| Pass|
| As a user I want to view, add and remove items in my cart |user can view items in cart, add and remove items (with informative messages)|[video](https://github.com/user-attachments/assets/5f6f77a2-1b2b-4207-929f-798829b0e1c7) |video shows items being added and removed from cart with cart total in navbar incrementing and decrementing correctly. User messaging is shown at each stage| Pass|
| As a user I want to enter my delivery details and view my cart and payment details at checkout |user should be able to view an itemised breakdown of the cost of their order and any discount. The amount to be charged to the card should be clearly indicated|    ![screenshot](documentation/testing/stories/stories-view-checkout.png) |the screenshot shows an itemised break down of the order with sums correctly calculated and clearly shown. The payment details are again shown in warning text next to the payment button| Pass|
| As a user I want to have a familiar experience making on-line payment for my items and have access to all the relevant details |user should have a familiar payment interface and immediate confirmation of their order |[video](https://github.com/user-attachments/assets/64105a45-ce54-4634-abf8-c325b0b7d204) |video shows payment via a familiar interface provided by Stripe. The user gets immediate confimation that the order has been successfully placed with a breakdown of all the order information. The user is informed they will get an email| Pass|
| As a user I want to get an email confirming my order has been placed. |user should receive email confirmation of their order containing all relevant details |![screenshot](documentation/testing/stories/stories-email.png) |the screen shot shows an example order confirmation email containing all the order details| Pass|

### [Registering for an Account](https://github.com/doctorandrewbrown/community-appliances/blob/main/README.md#registering-for-an-account)
- As a user I want to sign-up for an account to access useful/interesting additional features in the app

This user story was tested by going through the registration process with a temporary email for a fictional user.

|sign-up form|verify email|email confirm link|email confirmed|
| --- | --- | --- | --- |
| ![screenshot](documentation/testing/stories/authentication-signup-form.png)| ![screenshot](documentation/testing/stories/authentication-verify-email.png)| ![screenshot](documentation/testing/stories/authentication-temp-email-link.png)| ![screenshot](documentation/testing/stories/authentication-email-confirmed.png)|


### [Users with an Account](https://github.com/doctorandrewbrown/community-appliances/blob/main/README.md#users-with-an-account)
| User Story | Tests |Video/Screenshot | Notes | Pass/Fail |
|:--- | :--- |----| --- | --- |
| As a user with an account I want to create and update default delivery information to prefill my delivery details into a form at checkout|delivery details form is pre-filled at checkout |[video](https://github.com/user-attachments/assets/9d5e7f7b-8d29-4ce2-99ff-d34ea234b2f3) |video shows form prefilled at checkout once user signs in| Pass |
| |user can edit default delivery details|![screenshot](documentation/testing/stories/stories-account-profile-update.png)| |Pass|
| As a user with an account I want to view a record of previous purchases, ie an order-history|user can view list and detail views of previous orders |[video](https://github.com/user-attachments/assets/0f5d2509-e4b9-4dc5-915d-c0237f1f69d7) |video shows list and detail views to signed in user| Pass |
| As a user with an account I want the option to make a volunteer profile linked to my account, in order to volunteer with the charity|user can create and update a volunteer profile |[video](https://github.com/user-attachments/assets/582e7829-e467-4765-b724-2ed88c07e314) |video shows signed in user editing volunteer profile including toggling 'checkbox to indicate availability| Pass |

### [User Messaging](https://github.com/doctorandrewbrown/community-appliances/blob/main/README.md#user-messaging)
- As a user I want immediate clear feedback messages from interactions with the app

This user story was tested by ensuring messaging was triggered as intended and was informative to the user. Examples of messaging used in the app are shown below

|info| success |warning | error |
| --- | --- | --- | --- |
| ![screenshot](documentation/testing/stories/stories-messages-info.png)  |![screenshot](documentation/testing/stories/stories-messages-success.png)| ![screenshot](documentation/testing/stories/stories-messages-warning.png)| ![screenshot](documentation/testing/stories/stories-messages-error.png)|

### [Managing the Store (Admin User)](https://github.com/doctorandrewbrown/community-appliances/blob/main/README.md#managing-the-store)
- As an admin user I want full CRUD functionality for all models in the application database.

This user story was tested by manually performing create, read, update and delete test actions on each model from within the admin panel. The admin panel screenshots below show the list-view and the change-form for each model.

| app | model| admin list-view| admin change-form | comments |Pass/Fail |
| --- | --- | --- | --- | --- | --- |
| Checkout | Orders | ![screenshot](documentation/testing/stories/stories-admin-orders-list.png) | ![screenshot](documentation/testing/stories/stories-admin-orders-change.png)  | | Pass | 
| Products | Products | ![screenshot](documentation/testing/stories/stories-admin-products-list.png) | ![screenshot](documentation/testing/stories/stories-admin-products-change.png)  | | Pass | 
| Products | Categories | ![screenshot](documentation/testing/stories/stories-admin-categories-list.png) | ![screenshot](documentation/testing/stories/stories-admin-categories-change.png)  | | Pass | 
| Products | Certificates | ![screenshot](documentation/testing/stories/stories-admin-certificates-list.png) | ![screenshot](documentation/testing/stories/stories-admin-certificates-change.png)  | | Pass | 
| Products | Condition | ![screenshot](documentation/testing/stories/stories-admin-condition-list.png) | ![screenshot](documentation/testing/stories/stories-admin-condition-change.png)  | | Pass | 
| Profiles | User profiles | ![screenshot](documentation/testing/stories/stories-admin-profiles-list.png) | ![screenshot](documentation/testing/stories/stories-admin-profiles-change.png)  | | Pass | 
| Volunteers | Volunteer profiles | ![screenshot](documentation/testing/stories/stories-admin-volunteers-list.png) | ![screenshot](documentation/testing/stories/stories-admin-volunteers-change.png)  | The screenshot of the volunteers list view shows a default ordering by "active" volunteers first. This is to improve admin-user experience. The code to give this behaviour is in admin.py file of volunteers app| Pass | 


## Form Validation Tests
Basic form validation was enforced via correct Django "field types" (e.g. EmailField for emails), and "field options" (e.g. blank=False for required fields) when defining models. Manual testing was via entering invalid data into the form, and ensuring the form was not submitted and error messaging was shown. 

Custom form validation was provided for the delivery postcode field in the profile form and the checkout form. This was to ensure only valid delivery postcodes (for the delivery area covered) could be saved to the Order and UserProfile models of the checkout and profiles app respectively. The code for postcode validation is contained in the forms.py files for of the checkout and profiles apps.

The table below shows the test results Pass/Fail for built-in form validation and custom form validation as described above, with example screenshots.


| App | Model |Form| Page | Screenshot | Comments | Pass/Fail|
| --- | --- | --- | --- | --- | --- | --- |
| checkout | Order |OrderForm | checkout |  ![screenshot](documentation/testing/form-validation/form-validation-postcode-error-checkout.png)  | screenshot shows error message if an invalid postcode is submitted in form (see forms.py for postcode validation code)| Pass |
| | | | | ![screenshot](documentation/testing/form-validation/form-validation-email.png)| screenshot shows error message if email format incorrect| |
| profiles | UserProfile |UserProfileForm | profile |  ![screenshot](documentation/testing/form-validation/form-validation-postcode-error-profile.png)  | screenshot shows error message if an invalid postcode is submitted in form (see forms.py for postcode validation code)  | Pass |
| volunteers | VolunteerProfile |VolunteerProfileForm | volunteers |  ![screenshot](documentation/testing/form-validation/form-validation-volunteers.png)  | screenshot shows error message if required field is omitted   | Pass |


## Defensive Programming
Defensive measures were taken to anticipate, and handle all possible user interactions with the application. This is important for user experience (UX) so that users do not get unecessary 500 error messages and all interactions are handled in a graceful and helpful manner. Manual testing of defensive measures was conducted and the results are shown in the table below.

| User Action/Server Error |Expected Result | Screenshot | Comments | Pass/Fail |
| --- | --- | --- | --- | --- |
| requests a non-existant page | trigger 404 error | ![screenshot](documentation/testing/defensive/defensive-404.png)| 404.html file placed in app template directory | Pass |
| non signed-in user requests a page only available to signed-in users | redirect to log-in page | ![screenshot](documentation/testing/defensive/defensive-sign-in.png)| @login_required python decorator used in the views.py files of the profile and volunteers apps | Pass |
| requests forbidden resource | trigger 403 error | ![screenshot](documentation/testing/defensive/defensive-403.png)|example would be a logged in user attempting to view another users order if they have access to the order number e.g. ..../profile/order_history/1D3FED1C1B1849DD93DC698DD92E. Python code to prevent this is in views.py file of the profile app | Pass |
| request contains invalid category parameter in url | trigger no results view | ![screenshot](documentation/testing/defensive/defensive-no-results.png)| code to check for valid category parameter is in views.py of the products app | Pass |
| request contains invalid sort parameter in url | display products with default ordering of price descending | ![screenshot](documentation/testing/defensive/defensive-default-sort.png)| code to check for valid sort parameter is in views.py of the products app | Pass |
| server error | trigger 500 error | ![screenshot](documentation/testing/defensive/defensive-500.png)| 500.html file placed in app template directory| Pass |

## Stripe Payment Testing
Payment testing was conducted by making test purchases in Stripe test mode. Successful test payments could then be observed in the Stripe transactions dashboard.

![screenshot](documentation/testing/images/stripe-test-transactions.png)

## Further Manual Testing
Much of the manual testing of the app has been described [above](https://github.com/doctorandrewbrown/community-appliances/blob/main/TESTING.md#user-story-testing). Additional manual testing is described below.
|  Page | Tests | Result | Notes | Screenshot |
| --- | --- | --- | --- | --- | 
| main navigation - all pages | | | |  | 
|    | clicking the site logo link returns user to home page | Pass |   | ![screenshot](documentation/testing/further-testing/further-testing-main-nav0.png)  |
|    | clicking the cart icon link takes user to cart page | Pass |   |   |
|    | clicking the account icon gives a dropdown with links to register or log-in pages (non signed-in user) and clicking on those links takes the user to the appropriate page| Pass |   | ![screenshot](documentation/testing/further-testing/further-testing-main-nav2.png)  |
|    | clicking the account icon gives a dropdown with links to the profile, volunteers and log-out pages (signed-in user) and clicking on those links takes the user to the appropriate page| Pass |   | ![screenshot](documentation/testing/further-testing/further-testing-main-nav1.png)  |
|    | clicking a product category gives a dropdown with results ordering options and clicking on those links takes the user to the products page showing correctly filtered and ordered results| Pass |   | ![screenshot](documentation/testing/further-testing/further-testing-main-nav-categories.png)  |
| home page | | | |  | 
|    | clicking the "Shop Now" button takes user to products page showing "All Appliances" ordered by price descending | Pass |   | ![screenshot](documentation/testing/further-testing/home-shop-now-button.png)  |
| products page | | | |  | 
|    | clicking on a product card link takes user to details page for product | Pass |   | ![screenshot](documentation/testing/further-testing/products-card-link.png)  |
| products details page | | | |  |
|    | clicking product image link opens large image of product | Pass |   | ![screenshot](documentation/testing/further-testing/products-detail-large-image.png)  |
|    | hover on grade dropdown gives detailed description of product condition| Pass |   | ![screenshot](documentation/testing/further-testing/products-detail-grade-dropdown.png)  |
|    | clicking the "Keep Shopping" button takes user to products page showing "All Appliances" ordered by price descending | Pass |   | ![screenshot](documentation/testing/further-testing/products-detail-keep-shopping-button.png)  |
| cart page | | | |  |
|    | clicking the "Continue Shopping" button takes user to products page showing "All Appliances" ordered by price descending | Pass |   | ![screenshot](documentation/testing/further-testing/cart-link-buttons.png)  |
|    | clicking on the checkout link button takes user to checkout page| Pass |   | ![screenshot](documentation/testing/further-testing/cart-link-buttons.png)  |
| checkout page | | | |  |
|    | checking the form checkbox updates default delivery details in users profile when form is submitted | Pass | signed in user  | ![screenshot](documentation/testing/further-testing/checkout-checbox-signed-in.png)  |
|    | clicking "create an account" and "login" links take user to registration or sign-in pages respectively | Pass | user not logged in  | ![screenshot](documentation/testing/further-testing/checkout-checkbox-signed-out.png)  |
|    | clicking "Adjust Cart" link button takes user back to cart page | Pass | | ![screenshot](documentation/testing/further-testing/checkout-buttons.png)  |
|    | clicking "Complete Order" submits the valid order form | Pass | | ![screenshot](documentation/testing/further-testing/checkout-buttons.png)  |
|    | clicking product image link in order summary takes user back to relevant product details page | Pass | | ![screenshot](documentation/testing/further-testing/checkout-order-summary-image.png)  |
| checkout success page | | | |  |
|    | clicking the "Continue Shopping" button takes user to products page showing "All Appliances" ordered by price descending  | Pass |   | ![screenshot](documentation/testing/further-testing/checkout-success-link-button.png)  |

### Lighthouse Testing
|  Page | Desktop | Mobile | Notes
| --- | --- | --- | --- |
|  home    | ![screenshot](documentation/testing/lighthouse/lighthouse-desktop-home.png)  | ![screenshot](documentation/testing/lighthouse/lighthouse-mobile-home.png)|
|  home    | ![screenshot](documentation/testing/lighthouse/lighthouse-desktop-products.png)  | ![screenshot](documentation/testing/lighthouse/lighthouse-mobile-products.png)|


## Bugs
### Invalid Sort Parameter in url
A bug was observed if the user entered an invalid sort parameter in the url. This would return results filtered by category but not ordered in a meaningful way (i.e. results were returned in database order) which would result in a poor user experience. Code to gaurd against this was included in views.py of the product app. Following checking for one of the valid sort parameters the following code handles invalid sort parameters,

```python

             # default ordering for no valid sortkey in query
            else:
                products = products.order_by('-price')

```

The above code ensures a more user friendly default ordering of products by descending price if a user enters an invalid sort parameter in the url.