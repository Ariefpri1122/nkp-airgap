id: pg_to_delta_pipeline
namespace: lakehouse

description: |
  Incremental Postgres → Delta Lake pipeline
  Bronze → Silver → Gold

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
      set -e
      echo "▶ Running Postgres → Bronze"

      ssh -o StrictHostKeyChecking=no nutanix@10.54.60.242 << 'EOF'
        export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
        export SPARK_HOME=/opt/spark
        export PATH=$SPARK_HOME/bin:$JAVA_HOME/bin:$PATH

        spark-submit \
          --packages io.delta:delta-spark_2.12:3.1.0 \
          /opt/jobs/pg_to_delta.py
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
      set -e
      echo "▶ Running Bronze → Silver"

      ssh -o StrictHostKeyChecking=no nutanix@10.54.60.242 << 'EOF'
        export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
        export SPARK_HOME=/opt/spark
        export PATH=$SPARK_HOME/bin:$JAVA_HOME/bin:$PATH

        spark-submit \
          --packages io.delta:delta-spark_2.12:3.1.0 \
          /opt/jobs/bronze_to_silver.py
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
      set -e
      echo "▶ Running Silver → Gold"

      ssh -o StrictHostKeyChecking=no nutanix@10.54.60.242 << 'EOF'
        export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
        export SPARK_HOME=/opt/spark
        export PATH=$SPARK_HOME/bin:$JAVA_HOME/bin:$PATH

        spark-submit \
          --packages io.delta:delta-spark_2.12:3.1.0 \
          /opt/jobs/silver_to_gold.py
      EOF
