# Duid API Documentation

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

# User API Documentation

## Create User
#### URL : `/api/user/`

#### Method : `POST`

#### Data :

```json
{
    "email": String,
    "password": String
}
```

#### Response :

```json
{
    "id": "00eec4dc-45d9-43ab-bee7-5f69dd1aba8b",
    "email": "email@mail.com",
    "created_at": "2020-12-04T07:29:39.255688Z",
    "updated_at": "2020-12-04T08:36:16.047932Z"
}
```

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
    "category_type": String ('INCOME' or 'EXPENSE')
}
```

#### Response :

```json
{
    "message": "success add category"
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
    "message": "success update transaction"
}
```

# Target API Documentation

#### Header for all request: 

```json
{"Authorization" : <BearerToken>}
```

annual_invest_rate is the rate that the money will grow in one year

annual_invest_rate of 0.06 means the money will increase 6% in one year

monthly_deposit_amount is calculated by system

for now, this app can only calculate target more than one year

this app will give monthly_deposit_amount of 0 if annual_invest_rate is 0

## Get all target
#### URL : `/api/target/`

#### Method : `GET`

#### Response :
```json
{
    "count": 19,
    "next": null,
    "previous": "http://localhost:8000/api/target/",
    "results": [
        {
            "target_id": "4f9a119d-62c6-4073-991e-11ae005ffe65",
            "user": "b925e7b0-ba47-4fb2-b15b-b1a147a97a4d",
            "due_date": "2025-04-21",
            "target_title": "asaada",
            "target_amount": 200,
            "annual_invest_rate": 0.0,
            "monthly_deposit_amount": 0
        },
        {
            "target_id": "92caf1ef-77ca-447c-9362-567148fb9926",
            "user": "b925e7b0-ba47-4fb2-b15b-b1a147a97a4d",
            "due_date": "2025-04-21",
            "target_title": "asaada",
            "target_amount": 200,
            "annual_invest_rate": 0.0,
            "monthly_deposit_amount": 0
        },
        {
            "target_id": "2288a6a6-0459-4eb1-93b3-7a140886bb44",
            "user": "b925e7b0-ba47-4fb2-b15b-b1a147a97a4d",
            "due_date": "2025-04-21",
            "target_title": "asaada",
            "target_amount": 200,
            "annual_invest_rate": 0.0,
            "monthly_deposit_amount": 0
        },
        {
            "target_id": "d32d4e26-4523-46e3-b96f-48e15a62f3a6",
            "user": "b925e7b0-ba47-4fb2-b15b-b1a147a97a4d",
            "due_date": "2027-04-21",
            "target_title": "asaada",
            "target_amount": 200000,
            "annual_invest_rate": 0.0,
            "monthly_deposit_amount": 0
        },
        {
            "target_id": "7866c0ea-dacd-4a4f-a81b-edc4d221dc39",
            "user": "b925e7b0-ba47-4fb2-b15b-b1a147a97a4d",
            "due_date": "2027-04-21",
            "target_title": "asaada",
            "target_amount": 200000,
            "annual_invest_rate": 0.6,
            "monthly_deposit_amount": 168
        },
        {
            "target_id": "40076bb5-84dc-4fd7-88fc-3cf7c1e6fd27",
            "user": "b925e7b0-ba47-4fb2-b15b-b1a147a97a4d",
            "due_date": "2027-04-21",
            "target_title": "asaada",
            "target_amount": 200000,
            "annual_invest_rate": 0.0,
            "monthly_deposit_amount": 0
        },
        {
            "target_id": "db5e6ab6-d771-42ef-8664-ad0b962d3e32",
            "user": "b925e7b0-ba47-4fb2-b15b-b1a147a97a4d",
            "due_date": "2027-04-21",
            "target_title": "asaada",
            "target_amount": 200000,
            "annual_invest_rate": 0.6,
            "monthly_deposit_amount": 168
        },
        {
            "target_id": "37d4dd66-345d-4198-a868-fbaf2e71bbc2",
            "user": "b925e7b0-ba47-4fb2-b15b-b1a147a97a4d",
            "due_date": "2027-04-21",
            "target_title": "asaada",
            "target_amount": 200000,
            "annual_invest_rate": 0.0,
            "monthly_deposit_amount": 0
        },
        {
            "target_id": "01d7544a-5497-4777-b993-05892ab4e289",
            "user": "b925e7b0-ba47-4fb2-b15b-b1a147a97a4d",
            "due_date": "2027-04-21",
            "target_title": "asaada",
            "target_amount": 200000,
            "annual_invest_rate": 0.0,
            "monthly_deposit_amount": 0
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
    "target_id": "db5e6ab6-d771-42ef-8664-ad0b962d3e32",
    "user": "b925e7b0-ba47-4fb2-b15b-b1a147a97a4d",
    "due_date": "2027-04-21",
    "target_title": "asaada",
    "target_amount": 200000,
    "annual_invest_rate": 0.6,
    "monthly_deposit_amount": 168
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
    "target_id": "93025e57-fcb0-4afe-b2a1-bc45172427bb",
    "user": "b925e7b0-ba47-4fb2-b15b-b1a147a97a4d",
    "due_date": "2027-04-21",
    "target_title": "asaada",
    "target_amount": 200000,
    "annual_invest_rate": 0.6,
    "monthly_deposit_amount": 168
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
    "target_amount": 300,
    "annual_invest_rate": 0.0,
    "monthly_deposit_amount": 0,
}
```