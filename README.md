# Abstraction
High-dimensional vector data is becoming increasingly important in data science and AI applications. As a result, different database systems are built for managing vector data recently. Those systems can be broadly classified into two categories: specialized and gener- alized vector databases. Specialized vector databases (e.g., Facebook Faiss, Milvus, Microsoft SPTAG, Pinecone) are developed and op- timized explicitly and specifically for storing and querying vector data, while generalized vector databases (e.g., Alibaba PASE and AnalyticDB-V) support vector data management inside a relational database such as PostgreSQL. However, it is not clear about the performance comparison between the two approaches, and more importantly, what causes the performance gap. In this work, we present a comprehensive experimental study to systematically com- pare the two approaches in terms of index construction, index size, and query processing on a variety of real-world datasets. We drill down the underlying reasons that cause the performance gap and analyze whether the gap is bridgeable. Finally, we provide lessons and directions for building future vector databases that can simulta- neously achieve high performance and generality to serve a broad spectrum of applications.

# About This Repository
This repository contains code used for comparing performance of PASE and Faiss.

# PASE
PASE is an extension of PostgreSQL used for Approximate Nearest Neighbor Search. 
It has implemented two index: IVFFlat and HNSW. We implemented a new index IVFPQ in
this repository.

## Prerequisite

1. Install PostgreSQL11.0 (Pase may have conflicts with newer versions of PG)
2. Install Openmp

## Pase Building

1. Download PASE under folder `contrib` of PG
2. cd pase
3. `make USE_PGXS=`
4. `make install`
5. Start PG
6. Input `create extension pase;` in psql command line


## Original PASE Code:

- [Pase: PostgreSQL Ultra-High Dimensional Approximate Nearest Neighbor Search Extension](https://github.com/alipay/PASE)

# Faiss

- [Faiss: A Library for Efficient Similarity Search and Clustering of Dense Vectors](https://github.com/facebookresearch/faiss)



