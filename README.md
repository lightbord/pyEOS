# pyEOS
A Python library for controlling ETC EOS Family lighting consoles using OSC.

## Why pyEOS?
pyEOS was created for one simple reason. When developing software to interact with EOS, I wanted to leave as much of the OSC work out of it. I wanted something that could be as simple as `eos.go()`, `eos.stopback()` or `eos.macro(1)`. That simple. One line, one function. But that doesn't mean that's all it can do, or should do. Future features will include the ability to easily listen for events such as a specific cue, or sub bump, or macro, or anything else!

## Development of pyEOS
I am by no means a Python developer. In fact I'm only toe deep into the vast ocean that is Python. Therefore, I invite the community to not only add features, but fix things. Improve things.

## Requirements for code used in live production
Because this code has the potential to be used in live production (theatrical or otherwise), I feel it isn't unreasonable to make a few requests of anyone who will be contributing to the development of pyEOS. I hope these go without saying, but better to be sure.
* Your code must be tested against the current (as of when you submit your code) version of ETC's EOS Family software. If at all possible, test it with a console, and tell us which. If you don't have access to a console, you can download Nomad from ETC's website.
* Your code must not break any other features of pyEOS. If it looks like something you're working on will interfere with everything else and you're having trouble fixing it, hold off on releasing it until it doesn't break anything else, and the rest of the devlopment of pyEOS can move along. The last thing anyone would want is to update their version of pyEOS, and suddenly not be able to `eos.go()`.
* If you find a bug in ETC's OSC implementation, please report it to them, and avoid using that function in pyEOS until ETC has resolved that bug.

## Dependencies and licensing
Currently pyEOS relies on pyOSC (available at https://github.com/ptone/pyosc). This is how it talks to EOS. As such it is bound to the GPLv3, and as such is licensed that way.

More (including some code) coming in the next few days...
