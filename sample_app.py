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

print('using easier68k version {}'.format(easier68k.__version__))

if __name__ == '__main__':
    # create a simulator object
    sim = easier68k.simulator.m68k.M68K()

    with open(sys.argv[1]) as asm_file:
        listfile, issues = parse(asm_file.read(-1))

        if issues:
            print('---- ISSUES ----')
            for i in issues:
                print('{}: {}'.format(issues[0], issues[1]))


        print()
        print('List file contents: ')
        pretty_json = json.loads(listfile.to_json())
        print(json.dumps(pretty_json, indent=4, sort_keys=True))

        print('---- Starting execution ----')
        sim.load_list_file(listfile)
        sim.clock_auto_cycle = True
        sim.run()
