# Spam or Ham Detection
This project is performed on GCP Dataproc cluster with the aid of Pig, Hive and MapReduce to find the Top spam and ham keywords of a big data dataset



## Description of the tasks performed

1) Creating a cluster with 3 Worker and 1 Master node at GCP
2) Gathered a bigdata about Amazon customers and their reviews under the Cell Phones and Accessories category.
3) Performed cleaning on the data to make it eligible for further analysis
4) Have split the ham and spam datasets and found out the top 10 spam and ham accounts using Apache Pig.
5) With the help of Map Reduce found the TF-IDF of the top 10 spam keywords for each top
10 spam accounts.
6) With the help of Map Reduce found the TF-IDF of the top 10 ham keywords for each top
10 ham accounts.

## Formula to calculate Tf-Idf
Term Frequency - Inverse Document Frequency (TF-IDF) is a widely used statistical method in natural language processing and information retrieval. It measures how important a term is within a document relative to a collection of documents (i.e., relative to a corpus). 

Tf=(Total number of times the term appears in a document/total number of terms in the document)
Idf= Log(number of document in the corpus/number of document in the corpus containing the term)
TfIdf= Tf*Idf

## References
- 1)https://www.learndatasci.com/glossary/tf-idf-term-frequency-inverse-document-frequency/
- 2)https://pig.apache.org/docs/r0.17.0/api/org/apache/pig/piggybank/storage/CSVExcelStorage.html 
- 3)https://www.geeksforgeeks.org/tf-idf-model-for-page-ranking/ 
- 4)https://data.stackexchange.com/stackoverflow/query/new
- 5)https://stackoverflow.com/questions/20731966/regex-remove-all-special-characters-except-numbers
- 6)https://www.geeksforgeeks.org/removing-stop-words-nltk-python/



