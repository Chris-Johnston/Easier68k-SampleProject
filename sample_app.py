"""
Easier68k-SampleProject

This is a test application as an example of using easier68k as an external python package.

Further examples will come later.
"""

# install using pip install -r requirements.txt
# you may need to use the --upgrade flag
import easier68k
from easier68k.core.enum.register import Register

print('using easier68k version {}'.format(easier68k.__version__))

if __name__ == '__main__':
    # create a simulator object
    sim = easier68k.simulator.m68k.M68K()

    # set register D1 value to 123
    sim.set_register_value(Register.D1, 123)

    assert sim.get_register_value(Register.D1) == 123

    print('done w/o errors')
