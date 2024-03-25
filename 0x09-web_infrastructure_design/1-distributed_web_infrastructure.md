Why Additional Elements:

Adding multiple servers provides redundancy, scalability, and load distribution, ensuring the website remains available and responsive under varying workloads.
Load Balancer Configuration:

The load balancer is configured with a Round Robin distribution algorithm, which cyclically routes incoming requests among available servers. This ensures fair resource utilization and prevents overloading of any single server.
Active-Active vs. Active-Passive Setup:

The load balancer enables an Active-Active setup, where all servers actively handle incoming requests simultaneously. In contrast, an Active-Passive setup would involve one server being active while others remain on standby, only becoming active if the primary server fails.
Database Primary-Replica Cluster:

In a Primary-Replica cluster, the Primary node (Master) accepts write operations and serves as the authoritative source for data changes. The Replica nodes (Slaves) replicate data from the Primary node to provide redundancy and read scalability. Writes occur on the Primary node, while reads can be distributed across both Primary and Replica nodes.
Difference Between Primary and Replica Nodes:

The Primary node accepts write operations, making changes to the database based on user interactions with the application. The Replica nodes replicate this data and serve read requests. In terms of the application, the Primary node is responsible for handling write operations, ensuring data consistency and integrity, while Replica nodes primarily serve read operations, improving scalability and performance.
Issues:
Single Points of Failure (SPOF):

Despite having multiple servers, each component (load balancer, web servers, application servers, and database) can still become a single point of failure if not properly configured for redundancy.
Security Issues:

Lack of firewall configurations exposes servers to potential attacks. Additionally, the absence of HTTPS encryption leaves data exchanged between clients and servers vulnerable to interception and manipulation, posing significant security risks.
No Monitoring:

Without monitoring tools in place, it's challenging to detect and address performance issues, security breaches, or resource bottlenecks effectively. Monitoring is essential for proactive maintenance and issue resolution, ensuring the infrastructure operates optimally and securely.
