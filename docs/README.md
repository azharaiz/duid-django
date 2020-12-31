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
