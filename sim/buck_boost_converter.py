"""Buck-Boost DC-DC converter simulation.
升降压 DC-DC 变换器仿真
"""

import numpy as np


class BuckBoostConverter:
    """Buck-Boost converter model / 升降压变换器模型

    Vout = -D * Vin / (1 - D)
    Note: output is inverted / 注意：输出为反向
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
        """Output voltage (inverted) / 输出电压（反向）"""
        return -self.duty * self.vin / (1 - self.duty)

    @property
    def abs_vout(self):
        """Absolute output voltage / 输出电压绝对值"""
        return abs(self.vout)

    @property
    def i_load(self):
        """Load current / 负载电流"""
        return self.abs_vout / self.r_load

    @property
    def voltage_ripple(self):
        """Output voltage ripple / 输出电压纹波"""
        return self.i_load * self.duty / (self.f_sw * self.c_out)

    def simulate(self, t_end, dt=None):
        """Simulate time-domain waveform / 时域波形仿真"""
        if dt is None:
            dt = 1.0 / (self.f_sw * 1000)
        t = np.arange(0, t_end, dt)
        v_out = np.full_like(t, self.vout) + self.voltage_ripple * np.sin(2 * np.pi * self.f_sw * t)
        i_l = np.full_like(t, self.i_load) + self.voltage_ripple * np.sin(2 * np.pi * self.f_sw * t)
        return t, v_out, i_l

    def __repr__(self):
        return (f"BuckBoostConverter(Vin={self.vin}V, D={self.duty}, "
                f"Vout={self.vout:.2f}V, f_sw={self.f_sw}kHz)")
