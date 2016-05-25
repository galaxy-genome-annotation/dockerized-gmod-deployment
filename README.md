# Galaxy/Apollo

This docker-compose.yml file specifies all of the infrastructure needed to run
a linked Galaxy and Apollo instance.


## Running

```
$ docker-compose up -d
$ docker-compose ps proxy
Name                  Command                State   Ports
-----------------------------------------------------------------------------------
galaxyapollo_proxy_1  nginx -g daemon off;   Up      443/tcp, 0.0.0.0:32772->80/tcp

```

As you can see, the second command has printed out the port binding of the
proxy. You should be able to navigate to localhost:32772 (if you're running
boot2docker/on OSX you may need to find the VM's IP address first), and access
the integrated Apollo/Galaxy instances.

## LICENSE

GPLv3
