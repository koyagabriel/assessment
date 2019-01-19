# HASHING ALGORITHMS
A hashing algorithm is a cryptographic hash function. It is a mathematical algorithm that maps data of arbitrary size to a hash of a fixed size. It’s designed to be a one-way function, infeasible to invert.

The ultlimate goal of a hashing algorithm is to generate a safe hash.
**(A hash is a value computed from a base input number using a hashing algorithm)**.

Shortly, the hash value is a summary of the original data. For instance, think of a paper document that you squeeze and squeeze so that, in the end, you aren’t even able to read the content. It’s almost (in theory) impossible to restore the original input without knowing what was the starting data.

### Qualities of an ideal cryptographic hash function
1. It should be fast to compute the hash value for any kind of data.
2. It should be impossible to regenerate a message from its hash value.
3. It should avoid hash collisions, each message has its own hash.
4. Every change to a message, even the smallest one, should change the hash value. It should be completely different. It’s called the `avalanche effect`.


### What we use it for?
1. Digital Signatures.
2. Message authentication codes (MACs).
3. Identifying Files (used in `.lock files` for uniquely identifying packages).
4. Detecting duplicates or as checksums `(detecting if a file didn't suffer accidental or intentional data corruption)`.


#### MD5(Message Digest Algorithm)
It is a widely used hash function producing 128-but hash value. Although MD5 was initially designed to be used as a cryptographic hash function, it has been found to suffer from extensive vulnerabilities such as supporting **collision**. It can still be used as a checksum to verify data integrity, but only against unintentional corruption. It remains suitable for other non-cryptographic purposes, for example for determining the partition for a particular key in a partitioned database.

#### Collision
A collision or clash is a situation that occurs when two distinct pieces of data have the same hash value.


#### Linear Probing
Linear probing is a scheme in computer programming for resolving collisions in hash tables, data structures for maintaining a collection of key–value pairs and looking up the value associated with a given key. In these schemes, each cell of a hash table stores a single key–value pair. When the hash function causes a collision by mapping a new key to a cell of the hash table that is already occupied by another key, linear probing searches the table for the closest following free location and inserts the new key there.

In linear probing, we linearly probe for next slot. Example
```
If slot hash(x) % S is full, then we try (hash(x) + 1) % S
If (hash(x) + 1) % S is also full, then we try (hash(x) + 2) % S
If (hash(x) + 2) % S is also full, then we try (hash(x) + 3) % S 
```
