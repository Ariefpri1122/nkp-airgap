id: pg_to_delta_pipeline
namespace: ingestion

triggers:
  - id: every_5_minutes
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "*/5 * * * *"

tasks:
  - id: pg_to_bronze
    type: io.kestra.plugin.scripts.shell.Script
    runner: PROCESS
    script: |
      set -ex
      ssh -o StrictHostKeyChecking=no nutanix@10.54.60.242 << EOF
      export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
      export SPARK_HOME=/opt/spark
      export PATH=\$SPARK_HOME/bin:\$JAVA_HOME/bin:\$PATH

      spark-submit \
        --packages io.delta:delta-spark_2.12:3.1.0,org.postgresql:postgresql:42.7.3 \
        /opt/jobs/pg_to_delta.py
      EOF

  - id: bronze_to_silver
    type: io.kestra.plugin.scripts.shell.Script
    runner: PROCESS
    script: |
      set -ex
      ssh -o StrictHostKeyChecking=no nutanix@10.54.60.242 << EOF
      export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
      export SPARK_HOME=/opt/spark
      export PATH=\$SPARK_HOME/bin:\$JAVA_HOME/bin:\$PATH

      spark-submit \
        --packages io.delta:delta-spark_2.12:3.1.0 \
        /opt/jobs/bronze_to_silver.py
      EOF

  - id: silver_to_gold
    type: io.kestra.plugin.scripts.shell.Script
    runner: PROCESS
    script: |
      set -ex
      ssh -o StrictHostKeyChecking=no nutanix@10.54.60.242 << EOF
      export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
      export SPARK_HOME=/opt/spark
      export PATH=\$SPARK_HOME/bin:\$JAVA_HOME/bin:\$PATH

      spark-submit \
        --packages io.delta:delta-spark_2.12:3.1.0 \
        /opt/jobs/silver_to_gold.py
      EOF
