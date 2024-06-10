# Postmortem: June 9, 2024, Web Stack Outage


## Issue Summary

- Duration: 2 hours 15 minutes (14:45 - 17:00 UTC-5)
- Impact: 60% of users experienced errors and slow loading times on our website and API.
- Root Cause: Misconfigured Nginx server and inadequate monitoring.

## Timeline

- 14:40 - Monitoring alert triggered for high error rates and slow response times.
- 14:45 - Engineer noticed issue and began investigating.
- 15:00 - Assumed root cause was database overload, began investigating DB performance.
- 15:20 - Realized DB was not the issue, escalated to backend team.
- 15:30 - Backend team investigated Nginx config, found misconfiguration.
- 16:00 - Began implementing fix, added monitoring for Nginx and server memory.
- 17:00 - Issue resolved.

## Root Cause and Resolution

- The misconfigured Nginx server caused requests to be routed incorrectly, leading to errors and slow loading times. The issue was fixed by updating the Nginx config and adding monitoring for Nginx and server memory to prevent similar issues in the future.

## Corrective and preventative measure

- Improve Nginx configuration management and monitoring.
- Add automated testing for Nginx config changes
- Increase frequency of server memory monitoring

- Tasks:
- Patch Nginx server with latest security updates.
- Add monitoring for Nginx request routing.
- Implement automated Nginx config testing.
- Schedule regular server memory usage reviews

This outage highlighted the importance of thorough monitoring and configuration management. By implementing these measures, we can prevent similar issues and improve our overall web stack reliability..
