id: lakehouse_pg_to_delta_pipeline
namespace: ingestion

description: |
  Postgres → Delta Lake incremental pipeline
  Bronze → Silver → Gold (SSH-based Spark execution)

triggers:
  - id: every_5_minutes
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "*/5 * * * *"

tasks:
  # =========================
  # TASK 1 — POSTGRES → BRONZE
  # =========================
  - id: pg_to_bronze
    type: io.kestra.plugin.scripts.shell.Script
    runner: PROCESS
    script: |
      set -ex

      echo "▶ Running PG -> Delta (Bronze)"

      ssh -o StrictHostKeyChecking=no nutanix@10.54.60.242 << EOF
      set -ex

      export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
      export SPARK_HOME=/opt/spark
      export PATH=\$SPARK_HOME/bin:\$JAVA_HOME/bin:\$PATH

      spark-submit \
        --packages io.delta:delta-spark_2.12:3.1.0,org.postgresql:postgresql:42.7.3 \
        /opt/jobs/pg_to_delta.py 2>&1 | tee /tmp/pg_to_delta.log
      EOF

  # =========================
  # TASK 2 — BRONZE → SILVER
  # =========================
  - id: bronze_to_silver
    type: io.kestra.plugin.scripts.shell.Script
    runner: PROCESS
    dependsOn:
      - pg_to_bronze
    script: |
      set -ex

      echo "▶ Running Bronze -> Silver"

      ssh -o StrictHostKeyChecking=no nutanix@10.54.60.242 << EOF
      set -ex

      export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
      export SPARK_HOME=/opt/spark
      export PATH=\$SPARK_HOME/bin:\$JAVA_HOME/bin:\$PATH

      spark-submit \
        --packages io.delta:delta-spark_2.12:3.1.0 \
        /opt/jobs/bronze_to_silver.py 2>&1 | tee /tmp/bronze_to_silver.log
      EOF

  # =========================
  # TASK 3 — SILVER → GOLD
  # =========================
  - id: silver_to_gold
    type: io.kestra.plugin.scripts.shell.Script
    runner: PROCESS
    dependsOn:
      - bronze_to_silver
    script: |
      set -ex

      echo "▶ Running Silver -> Gold"

      ssh -o StrictHostKeyChecking=no nutanix@10.54.60.242 << EOF
      set -ex

      export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
      export SPARK_HOME=/opt/spark
      export PATH=\$SPARK_HOME/bin:\$JAVA_HOME/bin:\$PATH

      spark-submit \
        --packages io.delta:delta-spark_2.12:3.1.0 \
        /opt/jobs/silver_to_gold.py 2>&1 | tee /tmp/silver_to_gold.log
      EOF
