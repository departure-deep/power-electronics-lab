"""Shared utilities for DC-DC converter simulation."""

import numpy as np


def ripple_voltage(i_load, duty, f_sw, c_out):
    """Calculate output voltage ripple / 计算输出电压纹波
    ΔV = I_load * D / (f_sw * C_out)
    """
    return i_load * duty / (f_sw * c_out)


def ripple_current(v_in, v_out, duty, f_sw, l):
    """Calculate inductor current ripple / 计算电感电流纹波
    ΔI = (V_in - V_out) * D / (f_sw * L)
    """
    return (v_in - v_out) * duty / (f_sw * l)


def efficiency(p_out, p_loss):
    """Calculate efficiency / 计算效率"""
    return p_out / (p_out + p_loss) * 100 if (p_out + p_loss) > 0 else 0


def estimate_dcr_loss(i_rms, dcr):
    """Estimate inductor DCR copper loss / 估算电感DCR铜损"""
    return i_rms ** 2 * dcr


def estimate_switching_loss(v_ds, i_d, t_sw, f_sw):
    """Estimate MOSFET switching loss / 估算MOSFET开关损耗"""
    return 0.5 * v_ds * i_d * t_sw * f_sw
