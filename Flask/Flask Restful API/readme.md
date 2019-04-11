# Rest API's that were made with or without using the [Flask Restful package.](https://flask-restful.readthedocs.io/en/latest/)    


## Basic APi
* The basic APi was just an example that isnt as fleshed out
* Doesnt use a database

* Basic api doesnt have much in the way of a front end but you can use PostMan to interact with the api endpoints. 


## Full Rest API
* Currently building a basic frontend for the Full Rest api 
* You can still use Postman to contact the api endpoints
* Uses Sqllite3 locally and Postgress on production server
* made using flask restful

## [Link to APi Docs](https://documenter.getpostman.com/view/4768713/S17rvUDQ)

Used a sql alchemy database



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







