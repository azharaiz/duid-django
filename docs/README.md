# Authentication API Documentation

## Get Token
#### URL : `/api/auth/token`

#### Method : `POST`

#### Body :
```json
{
    "email": "email@mail.com",
    "password": "password"
}
```

#### Response :
##### 200
```json
{
    "access": "ACCESS_TOKEN",
    "refresh": "REFRESH_TOKEN"
}
```

##### 404
```json
{
    "detail": "No active account found with the given credentials"
}
```

## Update Access Token
#### URL : `/api/auth/token/refresh`

#### Method : `POST`

#### Body :
```json
{
    "refresh": "REFRESH_TOKEN"
}
```

#### Response :
##### 200
```json
{
    "access": "ACCESS_TOKEN"
}
```

## Get User Profile
#### URL : `/api/auth/profile`

#### Method : `GET`

#### Header:
```json
{
    "Authorization" : "BEARER_TOKEN"
}
```

#### Response :
##### 200
```json
{
    "id": "USER_ID",
    "email": "USER_EMAIL",
    "created_at": "DATE_CREATED",
    "updated_at": "DATE_UPDATED"
}
```

## Update User Profile
#### URL : `/api/auth/profile`

#### Method : `PUT`

#### Header:
```json
{
    "Authorization" : "BEARER_TOKEN"
}
```

#### Body :
```json
{
    "email?": "USER_EMAIL",
    "password?": "USER_PASSWORD"
}
```

#### Response :
##### 200
```json
{
    "id": "USER_ID",
    "email": "USER_EMAIL",
    "created_at": "DATE_CREATED",
    "updated_at": "DATE_UPDATED"
}
```

##### 400
```json
{
    "message": "Invalid data"
}
```