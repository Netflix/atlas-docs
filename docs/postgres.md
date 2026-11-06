# PostgreSQL query backend

The [`atlas-postgres` module](https://github.com/Netflix/atlas/tree/main/atlas-postgres)
provides a PostgreSQL-backed `Database` for querying time-series blocks and
tags. It is **not a drop-in persistent replacement** for the in-memory Atlas
server described in [Memory Storage](overview.md#memory-storage).

In particular, changing `atlas.core.db.class` in `conf/memory.conf` to
`com.netflix.atlas.postgres.PostgresDatabase` is insufficient:

- `PostgresDatabase` requires a started `PostgresService` in its constructor.
  The default web API's `DatabaseSupplier` selects a class from
  `atlas.core.db.class`, but does not set up that service.
- The default `LocalPublishActor` casts the configured database to
  `MemoryDatabase` when receiving datapoints. It cannot publish into
  `PostgresDatabase`.
- The PostgreSQL module reads existing time-suffixed tables. It does not
  provide a pipeline that writes incoming metrics to them.

## Integrating the module

A custom application using this backend must include `atlas-postgres` and its
runtime dependencies, configure and start `PostgresService`, supply that
service to `PostgresDatabase`, and provide its own data-loading path. It must
also create the `atlas` schema and the time-suffixed tables that the queries
read. `SqlUtils.createSchema` and `SqlUtils.createTable` provide the SQL used
by the module's tests; `PostgresService` does not create the tables.

The following is an example of **service configuration only**, based on the
module's tests. It is not a complete Atlas server configuration:

```hocon
atlas.postgres {
  driver = "org.postgresql.Driver"
  url = "jdbc:postgresql://localhost:5432/atlas"
  user = "atlas"
  password = ${?ATLAS_POSTGRES_PASSWORD}
  init-statements = ["create extension if not exists hstore"]
  block-size = 360
  step = 10s
  tables = [
    {
      metric-name = "*"
      table-name = "others"
      columns = ["name"]
    }
  ]
}
```

`PostgresService` reads the connection settings, executes
`init-statements`, and installs SQL helper functions on startup.
`PostgresDatabase` reads `block-size` and `step`; the table definitions map
metric names and tag columns to the tables. Set these values to match the
tables and data loader in your application. The PostgreSQL role needs the
permissions required by the chosen initialization and loading process.

For working examples of the service setup and table/query behavior, see
[`PostgresSuite`](https://github.com/Netflix/atlas/blob/main/atlas-postgres/src/test/scala/com/netflix/atlas/postgres/PostgresSuite.scala)
and
[`PostgresDatabaseSuite`](https://github.com/Netflix/atlas/blob/main/atlas-postgres/src/test/scala/com/netflix/atlas/postgres/PostgresDatabaseSuite.scala).
The default wiring is in
[`DatabaseSupplier`](https://github.com/Netflix/atlas/blob/main/atlas-webapi/src/main/scala/com/netflix/atlas/webapi/DatabaseSupplier.scala)
and
[`LocalPublishActor`](https://github.com/Netflix/atlas/blob/main/atlas-webapi/src/main/scala/com/netflix/atlas/webapi/LocalPublishActor.scala).
