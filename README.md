# Pygmy TCP Port Scanner
A joke project that poorly scans IP addresses. It uses several processes to distribute the work across many different cores.

# Two different versions
1. There's the single threaded version
  - called `pygmy`
2. The "multi-threaded" version
  - called `chunga`
  - uses several processes (via `os.fork`)

## Pygmy: The single-threaded version
```
./bin/pygmy 127.0.0.1 127.0.0.2 127.0.0.3 127.0.0.4
```

## Chunga: The "Multi-threaded" version
```
./bin/chunga 8 ips.txt
```
The only difference between the two versions is the latter will spawn 8 processes and distribute the workload. This version will read the list of IP addresses that you would like to scan from the file named `ips.txt`.

### Chunga: The help file
```
usage: ./bin/chunga -c COUNT -f FILE [-i] [-v] [-d] [-o FILE] [-h]
Options:
 -c COUNT                Use COUNT worker processes
 -f FILE                 Read ip addresses from FILE (one per line)
 -i                      Read ip addresses from standard input
 -v                      Be verbose
 -d                      Be very verbose. Print debug output too
 -m                      Print minimal output (good for scripting)
 -o FILE                 Write results to FILE
 -h                      Print help screen
```

# LICENSE
This code uses the MIT license. 
See the [LICENSE](LICENSE) file for more info.

# VERSION
`v1.1.2`
