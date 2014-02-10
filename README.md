watchpi
=======

Turning irrational numbers into images and videos.

Right now I've only got photos.

This is how you use:
python stills.py [optional_args]

Output will be in a jpg file saved to current directory.

Optional arguments:
* -size {x} -- create an x px by x px image (default 300)
* -style {s} -- s can be "hor", "ver", or "square"; defines the style of
translating number to pixels (default "hor"; check samples to see what I mean)
* -grain {g} -- g is a number that sets how grainy the created image should be
(default to 1, higher value -> grainier)
* -num {n} -- n is the number to create the image from; options are "pi", "e",
"tau", "phi", and "sq2" (defaults to pi).
