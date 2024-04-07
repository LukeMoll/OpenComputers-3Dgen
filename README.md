# OpenComputers-3Dgen
_Fetch Minecraft player's skins and convert them into in-game models printable with OpenComputers_.

This repository involves Minecraft and [3D printers](https://ocdoc.cil.li/block:3d_printer) from the OpenComputers mod. It has no relation to real-world 3D printers. It worked at the time of development (2018), but changes to Minecraft and the mod may mean that it no longer works.

After running `./init.sh` to set up the environment, run `./start.sh`. This will start a Flask application serving two Routes:

## `/face/<username>.3dm`
Returns the contents of `3dm` file for `<username>`'s current Mojang skin. This prints a flat object of the player's face.

## `/head/<username>/3dm`
As above, but prints a 3D cube of the player's head.
