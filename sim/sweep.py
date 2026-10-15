"""Sweep Buck duty cycle and print a comparison table."""

from .buck_converter import BuckConverter


def run_sweep(vin=12.0, duties=(0.25, 0.5, 0.75), r_load=10.0):
    print("Duty    Vout (V)    Iload (A)    V ripple (mV)    I ripple (mA)")
    print("-----   --------   ----------   --------------   -------------")
    for duty in duties:
        buck = BuckConverter(vin, duty, 100e3, 47e-6, 100e-6, r_load)
        print(f"{duty:>4.2f}    {buck.vout:>7.3f}    {buck.i_load:>8.3f}"
              f"    {buck.voltage_ripple * 1000:>12.3f}"
              f"    {buck.current_ripple * 1000:>11.3f}")


if __name__ == "__main__":
    run_sweep()
