import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Read from S3
df = spark.read.csv("s3://your-bucket/sales-raw/", header=True)

# Clean nulls
df_clean = df.dropna()

# Write to Redshift
df_clean.write \
    .format("jdbc") \
    .option("url", "jdbc:redshift://cluster-url:5439/database") \
    .option("dbtable", "public.sales_clean") \
    .option("user", "user") \
    .option("password", "password") \
    .save()

job.commit()
