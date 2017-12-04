
class tekst():
    def __init__(self):
        self.plik = open('test.txt','r')
        self.tekst = self.plik.readlines()
        print(self.tekst)

    def __del__(self):
        self.plik.close()

    def znajdzlinie(self, dana):
        i=0
        for line in self.tekst:
            line = line.rstrip()
            if dana == line:
                return(i)
            i += 1

    def wypiszlinie(self):
        start = self.znajdzlinie("IMIONA:")+1
        stop = self.znajdzlinie("ZADANIE:")
        print("Start {}".format(start))
        print("Stop {}".format(stop))
        steps = stop - start

        l = []
        for step in range(steps):
            dana = self.tekst[step+start].rstrip()
            l.append(dana)
            print(dana)
        return l

if __name__ == '__main__':
    a = tekst()
    #print(a.wypiszlinie())
    a.wypiszlinie()