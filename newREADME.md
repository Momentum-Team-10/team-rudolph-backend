# Questions API Documentation

## Table of Contents
* General Instructions
* CRUD vs. HTTP Reference
* User Login
* User Log Out
* Register New User
* Retrieve Logged In User Info
* Update Logged In User Info
* Get User Details
* List All Questions
* Add New Question
* Single Question Details
* Delete Question
* Search Questions
* Search Answers

## General Instructions
The base url for all the extensions below is: `https://questions-t10.herokuapp.com/`.
Please be sure to use double quotes ("") for all JSON requests.
Several endpoints require Token Authentication. This is done in the header of the HTTP request, with the following form:
```http
Authentication: Token <token string>
```
Please refer to the documentation for the HTTP request library you are using to ensure the proper syntax.

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
Token authentication required. Should correspond to user being updated. Only include fields meant to be updated.
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

## Get User Details
Integer should be the id of the target user
### Request
```json
GET /user/3/
```
### Response
```json
200 OK
{
	"username": "thomas",
	"bio": null,
	"questions": [
		{
			"pk": 11,
			"title": "Why am I in couples counseling over a pan?",
			"body": "The cast iron skillet had a ton of gunk on it, so I went to town on it with soap and iron wool. What's the big deal?",
			"author": "thomas",
			"votes": 0,
			"created_at": "2021-12-17T11:21:43.613489Z",
			"favorited": [],
			"answered": null
		}
	],
	"answers": [
		{
			"pk": 2,
			"body": "Is it non-stick?",
			"author": "thomas",
			"question": 9,
			"votes": 1,
			"created_at": "2021-12-15T00:19:51.903050Z",
			"favorited": []
		}
	],
	"image_url": null,
	"date_joined": "2021-12-14T22:51:16.121295Z"
}
```

## List All Questions
Body should be empty
### Request
```json
GET /questions/
```
### Response
```json
200 OK
[
	{
		"pk": 10,
		"title": "What does it mean to fold in the cheese?",
		"body": "Do you fold it in half like a piece of paper and drop it in the pot?",
		"author": "admin",
		"votes": 0,
		"answers": [],
		"created_at": "2021-12-15T13:31:42.189621Z",
		"favorited": [],
		"answered": null
	},
    (...)
]
```

## Add New Question
Token authentication required. Title field is required, body field is optional
### Request
```json
POST /questions/
{
    "title": "Why am I in couples counseling over a pan?",
    "body": "The cast iron skillet had a ton of gunk on it, so I went to town on it with soap and iron wool. What's the big deal?"
}
```
### Response
```json
201 Created
{
	"pk": 11,
	"title": "Why am I in couples counseling over a pan?",
	"body": "The cast iron skillet had a ton of gunk on it, so I went to town on it with soap and iron wool. What's the big deal?",
	"author": "thomas",
	"votes": 0,
	"answers": [],
	"created_at": "2021-12-17T11:21:43.613489Z",
	"favorited": [],
	"answered": null
}
```

## Single Question Details
Integer should be the id of the target question
### Request
```json
GET /questions/9/
```
### Response
```json
200 OK
{
	"pk": 9,
	"title": "Why is my knife so dull?",
	"body": "I make sure to run it in the dishwasher after every use...",
	"author": "admin",
	"votes": 1,
	"answers": [
		{
			"pk": 1,
			"body": "You should let it soak at least 30 minutes before you put it in the dishwasher.",
			"author": "james",
			"question": 9,
			"votes": 1,
			"created_at": "2021-12-15T00:19:28.001432Z",
			"favorited": []
		}
	],
	"created_at": "2021-12-15T00:10:31.523378Z",
	"favorited": [],
	"answered": null
}
```

## Update Favorited Field on Question
Token authentication required. If User has already favorited the question, their pk will be removed from the Favorited field.
### Request
```json
PATCH /questions/9/
{
	"favorited": []
}
```
### Response
```json
200 OK
{
	"pk": 10,
	"title": "What does it mean to fold in the cheese?",
	"body": "Do you fold it in half like a piece of paper and drop it in the pot?",
	"author": "admin",
	"votes": 0,
	"answers": [],
	"created_at": "2021-12-15T13:31:42.189621Z",
	"favorited": [
		3
	],
	"answered": null
}
```

## Delete Question
Token authentication required. Authentication should match the author of the question. Body should be empty.
### Request
```json
DELETE /questions/11/
```
### Response
```json
204 No Content
```

## Search Questions
Spaces in search term need to replaced by a +. 
### Request
```json
GET /questions?search=knife
```
### Response
```json
200 OK
[
	{
		"pk": 9,
		"title": "Why is my knife so dull?",
		"body": "I make sure to run it in the dishwasher after every use...",
		"author": "admin",
		"votes": 1,
		"created_at": "2021-12-15T00:10:31.523378Z",
		"favorited": [
			1,
			2,
			3
		],
		"answered": null
	}
]
```

## Search Answers
Spaces in search term need to replaced by a +.
### Request
```json
GET /answers?search=soak
```
### Response
```json
200 OK
[
	{
		"pk": 1,
		"body": "You should let it soak at least 30 minutes before you put it in the dishwasher.",
		"author": "james",
		"question": 9,
		"votes": 1,
		"created_at": "2021-12-15T00:19:28.001432Z",
		"favorited": []
	}
]
```

## Update Favorited Field on Answer
Token authentication required. If User has already favorited the answer, their pk will be removed from the Favorited field.
### Request
```json
PATCH /questions/9/answers/2/
{
	"favorited": []
}
```
### Response
```json
200 OK
{
	"pk": 2,
	"body": "Is it non-stick?",
	"author": "thomas",
	"question": 9,
	"votes": 1,
	"created_at": "2021-12-15T00:19:51.903050Z",
	"favorited": [
		3
	]
}
```