"""
Easier68k-SampleProject

This is a test application as an example of using easier68k as an external python package.

Further examples will come later.
"""

import sys
import json
# install using pip install -r requirements.txt
# you may need to use the --upgrade flag
import easier68k
from easier68k.assembler.assembler import parse
from easier68k.core.enum.register import Register
from easier68k.core.models.list_file import ListFile
print('using easier68k version {}'.format(easier68k.__version__))

if __name__ == '__main__':
    # create a simulator object
    sim = easier68k.simulator.m68k.M68K()

    lf = ListFile()

    lf.read_s_record_filename(sys.argv[1])

    print()
    print('List file contents: ')
    print(lf.to_json())

    print('---- Starting execution ----')
    sim.load_list_file(lf)
    sim.clock_auto_cycle = True
    while not sim.halted:
        print(hex(sim.get_program_counter_value()))
        sim.step_instruction()


    print('---- Execution Done ----')

