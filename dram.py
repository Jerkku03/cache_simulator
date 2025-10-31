
class DRAM:
    def __init__(self):
        self.mem = [i for i in range(64)]

    def write(self, address, data):
        self.mem[address] = data

    def read(self, address):
        return self.mem[address]


    #for i in range(64): # Iterate through 0 to 63
        #print(f"Decimal: {i}, Hex: {hex(i)}, Binary: {bin(i)[2:].zfill(6)}")