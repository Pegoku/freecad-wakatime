# freecad-wakatime
A simple freecad wakatime extension

## Installation

### Prerequisites
- wakatime-cli
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

Navigate to the `Mod` directory using the CLI and use Git to install freecad-wakatime:

```shell
git clone https://github.com/Pegoku/freecad-wakatime.git
```
