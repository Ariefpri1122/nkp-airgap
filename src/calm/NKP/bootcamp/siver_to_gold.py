from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, current_timestamp
from delta.tables import DeltaTable

spark = (
    SparkSession.builder
    .appName("silver_to_gold_digital_payments_summary")
    .getOrCreate()
)

# ======================
# PATHS
# ======================
silver_path = "s3a://datalake/delta/silver/digital_payments"
gold_path   = "s3a://datalake/delta/gold/digital_payments_summary"

# ======================
# READ SILVER
# ======================
silver_df = spark.read.format("delta").load(silver_path)

# ======================
# AGGREGATE
# ======================
gold_df = (
    silver_df
    .groupBy("channel")
    .agg(
        count("*").alias("txn_count"),
        sum("amount").alias("total_amount")
    )
    .withColumn("last_updated", current_timestamp())
)

# ======================
# UPSERT TO GOLD
# ======================
if DeltaTable.isDeltaTable(spark, gold_path):
    gold_table = DeltaTable.forPath(spark, gold_path)

    (
        gold_table.alias("t")
        .merge(
            gold_df.alias("s"),
            "t.channel = s.channel"
        )
        .whenMatchedUpdate(set={
            "txn_count": "s.txn_count",
            "total_amount": "s.total_amount",
            "last_updated": "s.last_updated"
        })
        .whenNotMatchedInsertAll()
        .execute()
"silver_to_gold.py" 65L, 1531B
