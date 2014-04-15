#!/usr/bin/env python
import errno
import sys
import traceback
import urllib
import os
import os.path
import threading

def wget(url, filename):
    urllib.urlretrieve(url, filename)

def makedirs(path):
    try:
        os.makedirs(path)
    except Exception, e:
        pass

class OptThread (threading.Thread):
    def __init__(self, opt):
        threading.Thread.__init__(self)
        self.opt = opt
    def run(self):
        path = 'img/%s' % (self.opt[1])
        makedirs(path)
        for num in self.opt[2]:
            fil = 'img/%s/%s.png' % (self.opt[1], num)
            if not os.path.isfile(fil):
                link = 'http://www.oyumucaldirtmam.com/tutanaklar/6_%s_%s.png' % (self.opt[0], num)
                wget(link, fil)
                print '%s -> %s' % (link, fil)
    

def dump():
    opts = ((30,	'ALTINDAG',	range(1001, 2483)), 
            (56,	'AYAS',	    range(1001, 1055) + range(9900, 9901)),
            (86,	'BEYPAZAR',	range(1001, 1168)),
            (129,	'CANKAYA',	range(1002, 4588)),
            (158,	'CUBUKLU',	range(1002, 1242)),
            (200,	'ELMADAG',	range(9900,9901)),
            (262,	'GUDUL',	range(1002, 1042)),
            (284,	'HAYMANA',	range(1001, 1143)),
            (322,	'KALECIK',	range(1001, 1070) + range(9900, 9901)),
            (432,	'NALLIHAN',	range(1001, 1135)),
            (471,	'POLATLI',	range(1001, 1316)),
            (551,	'SEREFLIKOCHISAR', range(1001, 1118) + range(9900, 9901)),
            (616,	'YENIMAHALLE', range(1001, 3372) + range(9900, 9901)),
            (637,	'GOLBASI',	range(1001, 1268)),
            (638,	'KECIOREN',	range(1001, 3512)),
            (639,	'MAMAK',	range(1001, 2288)),
            (640,	'SINCAN',	range(1001, 2701) + range(9900, 9911)),
            (708,	'KAZAN',	range(1001, 1130)),
            (765,	'AKYURT',	range(1001, 1077)),
            (815,	'ETIMESGUT',range(1001, 2390)),
            (817,	'EVREN',	range(1001, 1017)),
            (983,	'PURSAKLAR',range(1001, 1269)))

    for opt in opts:
        thread = OptThread(opt)
        thread.start()

def main():

    try:
        try:
            dump()
        except Exception, e:
		    sys.stderr.write(repr(e))
		    sys.stderr.write('\n')
		    traceback.print_exc(file=sys.stderr)

    except Exception, e:
        sys.stderr.write(repr(e))
        traceback.print_exc(file=sys.stderr)


if __name__ == '__main__':
    main()


