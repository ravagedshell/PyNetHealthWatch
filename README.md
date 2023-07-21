# PyNetSecWatch, a headless Network Speed and Latency Tester

This is a tool I created back when I was working in the middle of bumb-f*** and was relying on Starlink and TMobile-5G internet to keep me connected. I created this tool to test latency and speed and used it to automatically trigger failover to the fastest available internet connection. I don't know if this even works still, it's Circa August-2022, and haven't had a need for it Since January, but figured someone might find it useful.

# Usage:
```bash
    # Test HTTP download speed with default options (20MB file, 5 iterations)
    PyNetHealthWatchSpeed.py --output <path-to-log-file>
    
    # Test HTTP download speed with specific size and iteraction count (to get averages)
    PyNetHealthWatchSpeed.py --size [ '5MB' | '10MB' | '20MB' | '50MB' | '100MB' | '200MB' | '512MB' | '1GB' ] --iterations <#-of-trys> --output <path-to-log-file>
    
    # Test latency against the default hosts
    PyNetHealthWatchLatency.py --output <path-to-log-file>

    # Test latency against a customer host
    PyNetHealthWatchLatency.py  --hostname <ip-or-hostname> --output <path-to-log-file>

    # Test latency against multiple hosts
    PyNetHealthWatchLatency.py  --hostfile <path-to-multiple-hosts-in-file> --output <path-to-log-file>
```