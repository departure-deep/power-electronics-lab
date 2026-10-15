# LTspice simulation log

## Experiment 1: ideal switch-level Buck

- Date: 2026-10-14
- Netlist: `spice/buck_ideal.cir`
- Tool: LTspice 26.x for Windows
- Input: 12 V DC
- Duty cycle: 50%
- Switching frequency: 100 kHz
- Inductor: 47 uH
- Output capacitor: 100 uF
- Load: 10 ohm
- Transient analysis: 0 to 2 ms, maximum step 10 ns

## Procedure

1. Open `spice/buck_ideal.cir` in LTspice. If the open dialog hides the file, change the filter from `Schematics (*.asc)` to `All files (*.*)`.
2. Run the simulation with the green Run button.
3. Add traces using `Plot Settings -> Add Trace`:
   - `V(out)` for output voltage
   - `V(sw)` for switch-node voltage
   - `I(L1)` for inductor current
4. Ignore the startup region and inspect approximately 1.5 to 2.0 ms.
5. Use two cursors on the same trace to compare a peak and the adjacent valley.

The netlist also contains automatic `.meas` statements for the steady-state interval. After running, open `View -> SPICE Error Log` (often `Ctrl+L`) to read `VOUT_RIPPLE` and `IL_RIPPLE`.

## Observations

- `V(out)` settles near 6 V after startup.
- `V(sw)` switches between approximately 0 V and 12 V.
- `I(L1)` is a triangular waveform with an average near 0.6 A.
- A cursor measurement between a current peak of 840.002 mA and a nearby valley of 271.651 mA gave a difference of -568.351 mA. The ripple magnitude for those two points is therefore 568.351 mA.
- The two current cursor points were not proven to be exact extrema, so repeat the measurement with cursors placed precisely on a peak and adjacent valley before treating it as the final value.
- A preliminary voltage-cursor difference was observed, but it was not taken from confirmed output-voltage extrema and is not recorded as the final voltage ripple.

## Automatic measurement result

The LTspice `.meas` output over 1.5 ms to 2 ms reported:

```text
VOUT_AVG    = 5.72722607045 V
VOUT_MAX    = 5.8123459816 V
VOUT_MIN    = 5.6426820755 V
VOUT_RIPPLE = 0.16966390697 V  (169.664 mV)

IL_AVG      = 0.564539876647 A
IL_MAX      = 1.02311944962 A
IL_MIN      = 0.0955323579627 A
IL_RIPPLE   = 0.927587091923 A (927.587 mA)
```

## Comparison with the analytical model

Python baseline estimates:

```text
Vout = 6.0 V
Iload = 0.6 A
Inductor ripple estimate = 638.3 mA
```

The first automatic comparison shows a substantial difference:

| Quantity | Python estimate | LTspice result |
|---|---:|---:|
| Average output voltage | 6.000 V | 5.727 V |
| Output voltage ripple | 30.0 mV | 169.664 mV |
| Average inductor current | 0.600 A | 0.565 A |
| Inductor current ripple | 638.3 mA | 927.587 mA |

This difference is a finding, not a failure to hide. Likely contributors include the simplified Python ripple equations, the switch and diode models, startup/operating-mode behavior, and the fact that the Python model does not solve the circuit differential equations. The next task is to diagnose these causes one at a time.

## Evidence boundary

This is a computer simulation, not a hardware measurement. Do not report the values as measured laboratory data or as proof of product-level performance.

## Experiment 2: manually drawn schematic (`Draft4.asc`)

- Date: 2026-10-15
- Schematic: `spice/Draft4.asc` (manually drawn in LTspice)
- Input: 12 V DC
- Duty cycle: 50%
- Switching frequency: 100 kHz
- Inductor: 47 uH
- Output capacitor: 100 uF
- Load: 10 ohm
- Switch model: `SWMOD`, with `Ron=0.05 ohm`, `Roff=1 Megohm`, `Vt=2 V`, `Vh=0.1 V`
- Diode model: LTspice built-in `1N914`
- Transient analysis: 0 to 2 ms, maximum step 10 ns
- Measurement interval: 1.5 ms to 2 ms

### Automatic measurement result

```text
VOUT_AVG    = 5.4160400068 V
VOUT_MAX    = 5.4240489006 V
VOUT_MIN    = 5.40924119949 V
VOUT_RIPPLE = 0.014807701108 V (14.8 mV)

IL_AVG      = 0.541985108985 A
IL_MAX      = 0.903500258923 A
IL_MIN      = 0.189547419548 A
IL_RIPPLE   = 0.713952839375 A (714.0 mA)
```

### Interpretation

- The average output current is approximately `5.416 V / 10 ohm = 0.542 A`, consistent with `IL_AVG`.
- `IL_MIN` remains above zero, so the converter is operating in continuous conduction mode during the measurement interval.
- The output is below the ideal `D*Vin = 6 V` estimate because the simulation includes the forward drop of the `1N914` diode and switch resistance.
- These values are schematic-simulation results, not hardware measurements.
