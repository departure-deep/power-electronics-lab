"""Buck (step-down) DC-DC converter simulation.
降压 DC-DC 变换器仿真
"""

import numpy as np
from .utils import ripple_voltage, ripple_current


class BuckConverter:
    """Buck converter model / 降压变换器模型

    Vout = D * Vin
    """

    def __init__(self, vin, duty, f_sw, l, c_out, r_load):
        self.vin = vin
        self.duty = duty
        self.f_sw = f_sw
        self.l = l
        self.c_out = c_out
        self.r_load = r_load

    @property
    def vout(self):
        """Output voltage / 输出电压"""
        return self.duty * self.vin

    @property
    def i_load(self):
        """Load current / 负载电流"""
        return self.vout / self.r_load

    @property
    def voltage_ripple(self):
        """Output voltage ripple / 输出电压纹波"""
        return ripple_voltage(self.i_load, self.duty, self.f_sw, self.c_out)

    @property
    def current_ripple(self):
        """Inductor current ripple / 电感电流纹波"""
        return ripple_current(self.vin, self.vout, self.duty, self.f_sw, self.l)

    def simulate(self, t_end, dt=None):
        """Simulate time-domain waveform / 时域波形仿真
        Returns: (t, v_out, i_l) arrays
        """
        if dt is None:
            dt = 1.0 / (self.f_sw * 1000)  # 1000 points per switching cycle
        t = np.arange(0, t_end, dt)
        v_out = np.full_like(t, self.vout)
        # Add ripple
        v_ripple = self.voltage_ripple * np.sin(2 * np.pi * self.f_sw * t)
        v_out += v_ripple
        # Inductor current
        i_l = np.full_like(t, self.i_load)
        i_ripple = self.current_ripple * np.sin(2 * np.pi * self.f_sw * t + np.pi/4)
        i_l += i_ripple
        return t, v_out, i_l

    def __repr__(self):
        return (f"BuckConverter(Vin={self.vin}V, D={self.duty}, "
                f"Vout={self.vout:.2f}V, f_sw={self.f_sw}kHz)")
