# dbt-databricks-demo

# prerequisites:
* poetry >= 1.8.3
* python >= 3.12

```
poetry config virtualenvs.create true
poetry env use 3.12
poetry init


poetry add dbt-core
poetry add dbt-databricks

```



```
docker build -t dbt .
docker run -p 8581:8580 --name dbt_rpc -v "/$(pwd):/app" --env-file ./.env -it dbt
docker run dbt dbt run


```