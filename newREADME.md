# Questions API Documentation

The base url for all the extensions below is: https://questions-t10.herokuapp.com/

## Authentication

|**URL** |**Description**         |**Method**|**Request**   |**Response**     |
|:------:|------------------------|----------|--------------|-----------------|
|/token/login/|Token authenticated login|`POST`|`username`<br>`password`|`HTTP_200_OK`<br>`auth_token`|
|/token/logout/|Token authenticated logout|`POST`|-|`HTTP_204_NO_CONTENT`|
