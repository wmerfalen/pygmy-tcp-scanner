# ghetto tcp scanner
A joke project that poorly scans IP addresses. It uses several processes to distribute the work across many different cores.

# Two different versions
1. There's the single threaded version
2. The `chunga` version
  - uses several processes (via `os.fork`)

## Single threaded version
```
python3 ./src/main.py 127.0.0.1 127.0.0.2 127.0.0.3 127.0.0.4
```

## "Multi-threaded" version
```
python3 ./src/chunga.py 8 ips.txt
```
The only difference between the two versions is the latter will spawn 8 processes and distribute the workload. This version will read the list of IP addresses that you would like to scan from the file named `ips.txt`.


# LICENSE
This code uses the MIT license. See the [LICENSE](LICENSE) file for more info.
