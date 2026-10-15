# Buck converter theory notes

## 1. Model scope

The current program uses an ideal continuous-conduction Buck approximation. It calculates steady-state values and estimated ripple. It does not solve MOSFET switching transitions, diode recovery, parasitic elements, control-loop dynamics, or hardware measurement.

## 2. Main relationships

For the ideal Buck converter:

```text
Vout = D × Vin
Iload = Vout / Rload
```

where `D` is duty cycle, `Vin` is input voltage, and `Rload` is load resistance.

The estimated inductor current ripple is:

```text
ΔIL = (Vin - Vout) × D / (fsw × L)
```

Using `Vout = D × Vin`, this becomes:

```text
ΔIL = Vin × D × (1 - D) / (fsw × L)
```

The estimated capacitor voltage ripple is:

```text
ΔVout = Iload × D / (fsw × C)
```

These are peak-to-peak-style engineering estimates under simplified assumptions.

## 3. Parameter trends

| Parameter change | Expected result |
|---|---|
| Increase `Vin` | Increase `Vout` and generally increase ripple |
| Increase `D` | Increase `Vout`; current ripple peaks near `D = 0.5` |
| Increase `fsw` | Reduce estimated voltage and current ripple |
| Increase `L` | Reduce estimated inductor current ripple |
| Increase `C` | Reduce estimated output voltage ripple |
| Increase `Rload` | Reduce load current and usually reduce capacitor ripple |

## 4. Example baseline

For `Vin = 12V`, `D = 0.5`, `fsw = 100kHz`, `L = 47µH`, `C = 100µF`, and `Rload = 10Ω`:

```text
Vout = 6.0V
Iload = 0.6A
estimated voltage ripple = 30mV
estimated inductor ripple = 638.3mA
```

These values are calculated results, not measurements.
