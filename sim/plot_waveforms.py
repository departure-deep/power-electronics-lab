"""Waveform visualization for converter simulation.
变换器波形可视化
"""

import numpy as np
try:
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False


def plot_waveforms(t, v_out, i_l, title="Converter Waveforms"):
    """Plot voltage and current waveforms / 绘制电压电流波形

    Args:
        t: Time array / 时间数组
        v_out: Output voltage array / 输出电压数组
        i_l: Inductor current array / 电感电流数组
        title: Plot title / 图表标题
    """
    if not HAS_MPL:
        print("matplotlib not installed. Data printed instead.")
        print(f"V_out: mean={np.mean(v_out):.3f}V, ripple={np.ptp(v_out):.3f}V")
        print(f"I_L: mean={np.mean(i_l):.3f}A, ripple={np.ptp(i_l):.3f}A")
        return

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
    fig.suptitle(title)

    ax1.plot(t * 1000, v_out, 'b-', linewidth=0.5)
    ax1.set_ylabel('Voltage (V) / 电压')
    ax1.grid(True, alpha=0.3)
    ax1.set_title(f'V_out = {np.mean(v_out):.2f}V, Ripple = {np.ptp(v_out)*1000:.1f}mV')

    ax2.plot(t * 1000, i_l, 'r-', linewidth=0.5)
    ax2.set_xlabel('Time (ms) / 时间')
    ax2.set_ylabel('Current (A) / 电流')
    ax2.grid(True, alpha=0.3)
    ax2.set_title(f'I_L = {np.mean(i_l):.3f}A, Ripple = {np.ptp(i_l)*1000:.1f}mA')

    plt.tight_layout()
    plt.savefig('waveforms.png', dpi=150)
    plt.show()
    print("Saved to waveforms.png")
