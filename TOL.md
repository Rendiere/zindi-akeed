# Thinking Out Loud

_A place to jot down things as they pop into your brain. Try to be clear so that it's not a struggle to figure out later what you meant._


## Ruix

...

## Devin

...

## Renier



* We will have to use the orders data to build up the frequency matrix [location, vendor] - basically, in location X, vendor Y was ordered from Z many times.
* We don't know much about the customers in test data, except some meta data for some and the locations they were.
* So, location is the main feature I think.
* Predictions could thus be made on a location basis and we can do some post-processing on predictions based on what we know about the customer from meta data.

For example:
  1. we construct N clusters / hex grid from user locations
  2. for each cluster, use order history of all orders within that geo region to build vendor popularity table
  3. thus, you have N x 100 location based vendor popularity
  4. if we don't know anything more about a customer, we simply attribute the vendor popularity rank for that location
  5. if we have more info, we can use that to model predictions 


* Predictions need to be probability of ordering from that vendor. Need to find a way to convert from ranked vendors based on popularity to probability of ordering.
