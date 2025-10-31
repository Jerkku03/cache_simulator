

class CPU:
    def __init__(self, cache, dram):
        self.cache = cache
        self.dram = dram

    
    def memRequest(self, reqType, address, data_out):
        #address and type change pos in getAddress
        #read
        if (reqType == 0):
            data_in = self.cache.getAddress(address, reqType, data_out, self.dram)
            print(data_in)
        #write
        elif (reqType == 1):
            self.cache.getAddress(address, reqType, data_out, self.dram)
        else:
            print("wrong request type")
        

