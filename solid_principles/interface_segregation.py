class IMultiFunctionDevice:
    def print(self):
        pass

    def scan(self):
        pass

    def fax(self):
        pass

    def copy(self):
        pass

class Printer(IMultiFunctionDevice):
    def print(self):
        print("Printing...")

class Scanner(IMultiFunctionDevice):
    def scan(self):
        print("Scanning")

class Copier(IMultiFunctionDevice):
    def copy(self):
        print("Copying...")

# Solution

class IPrinter:
    def print(self):
        pass

class IScanner:
    def scan(self):
        pass

class ICopier:
    def copy(self):
        pass

class IFax:
    def fax(self):
        pass

class Printer(IPrinter):
    def print(self):
        print("Printing...")

class Scanner(IScanner):
    def scan(self):
        print("Scanning")

class Copier(ICopier):
    def copy(self):
        print("Copying...")

class Fax(IFax):
    def fax(self):
        print("Faxing...")
# The IMultiFunctionDevice interface is broken down into smaller interfaces