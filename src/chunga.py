import socket
import sys
import os

preferences = dict(readFromStdin=False,debug=False,minimalOutput=False,threads=4,inputFile='',verbose=False,outputFile='')
def usage():
    print("usage: {0} -c COUNT -f FILE [-i] [-v] [-d] [-o FILE] [-h]".format(sys.argv[0]))
    print("")
    print("Options:")
    print(" -c COUNT                Use COUNT worker processes")
    print(" -f FILE                 Read ip addresses from FILE (one per line)")  
    print(" -i                      Read ip addresses from standard input")
    print(" -v                      Be verbose")
    print(" -d                      Be very verbose. Print debug output too")
    print(" -m                      Print minimal output (good for scripting)")
    print(" -o FILE                 Write results to FILE")
    print(" -h                      Print help screen")

def scan_hosts(hosts,proc_count):
    if preferences['debug']:
        print('Worker #{0} given {1} hosts'.format(proc_count,len(hosts)))
    for host in hosts:
        ports_open = 0
        for port in range(1,65535):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.500)
                s.connect((host,port))
                s.close()
                ports_open = ports_open + 1
                if preferences['minimalOpen']:
                    print('{0}:{1}'.format(host,port))
                else:
                    print('{0} open {1}'.format(host,port))
            except Exception:
                s.close()
                if preferences['debug']:
                    print('{0} closed {1}'.format(host,port))

if len(sys.argv) < 2:
    usage()
    sys.exit(1)

i = 1
while i < len(sys.argv):
    if sys.argv[i] == '-h':
        usage()
        sys.exit(1)

    if sys.argv[i] == '-c':
        if len(sys.argv) == i + 1:
            print("ERROR: -c requires an argument")
            sys.exit(1)
        else:
            preferences['threads'] = int(sys.argv[i+1])
            i = i + 2
            continue
    elif sys.argv[i] == '-f':
        if len(sys.argv) == i + 1:
            print("ERROR: -f requires an argument")
            sys.exit(1)
        else:
            preferences['inputFile'] = sys.argv[i+1]
            i = i + 2
            continue
    elif sys.argv[i] == '-i':
        preferences['readFromStdin'] = True
        i = i + 1
        continue
    elif sys.argv[i] == '-v':
        preferences['verbose'] = True
        i = i + 1
        continue
    elif sys.argv[i] == '-d':
        preferences['debug'] = True
        i = i + 1
        continue
    elif sys.argv[i] == '-m':
        preferences['minimalOutput'] = True
        i = i + 1
        continue
    i = i + 1


pool = dict()
iteration = 0
count = 0
if preferences['readFromStdin'] == True:
    for line in sys.stdin:
        if iteration not in pool:
            pool[iteration] = []
        pool[iteration].append(line)
        iteration = iteration + 1
        if iteration == preferences['threads']:
            iteration = 0
        count = count + 1
elif len(preferences['inputFile']) > 0:
    with open(preferences['inputFile'],'r') as f:
        while 1:
            data = f.readline()[:-1]
            if len(data) == 0:
                break
            if iteration not in pool:
                pool[iteration] = []
            pool[iteration].append(data)
            iteration = iteration + 1
            if iteration == preferences['threads']:
                iteration = 0
            count = count + 1
    f.close()

if preferences['debug'] == True and preferences['minimalOutput'] == False:
    print('Read {0} entries'.format(count))
    print('Spawning {0} worker processes'.format(preferences['threads']))

for proc_count in range(0,preferences['threads']):
    if proc_count not in pool:
        continue
    val = os.fork()
    if val == 0:
        pid = os.getpid()
        scan_hosts(pool[proc_count],proc_count)
        sys.exit()
    elif val > 0:
        continue
    else:
        break
sys.exit()
