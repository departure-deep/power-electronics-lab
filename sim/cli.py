"""Command-line entry point for the ideal Buck model."""

import argparse
from .buck_converter import BuckConverter


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run an ideal Buck converter calculation.")
    parser.add_argument("--vin", type=float, default=12.0)
    parser.add_argument("--duty", type=float, default=0.5)
    parser.add_argument("--frequency", type=float, default=100_000.0)
    parser.add_argument("--inductance", type=float, default=47e-6)
    parser.add_argument("--capacitance", type=float, default=100e-6)
    parser.add_argument("--load", type=float, default=10.0)
    args = parser.parse_args(argv)
    buck = BuckConverter(args.vin, args.duty, args.frequency,
                         args.inductance, args.capacitance, args.load)
    print(buck)
    print(f"Output voltage: {buck.vout:.3f} V")
    print(f"Load current: {buck.i_load:.3f} A")
    print(f"Estimated voltage ripple: {buck.voltage_ripple * 1000:.3f} mV")
    print(f"Estimated inductor ripple: {buck.current_ripple * 1000:.3f} mA")


if __name__ == "__main__":
    main()
