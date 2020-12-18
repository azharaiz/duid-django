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

# Target API Documentation

#### Header for all request: 

```json
{"Authorization" : BearerToken}
```

## Get all target
#### URL : `/api/target/`

#### Method : `GET`

#### Response :
```json
{
    "count": 10,
    "next": null,
    "previous": null,
    "results": [
        {
            "target_id": "d97b3622-8f1f-4ea8-9b1e-b82e79dbd31e",
            "user": "f90b4e9c-bf8d-4f5d-a467-4ea62d658069",
            "due_date": "2012-04-21",
            "target_title": "asaad",
            "target_amount": 200
        },
        {
            "target_id": "86c4a646-22cf-4f5f-bca4-ae57cb0d18e5",
            "user": "f90b4e9c-bf8d-4f5d-a467-4ea62d658069",
            "due_date": "2012-04-21",
            "target_title": "asaad",
            "target_amount": 200
        },
        {
            "target_id": "ae2326e5-b82b-4fa3-ae74-658b99fdbd93",
            "user": "f90b4e9c-bf8d-4f5d-a467-4ea62d658069",
            "due_date": "2025-04-21",
            "target_title": "asaad",
            "target_amount": 200
        },
        {
            "target_id": "efb3c2cf-eabb-4572-881c-bed619a3b337",
            "user": "f90b4e9c-bf8d-4f5d-a467-4ea62d658069",
            "due_date": "2025-04-21",
            "target_title": "asaad",
            "target_amount": 200
        },
        {
            "target_id": "eb3a02f1-4af9-4ce8-bb30-48b989ba70bf",
            "user": "f90b4e9c-bf8d-4f5d-a467-4ea62d658069",
            "due_date": "2025-04-21",
            "target_title": "asaad",
            "target_amount": 200
        },
        {
            "target_id": "bcb7f0bb-dfc7-4cc7-a603-62a889f98c64",
            "user": "f90b4e9c-bf8d-4f5d-a467-4ea62d658069",
            "due_date": "2025-04-21",
            "target_title": "asaad",
            "target_amount": 200
        },
        {
            "target_id": "2ea7d5cc-a04f-49f1-b06b-9d10308b4126",
            "user": "f90b4e9c-bf8d-4f5d-a467-4ea62d658069",
            "due_date": "2025-04-21",
            "target_title": "asaad",
            "target_amount": 200
        },
        {
            "target_id": "6d256195-5903-4a97-b297-4bbf15080bda",
            "user": "f90b4e9c-bf8d-4f5d-a467-4ea62d658069",
            "due_date": "2025-04-21",
            "target_title": "asaad",
            "target_amount": 200
        },
        {
            "target_id": "4af83e8b-392b-4866-8c59-4bb4022389a6",
            "user": "f90b4e9c-bf8d-4f5d-a467-4ea62d658069",
            "due_date": "2005-04-21",
            "target_title": "asaad",
            "target_amount": 200
        },
        {
            "target_id": "30e5f51e-794b-45bc-9b46-d2e2d8365b80",
            "user": "f90b4e9c-bf8d-4f5d-a467-4ea62d658069",
            "due_date": "2005-04-21",
            "target_title": "asaad",
            "target_amount": 200
        }
    ]
}
```

## Get one target
#### URL : `/api/target/<targetUUID>/`

#### Method : `GET`

#### Response :
```json
{
    "target_id": "d97b3622-8f1f-4ea8-9b1e-b82e79dbd31e",
    "user": "f90b4e9c-bf8d-4f5d-a467-4ea62d658069",
    "due_date": "2012-04-21",
    "target_title": "asaad",
    "target_amount": 200
}
```

## Create one target
#### URL : `/api/target/`

#### Method : `POST`

#### Data :

```json
{
    "target_title":"asaad",
    "target_amount":200,
    "due_date":"2025-04-21",
    "user":"f90b4e9c-bf8d-4f5d-a467-4ea62d658069"
}


```

#### Response :

```json
{
    "target_id": "24df44f2-69d9-4b77-941f-f3f352720f50",
    "user": "f90b4e9c-bf8d-4f5d-a467-4ea62d658069",
    "due_date": "2025-04-21",
    "target_title": "asaad",
    "target_amount": 200
}
```

## Delete one target
#### URL : `/api/target/<targetUUID>`

#### Method : `DELETE`

#### Response :

```json
No response
```

## Update one target
#### URL : `/api/target/<targetUUID>`

#### Method : `PUT`

#### Data :

```json
{
    "target_title":"BERUBAH",
    "target_amount":300,
    "due_date":"2025-04-22",
    "user":"f90b4e9c-bf8d-4f5d-a467-4ea62d658069"
}
```

#### Response :

```json
{
    "target_id": "f8516f61-7d2b-4058-8c45-ead82cb1ed81",
    "user": "f90b4e9c-bf8d-4f5d-a467-4ea62d658069",
    "due_date": "2025-04-22",
    "target_title": "BERUBAH",
    "target_amount": 300
}
```
