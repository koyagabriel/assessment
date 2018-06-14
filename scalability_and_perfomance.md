# Web Application Performance and Scalability

An application performance is measured in terms of its responsiveness, throughput, and resource utilization under a given workload. Note that an application performance will vary based on its workload.

Scalabilty refers to how an application is able to respond to additional load while maintaining the same level of performance by adding additional server resources such as CPU, memory, disk.

## Benefits of measuring performance and scalability

- Assess production readiness.
- Assess adequacy of software.
- Improve efficiency of performance tuning by identifying bottle necks.
- Accurate data on infrastructure requirements and costs to meet application performance and scalability goals.
- Assurance that current infrastructure will meet anticipated user demand.
- Reassurance to developers as regards having the knowledge whether pushing updates to software will affect the scalabilty and performance of the system.

## How to determine the scaling design to go for is mostly related with the we want to scale for long term or short term.

Generally when we want to scale for short term, you might consider vertical scaling. This is because is cheap and easy to implement. In a scenario where by you notice that the application is probably slow you can just increase the memory  (RAM) capacity of the system. Usually this scaling is limited and has only one server. For instance increasing the memory capacity of my machine for 8gb to 16gb to improve the system performance.

Horizontal scaling is more suitable for long term, this is because it more expensive to implement and in some cases you might to change the architecture and configuration of the system. This basically involves connecting multiple entities/ servers so that they work as a single logical unit.

## What to measure (Performance Metrics)

- Time To First Byte(TTFB): refers to how quickly the server sends back the first byte of a response to a given page request.
- Time To Last Byte(TTLB): refers to the time required to get all dependent requests including images, css and script files.

## What to measure (Load Characteristics)

- User Load: how many users are being simulated in accessing the system at a given time.
- Request per second.
- Errors per second.

## What to measure (Resource Utilization per server)

- CPU
- Memory
- Disk/Network

## Kinds of test

- Performance Test: determine or validate speed of the application.
- Load Test: Determines how an application's performance varies as load increases.
- Stress Test: its a kind of load test, that determines application behaviour when pushed beyond normal or peak load conditions.
