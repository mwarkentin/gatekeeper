# Usage examples

## Create `aqua` lock

### httpie

```
$ echo '{
  "user": "mwarkentin",
  "message": "Testing CDN"
}' | http POST http://localhost/locks/aqua/   cache-control:no-cache

HTTP/1.1 200 OK
Content-Length: 125
Content-Type: application/json

{
    "environment": "aqua",
    "message": "Testing CDN",
    "owner": "mwarkentin",
    "since": "2016-07-05 20:36:14.012595"
}
```

### curl

```
$ curl -X POST -H "Content-Type: application/json" -H "Cache-Control: no-cache" -d '{
  "user": "mwarkentin",
  "message": "Testing CDN"
}' "http://localhost/locks/aqua/"
```

## List locks

### httpie

```
$ http http://localhost/locks/
HTTP/1.1 200 OK
Content-Length: 170
Content-Type: application/json

{
    "locks": [
        {
            "environment": "aqua",
            "message": "Testing CDN",
            "owner": "mwarkentin",
            "since": "2016-07-05 20:36:14.012595"
        }
    ]
}
```

### curl

```
$ curl http://localhost/locks/
{
  "locks": [
    {
      "environment": "aqua",
      "message": "Testing CDN",
      "owner": "mwarkentin",
      "since": "2016-07-05 20:36:14.012595"
    }
  ]
}
```

## Get `aqua` lock

### httpie

```
$ http http://localhost/locks/aqua/
HTTP/1.1 200 OK
Content-Length: 125
Content-Type: application/json

{
    "environment": "aqua",
    "message": "Testing CDN",
    "owner": "mwarkentin",
    "since": "2016-07-05 20:36:14.012595"
}
```

### curl

```
$ curl http://localhost/locks/aqua/
{
  "environment": "aqua",
  "message": "Testing CDN",
  "owner": "mwarkentin",
  "since": "2016-07-05 20:36:14.012595"
}
```

## Delete `aqua` lock

### httpie

```
$ http DELETE http://localhost/locks/aqua/
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: text/html; charset=utf-8
```

### curl

```
$ curl -X DELETE -H "Cache-Control: no-cache" http://localhost/locks/aqua/
```
