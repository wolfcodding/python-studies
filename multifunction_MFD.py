'''Program emulates a multifunction device (MFD) class consisting of methods responsible for document scanning, printing, and sending via fax

The methods are delivered by the following classes:
* scan(), delivered by the Scanner class;
* print(), delivered by the Printer class;
* send() and print(), delivered by the Fax class.

Each method prints a message indicating its purpose and origin, like:
* 'print() method from Printer class'
* 'send() method from Fax class'

Instantiate the below classes:
* MFD_SPF class ('SPF' means 'Scanner', 'Printer', 'Fax')
* MFD_SFP class ('SFP' means 'Scanner', 'Fax', 'Printer')

Tests:
* on each object call the methods: scan(), print(), send();
* observe the output differences. Was the Printer class utilized each time?;

'''

class Scanner:
    def scan(self):
        print('scan() method from Scanner class')
    
class Printer:
    def print(self):
        print('print() method from Printer class')

class Fax:
    def send(self):
        print('send() method from Fax class')
    
    def print(self):
        print('print() method from Fax class')


class MFD_SPF(Scanner, Printer, Fax):
    def __repr__(self):
        return 'class MFD_SPF(Scanner, Printer, Fax)'

class MFD_SFP(Scanner, Fax, Printer):
    pass

MFDone = MFD_SPF()
MFDtwo = MFD_SFP()

#testing methods to point out nature of inheritance problems
for MFD in MFDone, MFDtwo:
    print('\nThese are ', type(MFD).__name__ , 'object methods where class', 
          ' sequence is {}, {}, {}'.format(*(x.__name__ for x in MFD.__class__.__bases__)),
            ':\n')
    for method in MFD.scan(), MFD.print(), MFD.send():
        method

