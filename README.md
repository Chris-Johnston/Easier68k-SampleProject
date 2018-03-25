# Easier68k-SampleProject

Example output can be seen on the build status page: [![Build Status](https://travis-ci.org/Chris-Johnston/Easier68k-SampleProject.svg?branch=master)](https://travis-ci.org/Chris-Johnston/Easier68k-SampleProject)

A sample project demonstrating the use of [Easier68k][easier68k].

## Build & Execution Steps:

(Confirmed to work with python versions >=3.5)

```bash
# install the requirements of the run scripts (contains git+https://github.com/Chris-Johnston/Easier68k)
python -m pip install -r requirements.txt

# assemble and run the program from a .x68 file
python sample_app.py helloworld.x68

# run the program from a pre-assembled .S68 file
python run_s68k.py helloworld.S68
```

[easier68k]: https://github.com/Chris-Johnston/Easier68k
