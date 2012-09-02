gatekeeper
==========

Gatekeeper is a service that lets you temporarily mark an environment as locked for deployment.

![Gatekeeper](http://f.cl.ly/items/1d432U1P130t1v0d1h2d/Gate%2520keeper.jpeg)

Usage
-----

### List all environments and their lock status

```
GET /
```

#### Parameters
**type**  
`all`, `locked`, `unlocked`. Default `all`.

#### Response
Status **200 OK**

```
{
  "environments": [
    {
      "theglitch": {
        "locked": false 
      }
    },
    {
      "staging": {
        "locked": false 
      }
    },
    {
      "production": {
      	"locked": true,
      	"locked_by": "mwarkentin",
      	"time": <datetime>,
  		"message": "Testing branch email-weekly-fix"
      }
    }
  ]
}
```

### Get the status of a single environment
```
GET /:environment/
```

#### Response
Status **200 OK**

```
{
  "environment": "production",
  "locked": true,
  "locked_by": "dlanger",
  "time": <datetime>,
  "message": "Locked to test branch email-weekly-fix"
}
```

```
{
  "environment": "theglitch",
  "locked": false
}
```

### Lock an environment
```
POST /:environment/lock/
```

#### Parameters
**user**  
*Required* **string** - User who locked the environment.

**message**  
*Optional* **string** - Description of why the environment has been locked.

**force**  
*Optional* **boolean** - If true, lock an environment even if someone else has already locked it.

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
  "environment": "staging",
  "locked": true,
  "locked_by": "mwarkentin",
  "time", <datetime>,
  "message": "Testing CDN"
}
```

#### Already locked response
Status **409 Conflict**

```
{
  "environment": "staging",
  "locked": true,
  "locked_by": "dlanger",
  "time", <datetime>,
  "message": "Testing branch email-weekly-fix"
}
```

### Unlock an environment
```
DEL /:environment/lock/
```

#### Parameters
**user**  
*Required* **string** - User who unlocked the environment.

**force**  
*Optional* **boolean** - If true, unlock an environment even if you don't own the lock.

#### Successful response
Status **200 OK**

```
{
  "environment": "staging",
  "locked": false
}
```

#### Already unlocked response
Status **404 Not Found**
