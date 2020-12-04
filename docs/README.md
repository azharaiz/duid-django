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
