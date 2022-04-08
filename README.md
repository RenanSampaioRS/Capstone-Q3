# API_RESTAURANT

## **EMPLOYEES**

### ![GET](./assets/img/GET.svg) GET_ALL_EMPLOYEES

```
/api/employees
```

#### Header

```
Bearer Token
```

#### Response

```json
[
  {
    "id": 1,
    "name": "Joseph Climber",
    "login": "joseph",
    "is_admin": false,
    "cpf": "047222222222"
  },
  {
    "id": 2,
    "name": "Irineu Rodrigues",
    "login": "irineu",
    "is_admin": true,
    "cpf": "047333333333"
  }
]
```

<br>
<br>

### ![GET](./assets/img/GET.svg) GET_EMPLOYEE

```
/api/employees/<employee_id: int>
```

#### Header

```
Bearer Token
```

#### Response

```json
{
  "id": 1,
  "name": "Joseph Climber",
  "login": "joseph",
  "is_admin": false,
  "cpf": "047222222222"
}
```

<br>
<br>

### ![POST](./assets/img/POST.svg) CREATE_EMPLOYEE

```
/api/employees
```

#### Header

```
Bearer Token
```

#### Body

```json
{
  "name": "Joseph Climber",
  "login": "joseph",
  "password": "123456",
  "is_admin": false,
  "cpf": "047222222222"
}
```

#### Response

```json
{
  "id": 1,
  "name": "Joseph Climber",
  "login": "joseph",
  "is_admin": false,
  "cpf": "047222222222"
}
```

<br>
<br>

### ![POST](./assets/img/POST.svg) LOGIN_EMPLOYEE

```
/api/employees/login
```

#### Header

```

```

#### Body

```json
{
  "login": "joseph",
  "password": "123456"
}
```

#### Response

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNjQ0MjgzMywianRpIjoiMTE5MGM5OGQtYTI1Mi00ZjdlLWE3ZWYtOWNkYjA0OTUzYjI3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MiwibmFtZSI6ImlsbGlhbiIsImxvZ2luIjoiaWxsaWFuIiwiY3BmIjoiMDAwMDAwMDAwMDAiLCJpc19hZG1pbiI6ZmFsc2V9LCJuYmYiOjE2MjY0NDI4MzMsImV4cCI6MTYyNjQ0NjQzM30.pp94uopkA-HjiwvLTQXbGPQv587yHljHpW-27MBkBAE"
}
```

<br>
<br>

### ![PATCH](./assets/img/PATCH.svg) UPDATE_EMPLOYEE

```
/api/employees/<employee_id: int>
```

#### Header

```
Bearer Token
```

#### Body

```json
{
  "name": "Joseph Rodrigues"
}
```

#### Response

```json
{
  "id": 1,
  "name": "Joseph Rodrigues",
  "login": "joseph",
  "is_admin": false,
  "cpf": "047222222222"
}
```

<br>
<br>

---

### ![DELETE](./assets/img/DELETE.svg) DELETE_EMPLOYEE

```
/api/employees/<employee_id: int>
```

#### Header

```
Bearer Token
```

#### Response

```json
""
```

<br>
<br>

---

## **USERS**

<br>

### ![GET](./assets/img/GET.svg) GET_ALL_USERS

```
/api/users
```

#### Header

```
Bearer Token
```

#### Response

```json
[
  {
    "id": 1,
    "name": "Joseph Climber",
    "cpf": "047222222222",
    "total_spent": 345.22
  },
  {
    "id": 2,
    "name": "Irineu Cleber",
    "cpf": "047333333333",
    "total_spent": 57.48
  }
]
```

<br>
<br>

### ![GET](./assets/img/GET.svg) GET_USER

```
/api/users/<user_id:int>
```

#### Header

```
Bearer Token
```

#### Response

```json
{
  "id": 1,
  "name": "Joseph Climber",
  "cpf": "047222222222",
  "total_spent": 345.22
}
```

<br>
<br>

### ![POST](./assets/img/POST.svg) CREATE_USER

```
/api/users
```

#### Header

```
Bearer Token
```

#### Body

```json
{
  "name": "Joseph Climber",
  "cpf": "047222222222"
}
```

#### Response

```json
{
  "id": 1,
  "name": "Joseph Climber",
  "cpf": "047222222222",
  "total_spent": 0
}
```

<br>
<br>

### ![GET](./assets/img/GET.svg) GET_USER BY QUERY PARAM

```
/api/users?cpf=<cpf: str>&name=<name: str>
```

#### Header

```
Bearer Token
```

#### Response

```json
{
  "id": 1,
  "name": "Joseph Climber",
  "cpf": "047222222222",
  "total_spent": 345.22
}
```

<br>
<br>

### ![PATCH](./assets/img/PATCH.svg) UPDATE_USER

```
/api/users/<user_id: int>
```

#### Header

```
Bearer Token
```

#### Body

```json
{
  "name": "Joseph Rodrigues",
  "total_spent": 522.35
}
```

#### Response

```json
{
  "id": 1,
  "name": "Joseph Rodrigues",
  "cpf": "047222222222",
  "total_spent": 522.35
}
```

<br>
<br>

---

## **TABLES**

<br>

### ![GET](./assets/img/GET.svg) GET_ALL_TABLES

```
/api/tables
```

#### Header

```
Bearer Token
```

#### Response

```json
[
  {
    "id": 1,
    "login": "table01",
    "number": 1,
    "seats": 6,
    "user": {
      "id": 1,
      "name": "Joseph Climber",
      "cpf": "047222222222",
      "total_spent": 522.35
    },
    "total": 127.48,
    "empty": false,
    "orders_list": "/api/orders/1"
  },
  {
    "id": 2,
    "number": 1,
    "seats": 6,
    "user": {},
    "total": 127.48,
    "empty": true,
    "orders_list": "/api/orders/2"
  }
]
```

<br>
<br>

### ![GET](./assets/img/GET.svg) GET_TABLE

```
/api/tables/table_id=<table_id: int>
```

#### Header

```
Bearer Token
```

#### Response

```json
{
  "id": 1,
  "login": "table01",
  "number": 1,
  "seats": 6,
  "user": {
    "id": 1,
    "name": "Joseph Climber",
    "cpf": "047222222222",
    "total_spent": 522.35
  },
  "total": 127.48,
  "empty": false,
  "orders_list": "/api/orders/1"
}
```

<br>
<br>

### ![GET](./assets/img/GET.svg) GET_TABLE BY QUERY PARAM

```
/api/tables?empty=<empty: bool>&number=<number: int>
```

#### Header

```
Bearer Token
```

#### Response

```json
{
  "id": 1,
  "login": "table01",
  "number": 1,
  "seats": 6,
  "user": {
    "id": 1,
    "name": "Joseph Climber",
    "cpf": "047222222222",
    "total_spent": 522.35
  },
  "total": 127.48,
  "empty": false,
  "orders_list": "/api/orders/1"
}
```

<br>
<br>

### ![POST](./assets/img/POST.svg) CREATE_TABLE

```
/api/tables
```

#### Header

```
Bearer Token
```

#### Body

```json
{
  "login": "table01",
  "password": "table01",
  "number": 1,
  "seats": 6
}
```

#### Response

```json
{
  "id": 1,
  "login": "table01",
  "number": 1,
  "seats": 6,
  "empty": true
}
```

<br>
<br>

### ![PATCH](./assets/img/PATCH.svg) UPDATE_TABLE

```
/api/tables/<table_id: int>
```

#### Header

```
Bearer Token
```

#### Body

```json
{
  "number": 2,
  "seats": 4
}
```

#### Response

```json
{
  "id": 1,
  "login": "table01",
  "number": 2,
  "seats": 4,
  "user": {
    "id": 1,
    "name": "Joseph Climber",
    "cpf": "047222222222",
    "total_spent": 522.35
  },
  "total": 127.48,
  "empty": false,
  "orders_list": "/api/orders/1"
}
```

<br>
<br>

### ![PATCH](./assets/img/PATCH.svg) PAY_BILL

```
/api/tables/paybill/<table_id: int>
```

#### Header

```
Bearer Token
```

#### Body

```json
empty
```

#### Response

```json
{
  "Total without discount": 140.0,
  "Total with discount": 112.0
}
```

<br>
<br>

### ![DELETE](./assets/img/DELETE.svg) DELETE_TABLE

```
/api/tables/<table_id: int>
```

#### Header

```
Bearer Token
```

#### Response

```js
"";
```

<br>
<br>

### ![POST](./assets/img/POST.svg) LOGIN_TABLE

```
/api/tables/login
```

#### Header

```

```

#### Body

```json
{
  "login": "Irineu",
  "password": "12345"
}
```

#### Response

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNjIxNDA3NSwianRpIjoiMWJjMDE5ZTktNzY2OS00MzJmLWJhMDctMzE0MjgxZTg0ODU5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MiwibmFtZSI6Ikx1Y2FzIEpvc2Vmb3ZpY3oiLCJsb2dpbiI6Imx1Y2FzIn0sIm5iZiI6MTYyNjIxNDA3NSwiZXhwIjoxNjI2MjE0OTc1fQ.Mj5yzf4ENLntgmnTs8Hvlvwqa_FI_T1fh_1uQiKy6fU"
}
```

<br>
<br>

---

## **ORDERS**

<br>

### ![GET](./assets/img/GET.svg) GET_ALL_ORDERS

```
/api/orders
```

#### Header

```
Bearer Token
```

#### Response

```json
[
    {
        "id": 1,
        "date": ,//decidir formato da data
        "table_number": 5,
        "cooking": false,
        "ready": false,
        "delivered": false,
        "paid": false,
        "products": [
                        {
                            "id": 1,
                            "name": "Risoto Carbonara",
                            "quantity": 2,
                            "price": 7.80
                        },
                        {
                            "id": 3,
                            "name": "Fettuccine com molho Marzano",
                            "quantity": 1,
                            "price": 15.00
                        }
                    ],
        "total_products": 30.60
    },
    {
        "id": 2,
        "date": ,//decidir formato da data
        "table_number": 3,
        "cooking": true,
        "ready": false,
        "delivered": false,
        "paid": false,
        "products": [
                        {
                            "id": 4,
                            "name": "Raviolli de Ricota",
                            "quantity": 1,
                            "price": 10.00
                        }
                    ],
        "total_products": 10.00
    }
]
```

<br>
<br>

### ![GET](./assets/img/GET.svg) GET_ORDER

```
/api/orders/<table_id: int>
```

#### Header

```
Bearer Token
```

#### Response

```json
[
    {
        "id": 1,
        "date": ,//decidir formato da data
        "table_number": 5,
        "cooking": false,
        "ready": false,
        "delivered": false,
        "products": [
                        {
                            "id": 1,
                            "name": "Risoto Carbonara",
                            "quantity": 2,
                            "price": 7.80
                        },
                        {
                            "id": 3,
                            "name": "Fettuccine com molho Marzano",
                            "quantity": 1,
                            "price": 15.00
                        }
                    ],
        "total_products": 30.60
    }
]
```

<br>
<br>

### ![GET](./assets/img/GET.svg) GET*ORDERS* BY QUERY PARAMS

```
/api/orders?table_id=<table_id: int>?&ready=<ready: bool>&paid=<paid: bool>
```

#### Header

```
Bearer Token
```

#### Response

```json
[
    {
        "id": 1,
        "date": ,//decidir formato da data
        "table_number": 5,
        "cooking": false,
        "ready": false,
        "delivered": false,
        "products": [
                        {
                            "id": 1,
                            "name": "Risoto Carbonara",
                            "quantity": 2,
                            "price": 7.80
                        },
                        {
                            "id": 3,
                            "name": "Fettuccine com molho Marzano",
                            "quantity": 1,
                            "price": 15.00
                        }
                    ],
        "total_products": 30.60
    }
]
```

<br>
<br>

### ![POST](./assets/img/POST.svg) CREATE_ORDER

```
/api/orders
```

#### Header

```
Bearer Token
```

#### Body

```json
{
  "date": "Timestamp -> Unix", //decidir formato da data
  "table_id": 5,
  "products": [1, 2, 3, 1]
}
```

#### Response

```json
{
    "id": 1,
    "date": ,//decidir formato da data
    "table_number": 5,
    "cooking": false,
    "ready": false,
    "delivered": false,
    "products": [
                    {
                        "id": 1,
                        "name": "Risoto Carbonara",
                        "quantity": 2,
                        "price": 7.80
                    },
                    {
                        "id": 3,
                        "name": "Fettuccine com molho Marzano",
                        "quantity": 1,
                        "price": 15.00
                    }
                ],
    "total_products": 30.60
}

```

<br>
<br>

### ![PATCH](./assets/img/PATCH.svg) UPDATE_ORDER

```
/api/orders/<order_id: int>
```

#### Header

```
Bearer Token
```

#### Body

```json
{
  "cooking": false,
  "ready": true,
  "delivered": false
}
```

#### Response

```json
[
    {
        "id": 1,
        "date": ,//decidir formato da data
        "table_number": 5,
        "cooking": false,
        "ready": true,
        "delivered": false,
        "products": [
                        {
                            "id": 1,
                            "name": "Risoto Carbonara",
                            "quantity": 2,
                            "price": 7.80
                        },
                        {
                            "id": 3,
                            "name": "Fettuccine com molho Marzano",
                            "quantity": 1,
                            "price": 15.00
                        }
                    ],
        "total_products": 30.60
    }
]
```

<br>
<br>

### ![DELETE](./assets/img/DELETE.svg) DELETE_ORDER

```
/api/orders/<order_id: int>
```

#### Header

```
Bearer Token
```

#### Response

```js
"";
```

<br>
<br>

---

## **PRODUCTS**

<br>

### ![GET](./assets/img/GET.svg) GET_ALL_PRODUCTS

```
/api/products
```

#### Header

```
Bearer Token
```

#### Response

```json
[
  {
    "id": 1,
    "name": "Risoto Carbonara",
    "section": "Pratos principais",
    "price": 7.8,
    "calories": 587.87
  },
  {
    "id": 3,
    "name": "Fettuccine com molho Marzano",
    "section": "Pratos principais",
    "price": 15.0,
    "calories": 635.22
  }
]
```

<br>
<br>

### ![GET](./assets/img/GET.svg) GET_PRODUCT

```
/api/products/<product_id: int>
```

#### Header

```
Bearer Token
```

#### Response

```json
{
  "id": 1,
  "name": "Risoto Carbonara",
  "section": "Pratos principais",
  "price": 7.8,
  "calories": 587.87
}
```

<br>
<br>

### ![GET](./assets/img/GET.svg) GET_PRODUCTS BY QUERY PARAM

```
/api/products?section=<section: bool>?veggie=<veggie: bool>
```

#### Header

```
Bearer Token
```

#### Response

```json
[
  {
    "id": 1,
    "name": "Risoto Carbonara",
    "section": "Pratos principais",
    "price": 7.8,
    "calories": 587.87
  },
  {
    "id": 3,
    "name": "Fettuccine com molho Marzano",
    "section": "Pratos principais",
    "price": 15.0,
    "calories": 635.22
  }
]
```

<br>
<br>

### ![POST](./assets/img/POST.svg) CREATE_PRODUCT

```
/api/products
```

#### Header

```
Bearer Token
```

#### Body

```json
{
  "name": "Risoto Carbonara",
  "price": 7.8,
  "calories": 587.87
}
```

#### Response

```json
{
  "id": 1,
  "name": "Risoto Carbonara",
  "section": "None",
  "price": 7.8,
  "calories": 587.87
}
```

<br>
<br>

### ![PATCH](./assets/img/PATCH.svg) UPDATE_PRODUCT

```
/api/products/<product_id: int>
```

#### Header

```
Bearer Token
```

#### Body

```json
{
  "price": 18.8
}
```

#### Response

```json
{
  "id": 1,
  "name": "Risoto Carbonara",
  "section": "None",
  "price": 18.8,
  "calories": 587.87
}
```

<br>
<br>

### ![DELETE](./assets/img/DELETE.svg) UPDATE_PRODUCT

```
/api/products/<product_id: int>
```

#### Header

```
Bearer Token
```

#### Response

```js
"";
```

<br>
<br>
