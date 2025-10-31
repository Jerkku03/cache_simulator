from dram import DRAM

class CACHE:
    def __init__(self):
        self.cacheMemory = [i for i in range(16)]

    def miss(self, address, type, data_out, dram):
        #read
        if (type == 0):
            data = dram.read(address)
            self.cacheMemory[int(bin(address)[2:].zfill(6), 2)] = data
            print((bin(address)[2:].zfill(6)))
                #check if tag in cache to overwrite
                #if any(bin(address)[2:4].zfill(6) in str(x) for x in self.cacheMemory):
                    #replace cache address with new
                    #self.cacheMemory[int(bin(address)[2:].zfill(6))] = self.cacheMemory.pop(bin(address)[2:4].zfill(6) in x for x in self.cacheMemory)
            return data
        #write
        if (type == 1):
            dram.write(address, data_out)

    def hit(self, address, type, data_out, dram):
        #if read
            if (type == 0):
                return self.cacheMemory[int(bin(address)[2:].zfill(6),2)]
            #if write
            if (type == 1):
                dram.write(address, data_out)


    #check if address in cache
    def getAddress(self, address, type, data_out, dram):
        #check index and tag
        if (int(bin(address)[2:].zfill(6),2) in self.cacheMemory): 
            print(f"< address - {address} > HIT")
            self.hit(address, type, data_out, dram)
        else: 
            print(f"< address - {address} > MISS")
            self.miss(address, type, data_out, dram)

    

    

        
