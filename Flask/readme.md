
# Flask sites and APis
A mix of sites/Apis I made over time, either to learn or for personal projects. Some of these are old and might not have the lastest versions uploaded yet.

This page will contain a breif overview of each site, with a link to the demo and the specific folder. 

Each site can be cloned and ran locally.


## Live demos 
Each website that is hosted on Heroku goes to sleep 30 mins since its last interaction. Heroku's free tier doesnt keep servers up 24/7, So give it a few seconds the first time you interact with each site. 


Each site uses a Postgress SQl database.


## Personal project - Reddit Sensei
https://redditsensei.com (site is temporaily down)

![alt text](https://i.imgur.com/Rh7kNJI.png "Logo Title Text 1")


Description:
The code is not hosted publically on github since its a personal business project. 

The purpose of this project is to increase your (business or personal) outreach on reddit guaranteeing that you will make it to the front page of the subreddit you want to target. I did this by using an complex chain of technologies to simulate an actual user voting on whatever post or comment you submit. Thes ite is functional, just finishes a few improvements before putting it online again.

Features & Technologies:
- Vue CLI 3 + Webpack + vue-loader for single file Vue components
  * Hot-reload in development
  * Lint-on-save with ESLint (Standard)
  * Stylus CSS preprocessor
  * Vue + vue-router + vuex working together
  * Single Page App
  * Axios
  * Bootstrap css
  * Buefy(Bulma Css/SASS framework)
  * Flexbox

- Progressive Web App
  * App manifest
  * Service worker

- [Created a Crud admin panel](https://github.com/ClintOxx/vuetify-admin-dashboard) 
  * Vuetify
  * CRUD tables 
  * JWT auth with token refresh, blacklisting 
  * User roles 

- Flask
  * Application Factory /w Blueprints
  * Albemic
  * Concurrent Futures Multithreading
  * Flask-SQL Alchemy
  * Postgress SQL
  * Flask-Restlful
  * Celery
  * Redis 
  * JWT
  * automatic email logging
  * pytest(function & unit)
  * Key Generator using Python Secrets module
  * OOP Modular design
  * & more
 
### More info on libraries/dependcies used for frontend

Built With
Dependencies(incomplete list)

| Name| Description | |
|--|--|:--:| 
|[vue]|Progressive JavaScript Framework|🖖
|[vue-cli-3]|️Standard Tooling for Vue.js Development|🛠️
|[vue-router]|Official Router for Vue.js|🚦
|[vuex]|️Centralized State Management for Vue.js|🗃️
|[Buefy]|️Bulma SASS framework + Vue components for Vue.js|📚
|[Vuetify Admin Panel](https://github.com/ClintOxx/vuetify-admin-dashboard) | Crud Admin panel made with vue |📚

[vue]: https://vuejs.org
[vue-router]: https://router.vuejs.org
[vue-cli-3]: https://cli.vuejs.org
[vuex]: https://vuex.vuejs.org
[Buefy]: https://buefy.org/


| Name| Description | |
|--|--|:--:| 
|[stylus-loader]|CSS preprocessor for webpack|🎨
|[vue/cli-plugin-babel]|Compiler for next generation JavaScript|🐠
|[vue/cli-plugin-eslint]|Pluggable JavaScript linter|✍️
|[vue/cli-plugin-pwa]|JavaScript Library for adding support to PWA|📱

[stylus-loader]: https://github.com/shama/stylus-loader
[vue/cli-plugin-babel]: https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel
[vue/cli-plugin-eslint]: https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint
[vue/cli-plugin-pwa]: https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-pwa


## Restful Api

Endpoint base url: https://clint-restful.herokuapp.com/

[Repo link](https://github.com/ClintOxx/Web-Dev/tree/master/Flask/Flask%20Restful%20API)

Description:
These were some Rest apis i made using flask by itself and then using the Flask-Restful module. You can actually ping the api's with a tester like this : https://apitester.com/ . 

[Api endpoint documentation](https://documenter.getpostman.com/view/4768713/S17rvUDQ)


Features & Technologies
- Flask
  - Flask-Restful 
  - sql alchemy 
  - SqLite3 
  - JWT

Request type | Endpoint URL | Description
--- | --- | ---
GET /items | https://clint-restful.herokuapp.com/items | This should return a list of items, each in json format.
GET /stores | https://clint-restful.herokuapp.com/stores | This should return a list of stores, each in json format.
GET /items/<name> | https://clint-restful.herokuapp.com/item/<name> | This should return one unique item, cant have duplicates each in json format.
GET /store/<name> | https://clint-restful.herokuapp.com/store/<name> | This should return one unique item, cant have duplicates each in json format.
POST /store/<name> | https://clint-restful.herokuapp.com/store/<name> | This should create and return one unique item, cant have duplicates each in json format.
POST /items/<name> | https://clint-restful.herokuapp.com/item/<name> | This should create one unique item, cant have duplicates otherwise it will fail
DEL /items/<name> | https://clint-restful.herokuapp.com/item/<name> | This should delete one unique item, item identified by name
DEL /store/<name>  | https://clint-restful.herokuapp.com/store/<name> | This should delete one unique item, item identified by name
PUT /items/<name> | https://clint-restful.herokuapp.com/item/<name> | This should create one unique item, or update the item it it exists
POST /auth | https://clint-restful.herokuapp.com/auth | Gets jwt token from autherization function
POST /register | https://clint-restful.herokuapp.com/register | registers and Gets jwt token from autherization function


## Microblog 

https://clint-flask-microblog.herokuapp.com/index 

[Repo link](https://github.com/ClintOxx/Web-Dev/tree/master/Flask/Microblog)

Default user:pass login:  bob:pass

Description:
The frontend will be updated with React(in progress) and made to look better and more modern, its just a simple blogging platform, not all that different from the twitter app but with more features and a different way of using Flask to set it up.

Features & Technologies

- React.js
  - Redux
  - React-Router
  - Single Page App
- Flask
  - Flask- SQL alchemy
  - Application Factory 
  - Albemic
  - Postgress SQL
  - Flask-Restful
  - Celery
  - Redis 
  - JWT
  - notifications
  & more



## Survey/Questionaire
(Will host on heroku when i have the freetime)

[Repo link](https://github.com/ClintOxx/Web-Dev/tree/master/Flask/survey)

![alt text](https://i.imgur.com/fNTwfxC.png?1 "Logo Title Text 1")

Description:
This is really just a simple single page app that utelizes Vue-Router to handle switching between components to display diferent questions without having to refresh the screen. You can sign up/sign in to create new surveys


Features & Technologies

- Vue.js Cli 2
  - Vuex
  - Vue-Router
-   Vue resource
- Flask
  - JWT
  * Flask-SQL Alchemy
  * Postgress SQL
  * Flask-Restlful


## Terrible Twitter clone 

https://clint-socialnw.herokuapp.com/

[Repo link](https://github.com/ClintOxx/Web-Dev/tree/master/Flask/Social%20Network)

Description:
Originally a portion of this was made by following TeamTreehouse's Build a Social Network with Flask course, I ended up adding more to it. The frontend will be updated with React (in progress) and made to look better and more modern, thinking about if i want to include React-Bootstrap to give it the authentic twitter feel lol.


Features & Technologies

- Flask
- Javascript
- peeweee (ORM)
- SqLite3 


### work in progress 
3. How to use/setup in each projects readme
4. upload latest versions


