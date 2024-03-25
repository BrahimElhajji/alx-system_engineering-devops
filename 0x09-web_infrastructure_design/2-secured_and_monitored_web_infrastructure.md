Why Additional Elements:

Firewalls provide an additional layer of security to protect the servers from unauthorized access and potential threats.
Using an SSL certificate ensures secure communication between clients and servers, safeguarding sensitive data from interception.
Monitoring clients collect valuable data on server performance and behavior, enabling proactive management and troubleshooting.
Purpose of Firewalls:

Firewalls monitor and control incoming and outgoing network traffic based on predefined security rules. They prevent unauthorized access, block malicious attacks, and ensure the security and integrity of the network infrastructure.
Importance of HTTPS Traffic:

Serving traffic over HTTPS encrypts data transmitted between clients and servers, protecting it from interception and tampering. This ensures the confidentiality and integrity of sensitive information, such as user credentials, payment details, and personal data.
Role of Monitoring:

Monitoring is used to track the health, performance, and availability of the infrastructure and applications. It helps detect and diagnose issues, optimize resource usage, and ensure the reliability and efficiency of the system.
Data Collection by Monitoring Tools:

Monitoring tools collect data through monitoring clients installed on the servers. These clients continuously gather metrics, logs, and events related to server performance, network activity, and application behavior. The collected data is then transmitted to the monitoring service for analysis and visualization.
Monitoring Web Server QPS:

To monitor the web server QPS (Queries Per Second), you would configure the monitoring tool to collect metrics related to incoming HTTP requests. This could include metrics such as request count, response time, error rate, and server load. By analyzing these metrics, you can track the server's performance and identify any spikes or anomalies in request volume.
Issues:
Terminating SSL at Load Balancer Level:

Terminating SSL at the load balancer decrypts the HTTPS traffic before forwarding it to the backend servers. While this improves efficiency, it means that traffic between the load balancer and servers is unencrypted, potentially exposing sensitive data to interception if the internal network is compromised.
Single MySQL Server for Writes:

Relying on only one MySQL server capable of accepting writes creates a single point of failure. If this server fails or experiences issues, it could lead to downtime and data loss, impacting the availability and integrity of the application.
Uniformity in Server Components:

Having servers with identical components (database, web server, and application server) can pose a problem in terms of scalability and fault tolerance. If all servers are configured the same way, they may all fail simultaneously in the event of a common issue or vulnerability. Introducing diversity in server configurations can mitigate this risk and enhance resilience.
