# Power Electronics Lab 🔋

Simulation and analysis of DC-DC converters (buck, boost, buck-boost) with waveform visualization.

## Features
- Buck converter simulation
- Boost converter simulation
- Buck-boost converter simulation
- Component selection calculator
- Efficiency analysis
- Waveform visualization (V, I, ripple)
- Thermal model estimation
- Interactive parameter tuning (web UI)

## Converter Models
```
Buck:      Vin ──[S]──[L]──[C]── Vout
                └──[D]──┘

Boost:     Vin ──[L]──[S]── Vout
                   └──[D]──[C]──

Buck-Boost: Vin ──[S]──[L]── Vout
                 └──[D]──[C]──
```

## Tech Stack
- **Simulation**: C++17 (numerical integration - RK4)
- **Frontend**: HTML5 Canvas for waveform plotting
- **Build**: CMake

## Skills Demonstrated
- Power electronics (converter topologies, duty cycle)
- Numerical simulation (Runge-Kutta, differential equations)
- Circuit analysis (inductor volt-second balance)
- C++ numerical computing

Built by Isaac © 2026
