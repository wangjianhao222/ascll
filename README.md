# ascll
just a simple ascll commandtool
Advanced ASCII Animator in Python
This Python script, ascll.py, is a command-line tool for creating and displaying animated ASCII art. It's built with several advanced features, including special visual effects and color support, allowing for dynamic and engaging text-based animations.

Key Features:
Load ASCII Art from a File: The script can read a series of ASCII art frames from a text file, with each frame separated by a double newline (\n\n).

Built-in Animation Effects: It includes three distinct visual effects that can be applied to your ASCII art:

Vortex: This effect rotates the ASCII art around a central point, creating a swirling, vortex-like motion. It dynamically changes colors as the animation progresses.

Particle: This effect generates and animates small, colored particles that move across the screen, creating a dynamic visual layer over the ASCII art.

Matrix: Although a matrix effect is mentioned in the code's configuration, the script only fully implements the vortex and particle effects. This suggests the matrix effect is a planned but not yet functional feature.

Customizable Settings: You can easily adjust the frame delay to control the animation's speed and choose a specific effect directly from the command line.

Command-Line Interface: The script uses the argparse library to provide a user-friendly command-line interface. You can specify an input file for the frames and select the desired animation effect and speed.

How to Use:
To run the script, open your terminal and use the following syntax:

Bash

python ascll.py [options]
Options:

-f, --file: Specify the path to a text file containing your ASCII art frames.

-e, --effect: Choose the animation effect. The available options are vortex and particle.

-d, --delay: Set the delay between frames in seconds. The default value is 0.05.

Example:

To run an animation using frames from a file named frames.txt with the vortex effect and a slower delay:

Bash

python ascll.py --file frames.txt --effect vortex --delay 0.1






