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

Used a sql alchemy database

GET /items
https://clint-restful.herokuapp.com/items
This should return a listen of items, each in json format.



Example Request
/items
curl --location --request GET "https://clint-restful.herokuapp.com/items" \
  --data ""
GET /stores
https://clint-restful.herokuapp.com/stores
This should return a listen of items, each in json format.



Example Request
/stores
curl --location --request GET "https://clint-restful.herokuapp.com/stores" \
  --data ""
GET /items/<name>
https://clint-restful.herokuapp.com/item/<name>
This should return one unique item, cant have duplicates each in json format.

HEADERS
AuthorizationJWT jsonData.access_token

Example Request
/items/<name>
curl --location --request GET "https://clint-restful.herokuapp.com/item/%3Cname%3E" \
  --header "Authorization: JWT jsonData.access_token" \
  --data ""
GET /store/<name>
https://clint-restful.herokuapp.com/store/<name>
This should return one unique item, cant have duplicates each in json format.

HEADERS
AuthorizationJWT jsonData.access_token

Example Request
/store/<name>
curl --location --request GET "https://clint-restful.herokuapp.com/store/%3Cname%3E" \
  --header "Authorization: JWT jsonData.access_token" \
  --data ""
POST /store/<name>
https://clint-restful.herokuapp.com/store/<name>
This should return one unique item, cant have duplicates each in json format.

HEADERS
AuthorizationJWT jsonData.access_token

Example Request
/store/<name>
curl --location --request POST "https://clint-restful.herokuapp.com/store/%3Cname%3E" \
  --header "Authorization: JWT jsonData.access_token"
POST /items/<name>
https://clint-restful.herokuapp.com/item/<name>
This should create one unique item, cant have duplicates otherwise it will fail

HEADERS
Content-Typeapplication/json
BODY
{
	"price": 15.99
}


Example Request
/items/<name>
curl --location --request POST "https://clint-restful.herokuapp.com/item/%3Cname%3E" \
  --header "Content-Type: application/json" \
  --data "{
	\"price\": 15.99
}"
DEL /items/<name>
https://clint-restful.herokuapp.com/item/<name>
This should delete one unique item, item identified by name

HEADERS
Content-Typeapplication/json

Example Request
/items/<name>
curl --location --request DELETE "https://clint-restful.herokuapp.com/item/%3Cname%3E" \
  --data ""
DEL /store/<name> Copy
https://clint-restful.herokuapp.com/store/<name>
This should delete one unique item, item identified by name

HEADERS
Content-Typeapplication/json

Example Request
/store/<name> Copy
curl --location --request DELETE "https://clint-restful.herokuapp.com/store/%3Cname%3E" \
  --data ""
PUT /items/<name>
https://clint-restful.herokuapp.com/item/<name>
This should create one unique item, or update the item it it exists

HEADERS
Content-Typeapplication/json
BODY
{
	"price": 17.99
}


Example Request
/items/<name>
curl --location --request PUT "https://clint-restful.herokuapp.com/item/%3Cname%3E" \
  --header "Content-Type: application/json" \
  --data "{
	\"price\": 17.99
}"
POST /auth
https://clint-restful.herokuapp.com/auth
Gets jwt token from autherization function

HEADERS
Content-Typeapplication/json
BODY
{
	"username": "jose",
	"password": "asdf"
}


Example Request
/auth
curl --location --request POST "https://clint-restful.herokuapp.com/auth" \
  --header "Content-Type: application/json" \
  --data "{
	\"username\": \"jose\",
	\"password\": \"asdf\"
}"
POST /register
https://clint-restful.herokuapp.com/register
Gets jwt token from autherization function

HEADERS
Content-Typeapplication/json
BODY
{
	"username": "jose",
	"password": "asdf"
}


Example Request
/register
curl --location --request POST "https://clint-restful.herokuapp.com/register" \
  --header "Content-Type: application/json" \
  --data "{
	\"username\": \"jose\",
	\"password\": \"asdf\"
}"
