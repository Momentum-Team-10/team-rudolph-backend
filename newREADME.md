# Questions API Documentation

The base url for all the extensions below is: `https://questions-t10.herokuapp.com/`


## CRUD vs. HTTP Reference
|**CRUD**|**HTTP**|
|:------:|:------:|
|Create|POST|
|Read|GET|
|Update|PUT/PATCH|
|Delete|DELETE|


## Token Authentication

|**URL** |**Description**         |**Method**|**Request**   |**Response**     |
|:------:|------------------------|----------|--------------|-----------------|
|`/token/login/`|Token authenticated login|`POST`|`username`<br>`password`|`HTTP_200_OK`<br>`auth_token`|
|`/token/logout/`|Token authenticated logout|`POST`|-|`HTTP_204_NO_CONTENT`|


## User endpoints
|**URL** |**Description**         |**Method**|**Request**   |**Response**     |
|:------:|------------------------|----------|--------------|-----------------|
|`/users/`|register a new user|`POST`|`username`<br>`password`<br>`re_password`|`HTTP_201_CREATED`<br>JSON of created User object|
|`/users/me/`|retrieve authenticated user data|`GET`|-|`HTTP_200_OK`<br>JSON of authenticated User object|
|`/users/me/`|update authenticated user data|`PATCH`|`{{ User.FIELDS_TO_UPDATE }}`|`HTTP_200_OK`<br>JSON of updated authenticated User object|


## Database endpoints

|**URL** |**Description**         |**Method**|**Request**   |**Response**     |
|:------:|------------------------|:--------:|:------------:|:---------------:|
|`/questions/`|Getting a list of all questions|`GET`|-|`HTTP_200_OK`<br>JSON list of Question objects with answers nested inside|
|`/questions/`|Adding new question|`POST`|`title`<br>`body`|`HTTP_201_Created`<br>JSON of created question object|
|`/questions/<int:pk>/`|Details of a single Question|`GET`|`HTTP_200_OK`<br>JSON of Question object with specified pk|
|`/questions/<int:pk>/answers/`|List of a question's answers|`GET`|`HTTP_200_OK`<br>JSON list of Answer objects|
|`/questions/<int:pk>/answers/<int:ans>/`|Update a question's Answer object. `pk` is the Question's pk and `ans` is the Answer's pk|`PATCH`|`HTTP_200_OK`<br>JSON of updated Answer object|
|`/user/<int:pk>/answers/`|List of user's answers|`GET`|`HTTP_200_OK`<br>JSON list of Answer objects|