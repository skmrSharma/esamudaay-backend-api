# eSamudaay - Backend take home assignment
## Build an application server with a single API.

## Contents:
1. [Description](#description)

2. [Example Input](#example-input)

3. [Installation](#installation)
4. [To run the code](#run-the-code)
5. [Technical Details](#technical-details)

## Description
This API will take as input items ordered, delivery distance, and offer applied. The response is the total order value.

All input and output currency values are in paisa (1 paisa = 0.01 INR).

Delivery distance should be an integer in meters.

Offer applied can be of two types: FLAT and DELIVERY.

If FLAT, the offer_price is deducted normally. If DELIVERY, it means no delivery fee will be charged.

The delivery fee is applied according to below cost slab:
```
0 to 10km: 50 INR
10 to 30km: 100 INR 
30 to 100km: 500 INR
100 to 500km: 2000 INR
```

## Example Input
An example input is:
```JSON
{
    "order_items": [
        {
            "name": "bread",
            "quantity": 2,
            "price": 2200
        },
        {
            "name": "butter",
            "quantity": 1,
            "price": 5900
        }
    ],
    "distance": 1200,
    "offer": {
        "offer_type": "FLAT",
        "offer_val": 1000
    }
}
```

The API output for above input is:
`{"order_total":14300}`

The `offer` parameter is optional. The other two are required and cannot be empty.

## Installation
To run the code you need the following:
```
python3
flask-restful
```

To install dependencies (make sure you have python and pip installed):
```
pip install Flask
pip install flask-restful
```

## Run the code
Finally, to run the code, download and extract the source code or clone this project if you have `git` installed.

```
git clone https://github.com/skmrSharma/esamudaay-backend-api/
python app.py
```

This will start the development server and you can test the values using Postman, or using curl.

## Technical Details
This API was built using Flask and Flask-RESTful. 

Flask is a lightweight web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs.

Since this is a very simple API that makes just one POST request I decided to use the RESTful extension for Flask, making the job easy and also making the code much readable.

