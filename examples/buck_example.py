"""Buck converter simulation example.
降压变换器仿真示例
"""

import sys
sys.path.insert(0, '..')

from sim import BuckConverter
from sim.plot_waveforms import plot_waveforms

# Parameters / 参数
buck = BuckConverter(
    vin=12.0,       # Input voltage / 输入电压 12V
    duty=0.5,       # Duty cycle / 占空比 50%
    f_sw=100e3,     # Switching freq / 开关频率 100kHz
    l=47e-6,        # Inductor / 电感 47µH
    c_out=100e-6,   # Output cap / 输出电容 100µF
    r_load=10.0     # Load resistance / 负载电阻 10Ω
)

print(buck)
print(f"Output voltage / 输出电压: {buck.vout:.2f}V")
print(f"Load current / 负载电流: {buck.i_load:.3f}A")
print(f"Voltage ripple / 电压纹波: {buck.voltage_ripple*1000:.2f}mV")
print(f"Current ripple / 电流纹波: {buck.current_ripple*1000:.2f}mA")

# Simulate / 仿真
t, v_out, i_l = buck.simulate(t_end=0.001)  # 1ms
plot_waveforms(t, v_out, i_l, title="Buck Converter Simulation / 降压变换器仿真")
