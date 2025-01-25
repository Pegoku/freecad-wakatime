# freecad-wakatime
A simple freecad wakatime extension

## Installation

### Prerequisites
- wakatime-cli (Linux and macOS only)
- wakatime configured 


<!-- ### Automatic Installation (WIP)
In the future this plugin may be in the Freecad-addons repo
The recommended way to install freecad-wakatime is via FreeCAD's [Addon Manager](https://wiki.freecad.org/Std_AddonMgr) under `Tools > Addon Manager` dropdown menu.

Search for **freecad-wakatime** in the workbench category. -->

### Manual Installation

The install path for FreeCAD modules depends on the operating system used.

To find the user's application data directory, enter the following command in FreeCAD's Python console:

```python
App.getUserAppDataDir()
```

Examples for different operating systems:

- **Linux:** `/home/<user>/.local/share/FreeCAD/Mod/`
- **macOS:** `/Users/<user>/Library/Preferences/FreeCAD/Mod/`
- **Windows:** `C:\Users\<user>\AppData\Roaming\FreeCAD\Mod\`

Navigate to the `Mod` directory (create it if it doesn't exist) using the CLI and use Git to install freecad-wakatime:

```shell
git clone https://github.com/Pegoku/freecad-wakatime.git
```

### Manual Update

Navigate to the `Mod/freecad-wakatime` directory using the CLI and use Git to update the extension:

```shell
git pull
```
