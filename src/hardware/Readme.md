# Hardware

Here to connect to Arduino Uno Board with the firmware `firmata`, with this to communicate to a database to insert the data 

## Architecture

![arq](assets/arq_hardware.excalidraw.png)

## Schematic

![schematic](./assets/board_connection_bb.png)

## Firmware

Install in your board the firmware `firmataStandard` in the Arduino IDE. 
Or you can download from here with [bootloader](./assets/firmware/StandardFirmata.ino.with_bootloader.hex) or [without bootloader](./assets/firmware/StandardFirmata.ino.hex)

## Module python

The module used is `pyFirmata2`

install with `pip install pyfirmata2`

`https://github.com/berndporr/pyFirmata2/tree/master`
