# Optimizing Database Queries

### Indexing
Indexing is a way to optimize performance of a database by minimizing the number of disk accesses required when a query is processed.

An index or database index is a data structure which is used to quickly locate and access the data in a database table.

Indexes are created using some database columns.

- The first column is the Search key that contains a copy of the primary key or candidate key of the table. These values are stored in sorted order so that the corresponding data can be accessed quickly.
- The second column is the Data Reference which contains a set of pointers holding the address of the disk block where that particular key value can be found.

### Partitioning
Partitioning is a general term used to describe the act of breaking up your logical data elements into multiple entities for the purpose of performance, availability, or maintainability.
Partitioning is more a generic term for dividing data across tables or databases.
We have two basic types of partitioning:
1. **Vertical Partitioning:** is the act of splitting up the data stored in one entity into multiple entities. For example, a customer might only have one billing address, yet I might choose to put the billing address information into a separate table with a CustomerId reference so that I have the flexibility to move that information into a separate database.
2. **Horizontal Partitioning or Sharding:** When you shard a database, you create replica's of the schema, and then divide what data is stored in each shard based on a shard key.  For example, I might shard my customer database using CustomerId as a shard key - I'd store ranges 0-10000 in one shard and 10001-20000 in a different shard.  

To summarize - partitioning is a generic term that just means dividing your logical entities into different physical entities for performance, availability, or some other purpose.  "Horizontal partitioning", or sharding, is replicating the schema, and then dividing the data based on a shard key.  "Vertical partitioning" involves dividing up the schema (and the data goes along for the ride).  

### Striping
Disk striping is a technique in which multiple smaller disks act as a single large disk. The process divides large data into data blocks and spreads them across multiple storage devices.

### Clustering
A database is a server that can store, filter and search data. Sometimes a single server is not enough to handle the amount of data or the amount of requests. Then you need a database cluster.

A database cluster basically means more than one database working together. They cluster together to provide a service. There are a few standard setups based on your needs:

**Master/slave replication.**

It basically means that you have one server with the truth, the master, and the slaves just copies anything the master does. This means that in setups that have many read requests and not so many write requests, you can read data from any of the slaves and if you want to write then you do it to the master. Any changes are then propagated to the slaves. This is a good setup for heavy read traffic.

**Master/master replication.**

Sometimes clustering is more about data security. That means that data need to exists on more than one server, to be reasonably sure that it won't disappear by way of a server crash. So a master/master replication means that two or more servers mirror each other.



