hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-file /home/agnideep_mukherjee2/TFIDF/mapper_1.py \
-mapper  'python3 mapper_1.py' \
-file /home/agnideep_mukherjee2/TFIDF/reducer_1.py \
-reducer 'python3 reducer_1.py' \
-input gs://dataproc-staging-us-central1-24631865637-6nswal7o/TFIDF_Ham/A1KRF81GTI2KKT.txt \
-output gs://dataproc-staging-us-central1-24631865637-6nswal7o/TFIDF_Ham/out1

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-file /home/agnideep_mukherjee2/TFIDF/mapper_2.py \
-mapper  'python3 mapper_2.py' \
-file /home/agnideep_mukherjee2/TFIDF/reducer_2.py \
-reducer 'python3 reducer_2.py' \
-input gs://dataproc-staging-us-central1-24631865637-6nswal7o/TFIDF_Ham/out1/ \
-output gs://dataproc-staging-us-central1-24631865637-6nswal7o/TFIDF_Ham/out2

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-file /home/agnideep_mukherjee2/TFIDF/mapper_3.py \
-mapper  'python3 mapper_3.py' \
-file /home/agnideep_mukherjee2/TFIDF/reducer_3.py \
-reducer 'python3 reducer_3.py' \
-input gs://dataproc-staging-us-central1-24631865637-6nswal7o/TFIDF_Ham/out2/ \
-output gs://dataproc-staging-us-central1-24631865637-6nswal7o/TFIDF_Ham/out3

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-file /home/agnideep_mukherjee2/TFIDF/mapper_4.py \
-mapper  'python3 mapper_4.py' \
-input gs://dataproc-staging-us-central1-24631865637-6nswal7o/TFIDF_Ham/out3/ \
-output gs://dataproc-staging-us-central1-24631865637-6nswal7o/TFIDF_Ham/final

hadoop fs -getmerge gs://dataproc-staging-us-central1-24631865637-6nswal7o/TFIDF_Ham/final/ /home/agnideep_mukherjee2/TFIDF/results/A1KRF81GTI2KKT.txt