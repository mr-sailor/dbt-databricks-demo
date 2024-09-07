# # Databricks notebook source
# # MAGIC %sql
# # MAGIC -- Set up the defaults
# # MAGIC USE CATALOG mmm_development_bronze;
# # MAGIC USE SCHEMA test_schema;

# # COMMAND ----------

# # MAGIC %sql
# # MAGIC DROP TABLE mmm_development_bronze.test_schema.raw_listings

# # COMMAND ----------

# import pyspark.sql.functions as F

# # COMMAND ----------

# df = spark.read.csv("s3://dbtlearn/listings.csv", header=True)

# schema = {
#   "id": "integer",
#   "listing_url": "string",
#   "name": "string",
#   "room_type": "string",
#   "minimum_nights": "integer",
#   "host_id": "integer",
#   "price": "string",
#   "created_at": "timestamp",
#   "updated_at": "timestamp",
# }
# for k, v in schema.items():
#   df = df.withColumn(k, F.col(k).cast(v))


# df.write.format("delta").saveAsTable("mmm_development_bronze.test_schema.raw_listings")

# # COMMAND ----------

# df = spark.read.csv("s3://dbtlearn/reviews.csv", header=True)

# schema = {
#     "listing_id": "integer",
#     "date": "TIMESTAMP",
#     "reviewer_name": "string",
#     "comments": "string",
#     "sentiment": "string",
# }

# for k, v in schema.items():
#   df = df.withColumn(k, F.col(k).cast(v))

# df.write.format("delta").saveAsTable("mmm_development_bronze.test_schema.raw_reviews")

# # COMMAND ----------

# df = spark.read.csv("s3://dbtlearn/hosts.csv", header=True)

# schema = {
#     "id": "integer",
#     "name": "string",
#     "is_superhost": "string",
#     "created_at": "timestamp",
#     "updated_at": "timestamp",
# }

# for k, v in schema.items():
#   df = df.withColumn(k, F.col(k).cast(v))

# df.write.format("delta").saveAsTable("mmm_development_bronze.test_schema.raw_hosts")

# # COMMAND ----------

# spark.table("mmm_development_bronze.test_schema.raw_reviews")
