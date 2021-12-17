# Questions API Documentation

The base url for all the extensions below is: `https://questions-t10.herokuapp.com/`


## CRUD vs. HTTP Reference
|**CRUD**|**HTTP**|
|:------:|:------:|
|Create|POST|
|Read|GET|
|Update|PUT/PATCH|
|Delete|DELETE|


## User Login
Username and password required
### Request
```json
POST /auth/token/login/
{
    "username": "babish",
    "password": "tinywhisk"
}
```

### Response
```json
200 OK
{
    "auth_token": "heybabyihearthebluesacallintossedsaladandscrambledeggs"
}
```


## User Log Out
Token authentication required, body should be empty
### Request
```json
POST /auth/token/logout/
```

### Response
```json
204 No Content
```


## Register New User
Username, password, and retyped password required
### Request
```json
POST /auth/users/
{
    "username": "chefjohn",
    "password": "cayennepepper",
    "re_password": "cayennepepper"
}
```
### Response
```json
201 Created
{
    "email": "",
    "username": "chefjohn",
    "id": 5
}
```


## Retrieve Logged In User Info
Body should be empty
### Request
```json
GET /auth/users/me/
```
### Response
```json
200 OK
{
    "email": "",
    "username": "sohla",
    "id": 3
}
```


## Update Logged In User Info
Only include fields meant to be updated
### Request
```json
PATCH /auth/users/me/
{
    "bio": "I am 50 years young, travel with my Mandelorian companion, and have a fondness for Bone Broth."
}
```
### Response
```json
200 OK
```


## Get List of All Questions
Body should be empty
### Request
```json
GET /questions/
```
### Response
```json

```







## Database endpoints

|**URL** |**Description**         |**Method**|**Request**   |**Response**     |
|:------:|------------------------|:--------:|:------------:|:---------------:|
|`/questions/`|Getting a list of all questions|`GET`|-|`HTTP_200_OK`<br>JSON list of Question objects with answers nested inside|
|`/questions/`|Adding new question|`POST`|`title`<br>`body`|`HTTP_201_Created`<br>JSON of created question object|
|`/questions/<int:pk>/`|Details of a single Question|`GET`|`HTTP_200_OK`<br>JSON of Question object with specified pk|
|`/questions/<int:pk>/answers/`|List of a question's answers|`GET`|`HTTP_200_OK`<br>JSON list of Answer objects|
|`/questions/<int:pk>/answers/<int:ans>/`|Update a question's Answer object. `pk` is the Question's pk and `ans` is the Answer's pk|`PATCH`|`HTTP_200_OK`<br>JSON of updated Answer object|
|`/user/<int:pk>/answers/`|List of user's answers|`GET`|`HTTP_200_OK`<br>JSON list of Answer objects|