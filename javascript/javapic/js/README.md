# Javapic Project

The photo gallery project has a landing page that has a rotating background image in the jumbotron. If users want to see the images in the gallery, they need to join the site via the sign-up form. Once they've signed up, they can see the photo gallery, and select click a photo to see a larger version of it.

# Functionality
- _index.html_
  - background image of the jumbotron change to another image in the folder every 10 seconds
- _join.html_
  - form validation that works in all major browsers (you'll need to deactivate browser validate to check this), had all fields marked "required" required, and all email fields require and check for proper email syntax.
  - any validation errors should be presented clearly to the user so that they may correct them
  - on completion of the form, navigate the user to the gallery, passing their name to the page
- _gallery.html_
  - uses the user's name in slogan 
  - loops through the image folder and display each image in the folder
  - lightbox appears with that image loaded in, when the lightbox is up, is the user clicks anywhere not on the image, the lightbox closes

# Project Files
- index.html
- join.html
- gallery.html
- css/style.css
- images/(pdxcg_01.jpg - pdxcg_60.jpg)
- gallery.js
- index.js
- join.js
