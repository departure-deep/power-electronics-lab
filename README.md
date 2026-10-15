# Power Electronics Lab 🔋

Simulation and analysis of DC-DC converters (buck, boost, buck-boost) with waveform visualization.

DC-DC 变换器（降压、升压、升降压）仿真与波形分析工具。

---

## Features / 功能特性

- **Buck converter simulation** — Vout = D × Vin
  降压变换器仿真
- **Boost converter simulation** — Vout = Vin / (1-D)
  升压变换器仿真
- **Buck-boost converter simulation** — Vout = -D × Vin / (1-D)
  升降压变换器仿真
- **Component selection calculator** — Inductor, capacitor sizing
  元器件选型计算 — 电感、电容参数计算
- **Efficiency analysis** — Conduction loss, switching loss estimation
  效率分析 — 导通损耗、开关损耗估算
- **Waveform visualization** — Voltage and current ripple plots
  波形可视化 — 电压电流纹波图表
- **Interactive parameter tuning** — Adjust duty cycle, frequency, etc.
  交互式参数调节 — 调整占空比、频率等

---

## Converter Models / 变换器模型

```
Buck (降压):       Vin ──[S]──[L]──[C]── Vout
                        └──[D]──┘

Boost (升压):      Vin ──[L]──[S]── Vout
                           └──[D]──[C]──

Buck-Boost (升降压): Vin ──[S]──[L]── Vout
                          └──[D]──┘
```

---

## Project Structure / 项目结构

```
power-electronics-lab/
├── sim/
│   ├── __init__.py           # Package init / 包初始化
│   ├── buck_converter.py     # Buck converter model / 降压模型
│   ├── boost_converter.py    # Boost converter model / 升压模型
│   ├── buck_boost_converter.py  # Buck-boost model / 升降压模型
│   ├── utils.py              # Shared utilities / 通用工具
│   └── plot_waveforms.py     # Waveform plotting / 波形绘制
├── examples/
│   └── buck_example.py       # Example usage / 使用示例
├── requirements.txt          # Python dependencies / Python 依赖
└── README.md
```

---

## Quick Start / 快速开始

```bash
# Install dependencies / 安装依赖
pip install -r requirements.txt

# Run example / 运行示例
python examples/buck_example.py
```

### Usage in Code / 代码中使用

```python
from sim import BuckConverter
from sim.plot_waveforms import plot_waveforms

buck = BuckConverter(
    vin=12.0,       # 12V input / 12V输入
    duty=0.5,       # 50% duty cycle / 50%占空比
    f_sw=100e3,     # 100kHz switching freq / 100kHz开关频率
    l=47e-6,        # 47µH inductor / 47µH电感
    c_out=100e-6,   # 100µF output cap / 100µF输出电容
    r_load=10.0     # 10Ω load / 10Ω负载
)

print(f"Vout = {buck.vout:.2f}V")          # 6.00V
print(f"Ripple = {buck.voltage_ripple*1000:.2f}mV")

t, v_out, i_l = buck.simulate(t_end=0.001)
plot_waveforms(t, v_out, i_l)
```

---

## License / 许可证
This project is distributed under the MIT License. See [LICENSE](LICENSE).

本项目采用 MIT 许可证，完整条款见 [LICENSE](LICENSE)。仓库保留原始版权声明；根据 MIT 许可证，你可以学习、修改和再发布本项目，但应保留许可证和版权声明。

## Command-line tool / 命令行工具

From the repository root:

```bash
python -m sim.cli --vin 12 --duty 0.5 --frequency 100000
```

Run the basic checks with:

```bash
python -m unittest discover -s tests
```

Compare several duty cycles automatically:

```bash
python -m sim.sweep
```

This is an ideal analytical model with estimated ripple, not a switch-level circuit simulation or hardware measurement.

Theory notes and assumptions are documented in [THEORY_NOTES.md](THEORY_NOTES.md).

The first LTspice switch-level netlist is [spice/buck_ideal.cir](spice/buck_ideal.cir). It is intentionally an idealized model for learning switching behavior, not a hardware-ready design.

The graphical schematic version is [spice/buck_ideal.asc](spice/buck_ideal.asc).

The comparison netlist with greatly reduced device losses is [spice/buck_lossless.cir](spice/buck_lossless.cir).

The first simulation procedure and observations are recorded in [SIMULATION_LOG.md](SIMULATION_LOG.md).

## Author / 作者
Isaac — Diploma in Electronic Engineering, TAR UMT

Built with ❤️ for learning power electronics
用 ❤️ 构建，用于学习电力电子技术
