gatekeeper
==========

Gatekeeper is a service that lets you temporarily mark an environment as locked for deployment.

![Gatekeeper](http://f.cl.ly/items/1d432U1P130t1v0d1h2d/Gate%2520keeper.jpeg)

Usage
-----

### List all environment locks

```
GET /locks/
```

#### Response
Status **200 OK**

```
{
  "locks": [
    {
      "environment": "acct-dev", 
      "owner": "mwarkentin", 
      "message": "Testing CDN", 
      "since": "2012-09-03 16:10:29.165004"
    }, 
    {
      "environment": "acct-stage", 
      "owner": "dlanger", 
      "message": "Testing weekly email fix branch", 
      "since": "2012-09-03 15:53:46.717481"
    }, 
    {
      "environment": "acct-prod", 
      "owner": "dlanger", 
      "message": "Testing weekly email fix branch", 
      "since": "2012-09-03 15:52:52.008120"
    }
  ]
}
```

### Get the status of a single environment lock
```
GET /locks/:environment/
```

#### Response
Status **200 OK**

```
{
  "environment": "acct-stage", 
  "owner": "dlanger", 
  "message": "Testing weekly email fix branch", 
  "since": "2012-09-03 15:53:46.717481"
}
```

#### No such environment response
Status **404 Not Found**

### Lock an environment
```
POST /locks/:environment/
```

#### Parameters
**user**  
*Required* **string** - User who locked the environment.

**message**  
*Optional* **string** - Description of why the environment has been locked.

```
{
  "user": "mwarkentin",
  "message": "Testing CDN"
}
```

#### Successful response
Status **200 OK**

```
{
  'environment': 'acct-dev', 
  'owner': 'mwarkentin', 
  'message': 'Testing CDN', 
  'since': '2012-09-03 16:10:29.165004'
}
```

#### Already locked response
Status **409 Conflict**


### Unlock an environment
```
DELETE /locks/:environment/
```

#### Successful response
Status **200 OK**

#### Already unlocked response
Status **404 Not Found**
