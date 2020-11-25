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

cp_pes = 397
cp_mems = 8
# cp_total = cp_pes + cp_mems

cp_cycle_exe_time = float(4122)
cp_ops_per_cycle = float(397)

def apply_model(pe_count, mem_count, cycle_exe_time, ops_per_cycle):

    cycles_per_sec = float(1e9)
    cp_total = pe_count + mem_count
    m_pe_power = pe_power_model[0]*cp_pes + pe_power_model[1]
    m_mem_power = mem_power_model[0]*cp_mems + mem_power_model[1]
    m_ic_power = ic_power_model[0]*cp_total + ic_power_model[1]

    m_power_mw = m_pe_power + m_mem_power + m_ic_power
    print('Total power in mW:', m_power_mw)
    # return m_power_mw

    cp_power_mw = m_power_mw
    # cp_power_mw = apply_model(cp_pes, cp_mems)

    cp_ops = ops_per_cycle*cycle_exe_time

    print('# ops in CP:', cp_ops)

    cp_exe_time_sec = cycle_exe_time / cycles_per_sec

    print('Exe time cp (sec):', cp_exe_time_sec)

    cp_power_watts = cp_power_mw / 1000
    print('power (Watts)', cp_power_watts)

    cp_energy_joules = cp_power_watts * cp_exe_time_sec
    print('Energy consumed =', cp_energy_joules)

    print('Energy / op =', cp_energy_joules / cp_ops)

print('==== Camera pipeline...')
apply_model(cp_pes, cp_mems, cp_cycle_exe_time, cp_ops_per_cycle)

print('\n\n')
print('==== Mobilenet...')
mn_pes = 114
mn_mems = 7 
mn_cycle_exe_time = 1026
mn_ops_per_cycle = 114

apply_model(mn_pes, mn_mems, mn_cycle_exe_time, mn_ops_per_cycle) 
