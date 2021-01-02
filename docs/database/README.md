# Database Documentation

## User:
* user_id : UUID
* username : String
* email : String (E-mail)
* password : String (hashed)
* created_at : Date
* updated_at : Date

Primary key : user_id

## Account (Dompet) :
* account_id : UUID
* user_id : UUID
* account_title : String
* created_at : Date
* updated_at : Date

Primary key : account_id </br>
Foreign key : user_id </br>
Unique key : (user_id, account_title)

## Category :
* category_id : UUID
* user_id : UUID
* category_title : String
* type : String [expense (-), income (+)]
* created_at : Date
* updated_at : Date

Primary key : category_id </br>
Foreign key : user_id </br>
Unique key : (user_id, category_title)

## Transaction :
* transaction_id (primary key) : UUID
* user_id (foreign key) : UUID
* category_id (foreign key) : UUID
* account_id (foreign key) : UUID
* amount : Float
* created_at : Date
* updated_at : Date

Primary key : transaction_id </br>
Foreign key : category_id, user_id, account_id

## Target :
* target_id (primary key) : UUID
* user_id (foreign key) : UUID
* due_date : Date
* target_title : String
* target_amount : Integer

Primary key : target_id </br>
Foreign key : user_id 
