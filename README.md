# Galaxy/Apollo

This docker-compose.yml file specifies all of the infrastructure needed to run
a linked Galaxy and Apollo instance.

![](./apollo.png)


## Running

```
$ docker-compose up -d
$ docker-compose logs
```

## Services:

Service                 | Port
----------------------- | ----
Galaxy                  | 8200
Apollo (through Galaxy) | 8200
PostgREST               | 8300
Angular Chado Admin     | 8400
Chado JBrowse Connector | 8500


## LICENSE

GPLv3
