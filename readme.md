# fixdir: fix directory naming
- Pass in the directory, the old name format, and the new name format
- Old format should be the current format of the filenames, with parts you want to capture replaced with `{}`
    - These are like unnamed capture groups in regex (zero-indexed)
- New format should be the new name of the file, with the order of the capture groups specified
- You can preview some of the names before they are changed unless you use `-f` (force).

Example: editing a folder full of TV episodes:
```
"The.Sopranos.S1E01.1080p.5.1Ch.BluRay.ReEnc-DeeJayAhmed.mkv"
"The.Sopranos.S1E02.1080p.5.1Ch.BluRay.ReEnc-DeeJayAhmed.mkv"
"The.Sopranos.S1E03.1080p.5.1Ch.BluRay.ReEnc-DeeJayAhmed.mkv"
...
```
Pass in these arguments:
```
dir = ./
old_format = "The.Sopranos.S{}E{}.1080p.5.1Ch.BluRay.ReEnc-DeeJayAhmed.mkv"
new_format = "The Sopranos: {0}.{1}.mkv"
```
Output:
```
"The Sopranos: 1.01.mkv"
"The Sopranos: 1.02.mkv"
"The Sopranos: 1.03.mkv"
...
```

# How to install
1. `chmod +x fixdir`
2. Add to PATH: put `export PATH=/path/to/script:$PATH` at the end of `.bashrc` or `.zshrc`
3. Restart terminal

# Tips
- It's regex based and not well-tested, so be specific with the formats and be careful with `-f`
- grep can probably do this so just use that instead :)