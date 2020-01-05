# JSON Basics

## Definition of JSON
Javascript Object Notation
--> is usually a **dictionary** 
However, confusingly an object in javascript is the data type for 
both lists (Arrays) and Dictionaries(Hashes) 

## Create a JSON file

### json.dumps(obj) ---> string json

### json.dump(obj, file) ---> writes json in file

## Make post requests with JSON
you need:
- path
- json
- headers

## Task 
Make a small program that requests 3 postcodes using POST and
returns something like:
```
    > 1 - postcode: xyzpto with nhs location at: xyz
    > 2 - Postcode: xyzpyo2 with nhs location at: xyz
    > 3 - (...) 
```