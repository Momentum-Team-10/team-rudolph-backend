# Questions API Documentation

## Table of Contents
* [General Instructions](https://github.com/Momentum-Team-10/team-rudolph-backend#general-instructions)
* [CRUD vs. HTTP Reference](https://github.com/Momentum-Team-10/team-rudolph-backend#crud-vs-http-reference)
* [User Login](https://github.com/Momentum-Team-10/team-rudolph-backend#user-login)
* [User Log Out](https://github.com/Momentum-Team-10/team-rudolph-backend#user-log-out)
* [Register New User](https://github.com/Momentum-Team-10/team-rudolph-backend#register-new-user)
* [Retrieve Logged In User Info](https://github.com/Momentum-Team-10/team-rudolph-backend#retrieve-logged-in-user-info)
* [Update Logged In User Info](https://github.com/Momentum-Team-10/team-rudolph-backend#update-logged-in-user-info)
* [Get User Details](https://github.com/Momentum-Team-10/team-rudolph-backend#get-user-details)
* [List All Questions](https://github.com/Momentum-Team-10/team-rudolph-backend#list-all-questions)
* [Add New Question](https://github.com/Momentum-Team-10/team-rudolph-backend#add-new-question)
* [Single Question Details](https://github.com/Momentum-Team-10/team-rudolph-backend#single-question-details)
* [Update Question's Favorited Field](https://github.com/Momentum-Team-10/team-rudolph-backend#update-questions-favorited-field)
* [Update Question's Accepted Answer](https://github.com/Momentum-Team-10/team-rudolph-backend#update-questions-accepted-answer)
* [Upvote Question](https://github.com/Momentum-Team-10/team-rudolph-backend#upvote-question)
* [Downvote Question](https://github.com/Momentum-Team-10/team-rudolph-backend#downvote-question)
* [Delete Question](https://github.com/Momentum-Team-10/team-rudolph-backend#delete-question)
* [Search Questions](https://github.com/Momentum-Team-10/team-rudolph-backend#search-questions)
* [Add New Answer to Question](https://github.com/Momentum-Team-10/team-rudolph-backend#add-new-answer-to-question)
* [Edit Answer](https://github.com/Momentum-Team-10/team-rudolph-backend#edit-answer)
* [Delete Answer](https://github.com/Momentum-Team-10/team-rudolph-backend#delete-answer)
* [Search Answers](https://github.com/Momentum-Team-10/team-rudolph-backend#search-answers)
* [Update Answer's Favorited Field](https://github.com/Momentum-Team-10/team-rudolph-backend#update-answers-favorited-field)
* [Upvote Question](https://github.com/Momentum-Team-10/team-rudolph-backend#upvote-answer)
* [Downvote Question](https://github.com/Momentum-Team-10/team-rudolph-backend#downvote-answer)

## General Instructions
The base url for all the extensions below is: `https://questions-t10.herokuapp.com/`.
Please be sure to use double quotes ("") for all JSON requests.
Several endpoints require Token Authentication. This is done in the header of the HTTP request, with the following form:
```http
Authentication: "Token <token string>"
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
Username and password required.
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
Token authentication required, body should be empty.
### Request
```json
POST /auth/token/logout/
```
### Response
```json
204 No Content
```

## Register New User
Username, password, and retyped password required.
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
Body should be empty.
### Request
```json
GET /auth/users/me/
```
### Response
```json
200 OK
{
	"username": "thomas",
	"bio": null,
	"questions": [],
	"answers": [
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
	],
	"image_url": null,
	"date_joined": "2021-12-14T22:51:16.121295Z"
}
```

## Update Logged In User Info
Token authentication required. Should correspond to user being updated. Only include fields meant to be updated.
### Request
```json
PATCH /auth/users/me/
{
    "bio": "I like the InstaPot."
}
```
### Response
```json
200 OK
{
	"username": "thomas",
	"bio": "I like the InstaPot.",
	"questions": [],
	"answers": [
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
	],
	"image_url": null,
	"date_joined": "2021-12-14T22:51:16.121295Z"
}
```

## Get User Details
Integer should be the id of the target user. Body should be empty.
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
Body should be empty.
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
Token authentication required. Title field is required, body field is optional.
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
Integer should be the id of the target question. Body should be empty.
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

## Update Question's Favorited Field
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

## Update Question's Accepted Answer
Token authentication required. Authenticated user must match the author of the question. Set field value to the pk of the desired answer. To set no accepted answer, set value to `null`.
### Request
```json
PATCH /questions/9/
{
	"answered": 1
}
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
		},
		(...)
	],
	"created_at": "2021-12-15T00:10:31.523378Z",
	"favorited": [
		1,
		2
	],
	"answered": 1
}
```

## Upvote Question
Token authentication required. Field value should be an empty list (or array, for the Javascript-inclined).
### Request
```json
PATCH /questions/10/
{
	"upvotes": []
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
	"votes": 1,
	"upvotes": [
		3
	],
	"downvotes": [],
	"answers": [],
	"created_at": "2021-12-15T13:31:42.189621Z",
	"favorited": [
		3
	],
	"answered": null,
	"tags": []
}
```

## Downvote Question
Token authentication required. Field value should be an empty list (or array, for the Javascript-inclined).
### Request
```json
PATCH /questions/10/
{
	"downvotes": []
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
	"votes": -1,
	"upvotes": [],
	"downvotes": [
		2
	],
	"answers": [],
	"created_at": "2021-12-15T13:31:42.189621Z",
	"favorited": [
		3
	],
	"answered": null,
	"tags": []
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
Spaces in search term need to replaced by a +. Body should be empty.
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

## Add New Answer to Question
Token authentication required. Body field required.
### Request
```json
POST /questions/10/answers/
{
	"body": "I think you fold it hot dog style, not hamburger."
}
```
### Response
```json
201 Created
{
	"pk": 4,
	"body": "I think you fold it hot dog style, not hamburger.",
	"author": {
		"pk": 2,
		"username": "james"
	},
	"question": 10,
	"votes": 0,
	"upvotes": [],
	"downvotes": [],
	"created_at": "2021-12-21T14:07:41.639121Z",
	"favorited": []
}
```

## Edit Answer
Token authentication required, and must match the author of the answer. Body field required.
### Request
```json
PATCH /questions/10/answers/4/
{
	"body": "I think you fold it hamburger, not hot dog."
}
```
### Response
```json
{
	"pk": 4,
	"body": "I think you fold it hamburger, not hot dog.",
	"author": {
		"pk": 2,
		"username": "james"
	},
	"question": 10,
	"votes": 0,
	"upvotes": [],
	"downvotes": [],
	"created_at": "2021-12-21T14:07:41.639121Z",
	"favorited": []
}
```

## Delete Answer
Token authentication required, and must match the author of the answer. Body should be empty.
### Request
```json
DELETE /questions/10/answers/4/
```
### Response
```json
204 No Content
```

## Search Answers
Spaces in search term need to replaced by a +. Body should be empty.
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

## Update Answer's Favorited Field
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

## Upvote Answer
Token authentication required. Field value should be an empty list (or array, for the Javascript-inclined).
### Request
```json
PATCH /questions/9/answers/1/
{
	"upvotes": []
}
```
### Response
```json
200 OK
{
	"pk": 1,
	"body": "You should let it soak at least 30 minutes before you put it in the dishwasher.",
	"author": "james",
	"question": 9,
	"votes": 1,
	"upvotes": [
		1
	],
	"downvotes": [],
	"created_at": "2021-12-15T00:19:28.001432Z",
	"favorited": [
		1,
		2
	]
}
```

## Downvote Answer
Token authentication required. Field value should be an empty list (or array, for the Javascript-inclined).
### Request
```json
PATCH /questions/9/answers/1/
{
	"downvotes": []
}
```
### Response
```json
200 OK
{
	"pk": 1,
	"body": "You should let it soak at least 30 minutes before you put it in the dishwasher.",
	"author": "james",
	"question": 9,
	"votes": -1,
	"upvotes": [],
	"downvotes": [
		3
	],
	"created_at": "2021-12-15T00:19:28.001432Z",
	"favorited": [
		1,
		2
	]
}
```



## Tags
Token authentication required. 
### GET Request
```json
GET /tags/
{
  
}
```
### Response
```json
200 OK
[
  {
    "pk": 1,
    "name": "Baking",
    "slug": "baking"
  },
  {
    "pk": 2,
    "name": "Butchery",
    "slug": "butchery"
  },
  {
    "pk": 3,
    "name": "Seafood",
    "slug": "seafood"
  },
  {
    "pk": 4,
    "name": "Smoking",
    "slug": "smoking"
  },
  {
    "pk": 5,
    "name": "Vegetables",
    "slug": "vegetables"
  }
]
```

### POST Request
```json
POST /tags/
{
  "name": "Fruit"
}
```
### Response
```json
201 Created
{
  "pk": 6,
  "name": "Fruit",
  "slug": "fruit"
}
```