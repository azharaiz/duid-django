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

# Transaction API Documentation
## Get all auth user's transaction
#### URL : `/api/transaction/`

#### Method : `GET`

#### Query parameter : 
```json
?account_id=uuid
?category_id=uuid
```

#### Response :
```json
{
    "transaction_list": [
        {
            "transaction_id": "31bb657b-b777-40d8-bb03-2e9fe71c4a54",
            "user": "cc1eacfd-a6f4-4587-8ab0-b5349337dc92",
            "dompet": "7f9f3b50-b707-4c5e-99bf-289adb748470",
            "category": "dac6c3f9-99d5-4a6b-b82a-b18df76e5a48",
            "amount": 100.0,
            "created_at": "2020-12-16T08:50:19.919065Z",
            "updated_at": "2020-12-16T08:50:19.919091Z"
        },
        {
            "transaction_id": "7b79ad02-2fd1-4628-9031-94d670a841b5",
            "user": "cc1eacfd-a6f4-4587-8ab0-b5349337dc92",
            "dompet": "7f9f3b50-b707-4c5e-99bf-289adb748470",
            "category": "dac6c3f9-99d5-4a6b-b82a-b18df76e5a48",
            "amount": 1003333.0,
            "created_at": "2020-12-16T08:50:45.578977Z",
            "updated_at": "2020-12-16T08:50:45.578999Z"
        }
    ]
}
```

## Create one auth user's transaction
#### URL : `/api/transaction/`

#### Method : `POST`

#### Data :

```json
{
    "user": uuid,
    "dompet": uuid,
    "category": uuid,
    "amount": float,
    "created_at": date,
    "updated_at": date
}
```

#### Response :

```json
{
    "message": "success add transaction"
}
```

## Delete one auth user's transaction
#### URL : `/api/transaction/<TransactionUUID>/`

#### Method : `DELETE`

#### Response :

```json
{
    "message": "success delete transaction"
}
```

## Update one auth user's transaction
#### URL : `/api/transaction/<TransactionUUID>/`

#### Method : `PUT`

#### Data :

```json
{
    "user": uuid,
    "dompet": uuid,
    "category": uuid,
    "amount": float,
    "created_at": date,
    "updated_at": date
}
```

#### Response :

```json
{
    "message": "success update category"
}
```