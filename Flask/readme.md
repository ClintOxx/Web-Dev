
# Flask sites and APis
A mix of sites/Apis I made over time, either to learn or for personal projects. Some of these are old and might not have the lastest versions uploaded yet.

This page will contain a breif overview of each site, with a link to the demo and the specific folder. 

Each site can be cloned and ran locally.


## Live demos 
Each website that is hosted on Heroku goes to sleep 30 mins since its last interaction. Heroku's free tier doesnt keep servers up 24/7, So give it a few seconds the first time you interact with each site. 


Each site uses a Postgress SQl database.


### Personal project - Reddit Sensei
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

- Progressive Web App
  * App manifest
  * Service worker

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
  * OOP Modular design
  * & more
 
## More info on libraries/dependcies used for frontend

### Built With
Dependencies(Vuetify overhaul coming soon)

| Name| Description | |
|--|--|:--:| 
|[vue]|Progressive JavaScript Framework|🖖
|[vue-cli-3]|️Standard Tooling for Vue.js Development|🛠️
|[vue-router]|Official Router for Vue.js|🚦
|[vuex]|️Centralized State Management for Vue.js|🗃️
|[vuetify]|️Material Component Framework for Vue.js|📚

[vue]: https://vuejs.org
[vue-router]: https://router.vuejs.org
[vue-cli-3]: https://cli.vuejs.org
[vuex]: https://vuex.vuejs.org
[vuetify]: https://vuetifyjs.com


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



### Survey/Questionaire
(Will host on heroku when i have the freetime)
https://github.com/ClintOxx/Web-Dev/tree/master/Flask/survey

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



### Microblog 
https://clint-flask-microblog.herokuapp.com/index 
https://github.com/ClintOxx/Web-Dev/tree/master/Flask/Microblog

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

### Restful Api
https://clint-restful.herokuapp.com/
https://github.com/ClintOxx/Web-Dev/tree/master/Flask/Flask%20Restful%20API

Description:
These were some Rest apis i made using flask by itself and then using the Flask-Restful module. You can actually ping the api's with a tester like this : https://apitester.com/ . 

api endpoints documentation:
https://documenter.getpostman.com/view/4768713/S17rvUDQ 

![alt text](https://i.imgur.com/Ju7O9VS.png "Logo Title Text 1")


Features & Technologies
- Flask
  - Flask-Restful 
  - sql alchemy 
  - SqLite3 
  - JWT 


### Terrible Twitter clone 
https://clint-socialnw.herokuapp.com/
https://github.com/ClintOxx/Web-Dev/tree/master/Flask/Social%20Network

Description:
Originally a portion of this was made by following TeamTreehouse's Build a Social Network with Flask course, I ended up adding more to it. The frontend will be updated with Vue (in progress) and made to look better and more modern, thinking about if i want to include Vue-Bootstrap to give it the authentic twitter feel lol.


Features & Technologies

- Flask
- Javascript
- peeweee (ORM)
- SqLite3 


### work in progress 
3. How to use/setup in each projects readme
4. upload latest versions


