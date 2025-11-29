# Pc-Control-Panel
A hackpad for Hack Club Blueprint. Has 6 shortcut keys, an OLED display, and a volume knob with leds to show volume.

# Cad
<img src=Assets/Cad.png alt="Cad" width="300"/>
The design includes 3 3D printed parts: A back piece that supports the PCB at a 45 degree angle, a front panel with cutouts, and a small spacer to support the OLED display. 
Modeled in Fusion.

# PCB
<img src=Assets/Schematic.png alt="Schematic" width="300"/>
<img src=Assets/PCB.png alt="PCB" width="300"/>
Notable features include:
<ul>
  <li>Larger traces for 5v and 3v3 power rails</li>
  <li>Large ground plane with minimal via usage</li>
</ul>
Made in KiCad.

# Firmware (WIP)
Hackpad uses KMK firmware. Currently, code uses switches to act as a small keyboard. More features (keyboard shortcuts, volume control, oled clock) are planned once board is available for testing.

# Bill of Materials
<ul>
  <li>1x PCB from PCBWay</li>
  <li>1x XIAO RP2040</li>
  <li>1x 0.91 in OLED</li>
  <li>1x EC11 Encoder</li>
  <li>6x MX-Style switches</li>
  <li>6x Blank DSA keycaps</li>
  <li>10x SK6812 MINI-E LEDs</li>
</ul>
All other parts (3d prints, screws) will be self-provided.


