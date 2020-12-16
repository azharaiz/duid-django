# Account(Dompet) API Documentation

#### Header for all request: 

```json
{"Authorization" : BearerToken}
```

## Get all dompet
#### URL : `/api/dompet/`

#### Method : `GET`

#### Response :
```json
{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "account_id": "00eec4dc-45d9-43ab-bee7-5f69dd1aba8b",
            "account_title": "new",
            "created_at": "2020-12-04T07:29:39.255688Z",
            "updated_at": "2020-12-04T08:36:16.047932Z",
            "user": "ae1a0426-17bb-4578-b34e-523695139654"
        },
        {
            "account_id": "9ecd1f36-20dd-4076-b6f0-82e87e931133",
            "account_title": "duaaa",
            "created_at": "2020-12-04T07:29:41.691663Z",
            "updated_at": "2020-12-04T07:29:41.691708Z",
            "user": "ae1a0426-17bb-4578-b34e-523695139654"
        },
        {
            "account_id": "581d5993-f67d-413b-b734-b066c2a4b283",
            "account_title": "aaaaa",
            "created_at": "2020-12-04T08:25:23.764912Z",
            "updated_at": "2020-12-04T08:25:23.764979Z",
            "user": "ae1a0426-17bb-4578-b34e-523695139654"
        },
        {
            "account_id": "0162242c-5163-41f6-b686-77e140e32284",
            "account_title": "aaaaa",
            "created_at": "2020-12-04T08:25:50.698512Z",
            "updated_at": "2020-12-04T08:25:50.698564Z",
            "user": "ae1a0426-17bb-4578-b34e-523695139654"
        },
        {
            "account_id": "6cc15489-41ae-4a0f-b3cd-bc26753750ee",
            "account_title": "BERUBAH",
            "created_at": "2020-12-04T10:26:35.326316Z",
            "updated_at": "2020-12-04T10:27:02.982422Z",
            "user": "ae1a0426-17bb-4578-b34e-523695139654"
        }
    ]
}
```

## Get one dompet
#### URL : `/api/dompet/<DompetUUID>/`

#### Method : `GET`

#### Response :
```json
{
    "account_id": "00eec4dc-45d9-43ab-bee7-5f69dd1aba8b",
    "account_title": "new",
    "created_at": "2020-12-04T07:29:39.255688Z",
    "updated_at": "2020-12-04T08:36:16.047932Z",
    "user": "ae1a0426-17bb-4578-b34e-523695139654"
}
```

## Create one dompet
#### URL : `/api/dompet/`

#### Method : `POST`

#### Data :

```json
{
    "account_title": String,
    "user": String(UserUUID)
}


```

#### Response :

```json
{
    "account_id": "00eec4dc-45d9-43ab-bee7-5f69dd1aba8b",
    "account_title": "JUST MADE",
    "created_at": "2020-12-04T07:29:39.255688Z",
    "updated_at": "2020-12-04T08:36:16.047932Z",
    "user": "ae1a0426-17bb-4578-b34e-523695139654"
}
```

## Delete one dompet
#### URL : `/api/dompet/<DompetUUID>`

#### Method : `DELETE`

#### Response :

```json
No response
```

## Update one dompet
#### URL : `/api/dompet/<DompetUUID>`

#### Method : `PUT`

#### Data :

```json
{
    "account_id": "00eec4dc-45d9-43ab-bee7-5f69dd1aba8b",
    "account_title": "BERUBAH",
    "created_at": "2020-12-04T07:29:39.255688Z",
    "updated_at": "2020-12-04T15:15:16.579703Z",
    "user": "ae1a0426-17bb-4578-b34e-523695139654"
}
```

#### Response :

```json
{
    "account_id": "00eec4dc-45d9-43ab-bee7-5f69dd1aba8b",
    "account_title": "BERUBAH",
    "created_at": "2020-12-04T07:29:39.255688Z",
    "updated_at": "2020-12-04T15:15:16.579703Z",
    "user": "ae1a0426-17bb-4578-b34e-523695139654"
}
```

