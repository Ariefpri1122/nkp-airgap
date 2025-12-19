from pyspark.sql import SparkSession
from pyspark.sql.functions import col, max as spark_max
from delta.tables import DeltaTable

# ======================
# CONFIG
# ======================
PG_URL = "jdbc:postgresql://10.54.59.93:5432/digitalbanking_db"
PG_TABLE = "digital_payments"
PG_USER = "postgres"
PG_PASSWORD = "nutanix/4u"

DELTA_PATH = "s3a://datalake/delta/digital_payments"
CHECKPOINT_PATH = "s3a://datalake/delta/_checkpoints/digital_payments"

# ======================
# SPARK
# ======================
spark = (
    SparkSession.builder
    .appName("pg_to_delta_incremental")
    .getOrCreate()
)

# ======================
# LOAD LAST WATERMARK
# ======================
try:
    checkpoint_df = spark.read.format("delta").load(CHECKPOINT_PATH)
    last_ts = checkpoint_df.select(spark_max("last_ts")).collect()[0][0]
except:
    last_ts = None

# ======================
# READ POSTGRES
# ======================
query = f"(SELECT * FROM {PG_TABLE}"
if last_ts:
    query += f" WHERE created_at > '{last_ts}'"
query += ") t"

pg_df = (
    spark.read.format("jdbc")
    .option("url", PG_URL)
    .option("dbtable", query)
    .option("user", PG_USER)
    .option("password", PG_PASSWORD)
    .option("driver", "org.postgresql.Driver")
    .load()
)

if pg_df.count() == 0:
    print("No new data")
"pg_to_delta.py" 74L, 1838B
