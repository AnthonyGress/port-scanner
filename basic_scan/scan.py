from socket import *
import time
start_time = time.time()

if __name__ == '__main__':
    target = input('Enter the host to scan: ')
    t_IP = gethostbyname(target)
    print('Starting scan on host: ', t_IP)

    for i in range (50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            print('Port %d: OPEN' % (i,))
        s.close()
print('Time taken: ', time.time() - start_time)
