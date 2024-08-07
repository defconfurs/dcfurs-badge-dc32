# DCFurs Badge Firmware

This directory contains board support and firmware for the 2024 DCFurs badge, to
be built using Micropython. The build instructions should roughly follow the RP2
port as follows:

### Clone Micropython

Clone the latest release of Micropython as follows:

```
git clone -b v1.23.0 https://github.com/micropython/micropython.git
```

You will probably also need to download the Arm GNU toolchain from [ARM](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads) and install it into
your PATH environment variable before proceeding.

### Build prerequisites

From the root of the micropython project, build the `mpy-cross` tool:

```
make -C mpy-cross
```

Then, from the `ports/rp2` directory in the micropython project build the
submodules:

```
make submodules
make clean
```

### Build the DCFurs Badge Firmware

From the `ports/rp2` directory in the micropython project, we can build the
badge firmware by specifying the path to the DCFurs board support directory:

```
make BOARD_DIR=~/path/to/dcfurs-dc32-badge/board/DCF2024_BADGE
```

Once the build has finished, you should be able to find the compiled firmware
in the `ports/rp2/build-DCF2024_BADGE` directory of the micropython project.

