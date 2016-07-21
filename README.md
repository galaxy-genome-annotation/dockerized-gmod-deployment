# Galaxy/Apollo

This docker-compose.yml file specifies all of the infrastructure needed to run
the current iteration of GMOD products.

We have attempted to include as many "bells and whistles" as possible, which
means this approaches the level of "tech-demo" and away from something you
might wish to deploy as-is. That said, the deployment is very easy to customise
and adapt to your particular organisation's needs.

![](./media/network.png)

## Screenshots

**Galaxy** ...

![](./media/galaxy.png)

... allows you to load data in **Apollo**,

![](./media/apollo.png)

which in turn can be exported to **Chado** and **Tripal**.

![](./media/tripal.png)

But wait, there's more! Data in Chado is made available in **JBrowse**

![](./media/jbrowse.png)

and an experimental, AngularJS Chado Interface

![](./media/angular.png)


## Running

```
$ docker-compose up -d
$ docker-compose logs
```

## Services:

Service                          | Port
-------------------------------- | ----
Galaxy                           | 8200
Tripal (/tripal)                 | 8200/tripal
Apollo (through Galaxy, /apollo) | 8200/apollo
PostgREST                        | 8300
Angular Chado Admin              | 8200/chado/
Chado JBrowse Connector          | 8200/jbrowse/

## Credentials

Service | Username         | Password
------- | ---------------- | ---------
Galaxy  | admin@galaxy.org | admin
Tripal  | admin            | changeme

## Dependencies

This `docker-compose.yml` depends on a large number of containers. We link some
build status images here for developer convenience

Image               | Status
-----               | ------
galaxy              | ![](https://quay.io/repository/erasche/docker-galaxy-annotation/status)
postgrest           | ![](https://quay.io/repository/erasche/postgrest/status)
chado-angular       | ![](https://quay.io/repository/erasche/chado-angular-admin/status)
chado-jb-connectory | ![](https://quay.io/repository/erasche/chado-jbrowse-connector/status)
chado               | ![](https://quay.io/repository/erasche/chado/status)
tripal              | ![](https://quay.io/repository/erasche/tripal/status)

## LICENSE

GPLv3
