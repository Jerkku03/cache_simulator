from cache import CACHE
from dram import DRAM
from cpu import CPU

def simulate():
    dram = DRAM()
    cache = CACHE()
    cpu = CPU(cache, dram)
    cpu.memRequest(0,4,2)

simulate()