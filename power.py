import numpy as np

# With resnet
# PEs = np.array([19, 28, 83, 0, 56, 48])
# Mems = np.array([1, 2, 5, 1, 6, 35])

# Without resnet
PEs = np.array([19, 28, 83, 0, 56])
PE_power_mw = np.array([6.86, 11.2, 26.9, 0, 8.8])

Mems = np.array([1, 2, 5, 1, 6])
Mem_power_mw = np.array([6.946, 14, 34, 3.13, 17.99])

total_tiles = PEs + Mems

Ic_power_mw = np.array([13.0, 22.7, 54.8, 0.35, 20.44])

print('PEs', PEs)
print('Mems', Mems)
print('Total', total_tiles)

pe_power_mw = np.polyfit([0, 1, 2], [0, 2, 4], 1)

print('polyfit test:', pe_power_mw)


pe_power_model = np.polyfit(PEs, PE_power_mw, 1)
print('pe power:', pe_power_model)
# slope = pe_power_model[0]
# offset = pe_power_model[1]


mem_power_model = np.polyfit(Mems, Mem_power_mw, 1)
print('mem power:', mem_power_model)

ic_power_model = np.polyfit(total_tiles, Ic_power_mw, 1)
print('ic power model:', ic_power_model)

