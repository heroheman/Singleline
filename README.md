Singleline package for Sublime Text 2
=====================================

SingleLine is a CSS Single to Multiline Style Switch plugin for Sublime Text 2.

It will convert between multi-line rules:

    body {
        height: 600px;
        width: 600px;
        margin: auto;
        border: 1px solid #000;
    }

to

    body { height: 600px; width: 600px; margin: auto; border: 1px solid #000; }

--
It also works in less / scss with nested selectors:

    .upperclass{
       .middleclass{
            .testclass{
                margin: 20px;
                padding: 10px;
                background: #f00;
            }
        }
    }

to

    .upperclass{
       .middleclass{
            .testclass{ margin: 20px; padding: 10px; background: #f00; }
        }
    }

Keyboard Shortcuts
------------------
To toggle between single-line and multiline format you can either select the block or move the cursor inside the block and press `ctrl+alt+j`.

You can also expand selection to css rule with `ctrl+shift+r`.

Installing
----------
<!-- **With the Package Control plugin:** The easiest way to install this package is through Package Control, which can be found at this site: [http://wbond.net/sublime_packages/package_control](http://wbond.net/sublime_packages/package_control)

Once you install Package Control, restart ST2 and bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select `LESS` when the list appears. -->

**Without Git:** Download the latest source zip from [github](https://github.com/heroheman/Singleline/zipball/master) and extract the files to your Sublime Text "Packages" directory, into a new directory named `Singleline`.

**With Git:** Clone the repository in your Sublime Text "Packages" directory:

    git clone git://github.com/heroheman/Singleline.git

The "Packages" directory is located at:

* OS X:
    `~/Library/Application Support/Sublime Text 2/Packages/`
* Linux:
    `~/.Sublime Text 2/Packages/`
* Windows:
    `%APPDATA%/Sublime Text 2/Packages/`


That's it!