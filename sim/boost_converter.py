"""Boost (step-up) DC-DC converter simulation.
升压 DC-DC 变换器仿真
"""

import numpy as np
from .utils import ripple_voltage, ripple_current


class BoostConverter:
    """Boost converter model / 升压变换器模型

    Vout = Vin / (1 - D)
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
        return self.vin / (1 - self.duty)

    @property
    def i_load(self):
        """Load current / 负载电流"""
        return self.vout / self.r_load

    @property
    def i_in(self):
        """Input current / 输入电流"""
        return self.i_load / (1 - self.duty)

    @property
    def voltage_ripple(self):
        """Output voltage ripple / 输出电压纹波"""
        return self.i_load * self.duty / (self.f_sw * self.c_out)

    @property
    def current_ripple(self):
        """Inductor current ripple / 电感电流纹波"""
        return self.vin * self.duty / (self.f_sw * self.l)

    def simulate(self, t_end, dt=None):
        """Simulate time-domain waveform / 时域波形仿真"""
        if dt is None:
            dt = 1.0 / (self.f_sw * 1000)
        t = np.arange(0, t_end, dt)
        v_out = np.full_like(t, self.vout) + self.voltage_ripple * np.sin(2 * np.pi * self.f_sw * t)
        i_l = np.full_like(t, self.i_in) + self.current_ripple * np.sin(2 * np.pi * self.f_sw * t)
        return t, v_out, i_l

    def __repr__(self):
        return (f"BoostConverter(Vin={self.vin}V, D={self.duty}, "
                f"Vout={self.vout:.2f}V, f_sw={self.f_sw}kHz)")
