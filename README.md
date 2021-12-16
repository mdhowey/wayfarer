# Wayfarer

## Description

Seagull is a social network that provides travel tips to it's users. Users can authenticate in, add travel tips, view travel tips, and comment on other users travel tips.	

### The tech stack: 
The team and I utilized Bootstrap with Django for frontend, Python for backend, and PostgreSQL for database.

## Usage

### **Sprint 1: Basic Auth & Profiles**

*User is able to:*

1. Navigate to "/" and see a basic splash page with:
  - The name of the website.
  - Links to "Log In" and "Sign Up".

1. Sign up for an account.
2. Log in to their account if they already have one.
3. Be redirected to their public profile page after logging in.
4. On their public profile page, see their name, the current city they have set in their profile, and their join date.
5. See the site-wide header on every page with:
  - A link to "Log Out" if they're logged in.
  - Links to "Log In" and "Sign Up" if they're logged out.

1. Update their profile by making changes to their name and/or current city.
2. See the titles of all the posts they've contributed (start with pre-seeded data).
3. Click on the title of one of their posts and be redirected to a "show" page for that post.
4. View post "show" pages with title, author, and content.


*User is able to:*

1. See a "default" profile photo on their profile page before adding their own photo.
2. Update their profile photo (consider using Paperclip or Uploadcare).
3. See their profile photo next to their posts.

NOT COMPLETED:

4. Receive a welcome email after creating an account.

---

### **Sprint 2: CRUD**

*User is able to:*

1. View the "San Francisco" page (at "/cities/1") including:
  - The site-wi de header.
  - The name of the city.
  - An iconic photo of the city.

1. View a list of posts on the San Francisco page:
  - Sorted by newest first.
  - With the post titles linked to the individual post "show" pages.

1. Use an "Add New Post" button on the San Francisco city page to pull up the new post form.
2. Create a new post for San Francisco.
3. Click "Edit" on ANY individual post, and be redirected to the edit form.
4. Click "delete" on ANY individual post, then:
  - See a pop-up that says: "Are you sure you want to delete #{title}?"
  - If the user confirms, delete the post.

### Bounses:

*NOT COMPLETED:*

1. Visit city pages via pretty urls, like "/cities/san-francisco".
2. Visit user profile pages via pretty urls, like "/users/james".
3. On a city's page:
  - See post content truncated to 1000 characters max, with a link to view more.
  - See a relative published date, e.g. "2 days ago".

---

### **Sprint 3: Validations & Authorization**

*User is able to:*

1. View city pages for "London" and "Gibraltar".
2. Verify that a new post they create is successfully published on the correct city page.

A user CANNOT save invalid data to the database, according to the following rules:

1. A user CANNOT sign up with an email (or username) that is already in use.
2. A post's title must be between 1 and 200 characters.
3. A post's content must not be empty.

A user is authorized to perform certain actions on the site, according to the following rules:

1. A user MUST be logged in to create/update/destroy resources.
2. A user may only edit their own profile and edit/delete their own posts.

*Bounses:*

1. View an error message when form validations fail, for the following validations:
  - Title must be between 1 and 200 characters.
  - Content must not be empty.

*NOT COMPLETED:*

1. View only the 10 most recent posts on a city page (pagination), with
  - A link/button to the "Next" 10.
  - A link/button to the "Previous" 10.
1. See a list of the city pages they've contributed to, on their public profile
2. See the number of posts they've written for each city, next to the city's name in their profile.
3. View all vagabond cities as markers/pins on a map on the site's homepage.
4. Click on a pin on the homepage map and be redirected to the corresponding city page.

---

### **Sprint 4: Commenting**

*User is able to:*

1. Comment on individual posts.
2. See the number of comments a post has on the post's "show" page.
3. See the number of comments they've left, on their public profile.
4. Only add a comment when logged in.
5. Only edit/delete their own comments.

### Technical requirements:

- **Django:** Use Django as the core framework for Python.
- **PostgreSQL:** Use PostgreSQL for your database in development and production.
- **Data Models:** Include at least two data models with associations. (4 total models: Profile(User), Post, City, Comment)
- **Data Validation:** Your application should validate incoming data before entering it into the database.
- **Error Handling:** Forms in your application should also validate data, handle incorrect inputs, and provide user feedback on the client-side.
- **Views:** Use **partials** to follow DRY (Don’t Repeat Yourself) development in your views. (base.html)
- **Home & About Pages:** Create a landing page (homepage) that clearly explains your app's value proposition and guides the user through the "get started" funnel. Create an about page that includes photos and brief bios of your team members.
- **User Experience:** Ensure a pleasing and logical user experience. Use a framework like Bootstrap to enhance and ease your CSS styling. **For this project, please choose a framework other than Bulma**. (Bootstrap)
- **Responsive Design*:** Make sure your app looks great on a phone or tablet.
- **Heroku:** Deploy your app to Heroku. Ensure no app secrets are exposed.
- **Github:** Projects must have a minimum of 60 specific commits. (Just made it...)


**See Roadmap below for more information on the future of the project.

## Support

For any questions regarding this project, please email me directly at dev.howey@gmail.com

## Roadmap

This project started out as a group project for a bootcamp. It is possible that in the future it is expounded upon, this depending solely on the eagerness of other developers. For the time being, the project doesn't have much of a future.

## Contributing

Anyone interested in contributing is welcome to do so. Simply submit a pull request, and it will be reviewed promptly.

Please submit a pull request, and I'll be sure to review it ASAP. I am on GitHub daily.

## Authors and acknowledgment

A sincere thank you to an awesome bootcamp team:

  1) Phil Welsh
  2) Michael Karr
  3) Apoorva Sharma

## License

Apache License, Version 2.0 **

**To review the licensing, please visit https://www.apache.org/licenses/LICENSE-2.0.txt 
