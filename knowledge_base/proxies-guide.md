# Practical Guide to Proxies

- **Residential proxies**: best for anti-bot evasion; costlier; IPs from real ISPs.
- **Datacenter proxies**: cheaper; faster; easier to block.
- **Rotation**: change IP per request to reduce correlation; use sticky sessions for login flows.
- **Session Management**: cookie jars, authenticated proxies `user:pass@host:port`.
- **Health Checks**: test via `httpbin.org/ip`; measure latency & success rate.
- **Backoff & Retry**: exponential backoff for 403/429/5xx; cap max attempts.
