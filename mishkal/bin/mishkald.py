#! /usr/bin/python2
# -*- coding: UTF-8 -*-

import socket, os, sys, select

base_dir = os.path.dirname(os.path.realpath(__file__))
#~ sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../support/'))
#~ sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../mishkal'))
#~ sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../')) # used for core
sys.path.append(os.path.join(base_dir, '../support/'))
sys.path.append(os.path.join(base_dir, '../mishkal'))
sys.path.append(os.path.join(base_dir, '../')) # used for core

import tashkeel.tashkeel as ArabicVocalizer
import core.adaat 
import pyarabic.araby as araby
import  time
import re
scriptversion = '0.3'
AuthorName = "chrys"

class mishkald():
    def __init__(self):
        self.ip = '127.0.0.1'
        self.running = True
        self.port = 6123
        self.bufferSize = 65536
        self.debug = False
        self.sockets = []
        self.acceptSock = None
        self.vocalizer = None
        self.conversion = {'a':' أي ',
              'A':' أي ',
              'b': ' بي ',
              'B': ' بي ',
              'c': ' سي ',
              'C': ' سي ',
              'd': ' دي ',
              'D': ' دي ',
              'e': ' إي ',
              'E': ' إي ',
              'f': ' اف ',
              'F': ' اف ',
              'g': ' جي ',
              'G': ' جي ',
              'h': ' هيتش ',
              'H': ' هيتش ',
              'i': ' ايي ',
              'I': ' ايي ',
              'j': ' جَي ',
              'J': ' جَي ',
              'k': ' كَي ',
              'K': ' كَي ',
              'l': ' إل ',
              'L': ' إل ',
              'm': ' إم ',
              'M': ' إم ',
              'n': ' إن ',
              'N': ' إن ',
              'o': ' آو ',
              'O': ' آو ',
              'p': ' بِيِي ',
              'P': ' بِيِي ',
              'q': ' كِو ',
              'Q': ' كِو ',
              'r': ' أر ',
              'R': ' أر ',
              's': ' إس ',
              'S': ' إس ',
              't': ' تي ',
              'T': ' تي ',
              'u': ' يو ',
              'U': ' يو ',
              'v': ' في ',
              'V': ' في ',
              'w': ' دبليو ',
              'W': ' دبليو ',
              'x': ' إكس ',
              'X': ' إكس ',
              'y': ' وَاي ',
              'Y': ' وَاي ',
              'z': ' زي ',
              'Z': ' زي ',
			  
              }
    def getSockets(self):
        return self.sockets
    def post_processing(self,text):
        text = re.sub("([A-Za-z0-9][ ]*)(:)",r'\1'+' كولن '.decode("utf-8"),text)
        text = re.sub("(:)([ ]*[A-Za-z0-9])",' كولن '.decode("utf-8") + r'\2',text)

        for key in self.conversion:
            text = text.replace(key.decode("utf-8"),self.conversion[key].decode("utf-8"))
        return text
    def addSocket(self, conn):
        self.sockets.append(conn)
    def closeSock(self, conn):
        try:
            conn.close()
        except:
            pass
        try:
            self.sockets.remove(conn)
        except:
            pass
    def isSocketsEmpty(self):
        return self.sockets == []
    def isRunning(self):
        return self.running
    def setRunning(self, running):
        self.running = running
    def getData(self, conn):
        options ={
            "text" : None,
        }
        try:
            data = conn.recv(self.bufferSize)
            ready, _, _ = select.select([conn], [], [], 0)

            while ready != []:
                data += conn.recv(self.bufferSize)
                if '\00' in data:
                    break
                ready, _, _ = select.select([conn], [], [], 0)
            print "FIRST THINGS FIRST"
            print data
            arr = bytearray(data)
            print arr
            for item in arr:
                print item
            print "FIXAY"
            print len(arr)
            options["text"] = data.decode('utf8').replace('\00', '')
            self.start_time = time.time()
        except:
            self.closeSock(conn)
            return (options)

        if not data:
            return (options)

        return (options)
    def isDebug(self):
        return self.debug
    def run(self):
        self.acceptSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.acceptSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.acceptSock.bind((self.ip, self.port))
        self.acceptSock.listen(1)
        self.addSocket(self.acceptSock)
        self.vocalizer = ArabicVocalizer.TashkeelClass('/tmp/mishkal_cache/')
        self.vocalizer.set_log_level(50) # critical
        while self.isRunning():
            ready, _, _ = select.select(self.getSockets(), [], [])
            # only accept connection and skip
            if self.acceptSock in ready:
                conn, addr = self.acceptSock.accept()
                self.addSocket(conn)
                ready.remove(self.acceptSock)
            # for better reading skip if there are no more requests
            if ready == []:
                continue
            # handle outstanding requests
            for conn in ready:
                options = self.getData(conn)
                text = options['text']

                if not text:
                    print 'Debugggg'
                    print text
                    print options
                    print '\n'
                    continue
                #print 'First' + text
                lines = text.split('\n')

                result = u''
                for line in lines:
                    line = line.strip()
                    if line == '':
                        continue
                    if line.startswith('#'):
                        continue

                    lineResult = self.vocalizer.tashkeel(line)
                    result += ' ' + lineResult

                    if self.isDebug():
                        if text:
                            print lineResult.strip('\n').encode('utf8')
                try:
                    answer = result + '\00'
                    print("--- %s seconds ---" % (time.time() - self.start_time))
                    answer = self.post_processing(answer)
                    print str(len(answer.encode('utf-8')))
                    conn.send(str(len(answer.encode('utf-8'))))
                    #conn.send(answer.encode('utf-8'))
                    if self.isDebug():
                        print result.strip('\n').encode('utf8')
                finally:
                    self.closeSock(conn)
                if self.isSocketsEmpty():
                    self.setRunning(false)

def main():
    app = mishkald()
    app.run()
    del app

if __name__ == '__main__':
    try:
        print 'start as daemon'
        pid = "/run/mishkal.pid"
        from daemonize import Daemonize
        daemon = Daemonize(app="mishkald", pid=pid, action=main)
        daemon.start()
    except Exception as e:
        print 'starting daemon failed, start in foreground'
        print e
        main()
