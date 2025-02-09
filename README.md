# Freecad-wakatime
A simple freecad wakatime extension

## What is WakaTime?
WakaTime is an open-source time tracking tool. It provides insights into how much time you spend on different projects, languages, and files.

## What is freecad-wakatime?
The `freecad-wakatime` extension integrates WakaTime with FreeCAD, allowing you to track the time you spend working on your FreeCAD projects. This extension logs your activity and sends it to your WakaTime account, where you can view detailed reports and analytics.

## Installation

### Prerequisites
- WakaTime (wakatime.cfg) configured with your API key 


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

## Usage
Once installed, the freecad-wakatime workbench will be available, and you'll be able to enable or disable the tracking of time you spend working on your FreeCAD projects. You can view your coding activity on the WakaTime dashboard.

![image](image.png)

## License
This project is licensed under the LGPL-2.1 license. See the [LICENSE](https://github.com/Pegoku/freecad-wakatime/blob/main/LICENSE) file for more details.

