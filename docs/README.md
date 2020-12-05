# Category API Documentation

#### Header for all request: 

```json
{"Authorization" : BearerToken}
```

## Get all auth user's category
#### URL : `/api/category/`

#### Method : `GET`

#### Response :
```json
{
    "category_list": [
        {
            "category_id": "b509c818-575f-46ad-a07c-524850c3674d",
            "user": "2cbd2c4a-7601-4959-a249-a0d1ba87f448",
            "category_title": "tester1111",
            "category_type": "INCOME",
            "created_at": "2020-12-04T04:42:43.237667Z",
            "updated_at": "2020-12-04T04:42:43.237731Z"
        },
        {
            "category_id": "696b666b-cb12-4bb6-81c7-87710cba2a6c",
            "user": "2cbd2c4a-7601-4959-a249-a0d1ba87f448",
            "category_title": "tester343",
            "category_type": "INCOME",
            "created_at": "2020-12-04T06:39:29.363162Z",
            "updated_at": "2020-12-04T06:40:05.043961Z"
        },
        {
            "category_id": "b61c07cc-e70c-4958-bfb0-1490ccdb95ec",
            "user": "2cbd2c4a-7601-4959-a249-a0d1ba87f448",
            "category_title": "tester343w",
            "category_type": "INCOME",
            "created_at": "2020-12-04T07:29:13.324519Z",
            "updated_at": "2020-12-04T07:29:13.324546Z"
        }
    ]
}
```

## Get one auth user's category
#### URL : `/api/category/<CategoryUUID>/`

#### Method : `GET`

#### Response :
```json
{
    "category_id": "b509c818-575f-46ad-a07c-524850c3674d",
    "user": "2cbd2c4a-7601-4959-a249-a0d1ba87f448",
    "category_title": "tester1111",
    "category_type": "INCOME",
    "created_at": "2020-12-04T04:42:43.237667Z",
    "updated_at": "2020-12-04T04:42:43.237731Z"
}
```

## Create one auth user's category
#### URL : `/api/dompet/`

#### Method : `POST`

#### Data :

```json
{
    "category_title": String,
    "category_type": String ("INCOME" or "EXPENSE")
}


```

#### Response :

```json
{
    "message": "success add category"
}
```

## Delete one auth user's category
#### URL : `/api/category/<CategoryUUID>/`

#### Method : `DELETE`

#### Response :

```json
{
    "message": "success delete category"
}
```

## Update one auth user's category
#### URL : `/api/category/<CategoryUUID>/`

#### Method : `PUT`

#### Data :

```json
{
    "category_title": String,
    "category_type": String ("INCOME" or "EXPENSE")
}
```

#### Response :

```json
{
    "message": "success add category"
}
```
