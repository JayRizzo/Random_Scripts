ANSWER FOR: https://stackoverflow.com/q/4833052/1896134
<!-- language-all: lang-sh -->


<hr>

# Answer (Individual Files)

<hr>

### 1. Showcase keys to use in selection.

    xattr ~/Desktop/screenshot\ 2019-10-23\ at\ 010212.png
        # com.apple.FinderInfo
        # com.apple.lastuseddate#PS
        # com.apple.metadata:kMDItemIsScreenCapture
        # com.apple.metadata:kMDItemScreenCaptureGlobalRect
        # com.apple.metadata:kMDItemScreenCaptureType

### 2. Pick a Key to delete.
    xattr -d com.apple.lastuseddate#PS ~/Desktop/screenshot\ 2019-10-23\ at\ 010212.png
    xattr -d kMDItemIsScreenCapture ~/Desktop/screenshot\ 2019-10-23\ at\ 010212.png

### 3. Showcase keys again to see they have been removed.
    xattr -l ~/Desktop/screenshot\ 2019-10-23\ at\ 010212.png
        # com.apple.FinderInfo
        # com.apple.metadata:kMDItemScreenCaptureGlobalRect
        # com.apple.metadata:kMDItemScreenCaptureType

### 4. Lastly, REMOVE ALL keys for a particular file
    xattr -c ~/Desktop/screenshot\ 2019-10-23\ at\ 010212.png

<hr>

# Answer (All Files In A Directory)

<hr>

### 1. Showcase keys to use in selection.


    xattr -r ~/Desktop

### 2. Remove a Specific Key for EVERY FILE in a directory

    xattr -rd com.apple.FinderInfo ~/Desktop


### 3. Remove ALL keys on EVERY FILE in a directory

    xattr -rc ~/Desktop

> **WARN: Once you delete these you DON'T get them back!**
> ***FAULT ERROR: There is NO UNDO.***


<hr>

# Errors

<hr>

I wanted to address the error's people are getting.
**Because the errors drove me nuts too...**
On a mac if you install `xattr` in python, then your environment may have an issue.

> There are two different paths on my mac for `xattr`

    type -a xattr

        # xattr is /usr/local/bin/xattr    # PYTHON Installed Version
        # xattr is /usr/bin/xattr          # Mac OSX Installed Version

So in one of the example's where `-c` will not work in xargs is because in bash you default to the non-python version.

### Works with `-c`
    /usr/bin/xattr -c

### Does NOT Work with `-c`
    /usr/local/bin/xattr -c
        # option -c not recognized

My Shell/Terminal defaults to  /usr/local/bin/xattr because my `$PATH`
`/usr/local/bin:` is before `/usr/bin:` which I believe is the default.

I can prove this because, if you try to uninstall the python `xattr` you will see:

    pip3 uninstall xattr
    Uninstalling xattr-0.9.6:
      Would remove:
        /usr/local/bin/xattr
        /usr/local/lib/python3.7/site-packages/xattr-0.9.6.dist-info/*
        /usr/local/lib/python3.7/site-packages/xattr/*
    Proceed (y/n)?

<hr>

# Workarounds

<hr>

To Fix `option -c not recognized` Errors.

1. Uninstall any Python `xattr` you may have: `pip3 uninstall xattr`
1. Close all `Terminal` windows & quit `Terminal`
1. Reopen a new `Terminal` window.
1. ReRun `xattr` command and it should now work.

OR

> If you want to keep the Python `xattr` then use

    /usr/bin/xattr

for any `Shell` commands in `Terminal`

<hr>

### Example:

<hr>

Python's version of `xattr` doesn't handle images at all:

    Good-Mac:~ JayRizzo$ xattr ~/Desktop/screenshot\ 2019-10-23\ at\ 010212.png
        # com.apple.FinderInfo
        # Traceback (most recent call last):
        #   File "/usr/local/bin/xattr", line 8, in <module>
        #     sys.exit(main())
        #   File "/usr/local/lib/python3.7/site-packages/xattr/tool.py", line 196, in main
        #     attr_value = attr_value.decode('utf-8')
        # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb0 in position 2: invalid start byte

    Good-Mac:~ JayRizzo$ /usr/bin/xattr ~/Desktop/screenshot\ 2019-10-23\ at\ 010212.png
        # com.apple.FinderInfo
        # com.apple.lastuseddate#PS
        # com.apple.metadata:kMDItemIsScreenCapture
        # com.apple.metadata:kMDItemScreenCaptureGlobalRect
        # com.apple.metadata:kMDItemScreenCaptureType

## Man Pages

[MAN PAGE for OSX xattr][1]

[MAN PAGE for Python xattr VERSION 0.6.4][2]

> NOTE: I **could not** find the python help page for current VERSION 0.9.6


Thanks for Reading!

  [1]: https://ss64.com/osx/xattr.html
  [2]: http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/VisualWorks/CSV2HTML/CSV2HTML_PyDoc/xattr.html#xattr
