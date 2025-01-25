import os
import FreeCAD as App
import FreeCADGui as Gui
import threading
import inspect

class freecadWakatime(Workbench):
    MenuText = "Freecad Wakatime"
    ToolTip = "Configuration of Freecad Wakatime"
    Icon = os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), "resources", "Logo.svg")
    

    def Initialize(self):
        self.appendToolbar("Wakatime", ["ActivateWakatime"])

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    # def Activated(self):
    #     console_message = "Log: Workbench freecadWakatime activated\n"
    #     App.Console.PrintMessage(console_message)

    # def Deactivated(self):
    #     if self.wakatime_thread.is_alive():
    #         self.wakatime_thread.join()

    def ContextMenu(self, recipient):
        return

    def GetClassName(self):
        return "Gui::PythonWorkbench"

class ActivateWakatime:
    def __init__(self):
        import threading
        from scripts.logWaka import log_time_to_wakatime
        import os
        import subprocess
        os_name = os.name
        platform = os.sys.platform
        wakatime_cli_dir = os.path.join(os.path.expanduser("~"), "wakatime-cli")
        
        if os_name == 'nt':
                if not os.path.exists(wakatime_cli_dir+"\\wakatime-cli.exe"):                
                    import urllib.request
                    import zipfile
                    # Download and install wakatime-cli
                    wakatime_cli_url = "https://github.com/wakatime/wakatime-cli/releases/latest/download/wakatime-cli-windows-amd64.zip"
                    wakatime_cli_zip = os.path.join(os.path.expanduser("~"), "wakatime-cli.zip")
                    

                    # Download the wakatime-cli zip file
                    urllib.request.urlretrieve(wakatime_cli_url, wakatime_cli_zip)

                    # Extract the zip file
                    with zipfile.ZipFile(wakatime_cli_zip, 'r') as zip_ref:
                        zip_ref.extractall(wakatime_cli_dir)
                    
                    # Rename the extracted file to wakatime-cli.exe
                    for file_name in os.listdir(wakatime_cli_dir):
                        if file_name.startswith("wakatime-cli") and file_name.endswith(".exe"):
                            os.rename(os.path.join(wakatime_cli_dir, file_name), os.path.join(wakatime_cli_dir, "wakatime-cli.exe"))
                            break

                    # Clean up the zip file
                    os.remove(wakatime_cli_zip)


                # # Add wakatime-cli to PATH (windows)
                # print(os.pathsep + wakatime_cli_dir)
                # os.environ["PATH"] += os.pathsep + wakatime_cli_dir
        
        self.is_active = self.get_persistent_value("is_active", False)
        # self.is_active = False
        self.wakatime_thread = None
        if self.is_active:
            self.wakatime_thread = threading.Thread(target=log_time_to_wakatime)
            self.wakatime_thread.start()
            self.is_active = True  
            self.set_persistent_value("is_active", self.is_active)
            
            App.Console.PrintMessage("Log: Freecad-Wakatime active\n")
            
            
        else:
            App.Console.PrintMessage("Log: Freecad-Wakatime inactive\n")
    def GetResources(self):
        global pixmap
        # if self.is_active:
        #     pixmap = os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), "resources", "Logo-32-on.png")
        # else:
        #     pixmap = os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), "resources", "Logo-32-off.png")
        
        return {
            'Pixmap': os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), "resources", "Logo.svg"),
            'MenuText': 'Wakatime',
            'ToolTip': 'Activate/Deactivate Wakatime',
        }

    def Activated(self):
        import threading
        from scripts.logWaka import log_time_to_wakatime, check_wakatime
        if not check_wakatime():
            App.Console.PrintError("Wakatime is not installed. Please install it and try again\n")
            return
        
        if self.is_active:
            App.Console.PrintMessage("Desactivating Wakatime...\n")
            if self.wakatime_thread and self.wakatime_thread.is_alive():
                self.wakatime_thread.join(1)
            self.is_active = False
            self.set_persistent_value("is_active", self.is_active)
            App.Console.PrintMessage("Wakatime deactivated\n")
            # Gui.updateGui()
        else:
            App.Console.PrintMessage("Activating Wakatime...\n")
            self.wakatime_thread = threading.Thread(target=log_time_to_wakatime)
            self.wakatime_thread.start()
            self.is_active = True  
            self.set_persistent_value("is_active", self.is_active)
            App.Console.PrintMessage("Wakatime Thread activated\n")
        
        # Gui.addCommand('ActivateWakatime', self)
            
    def IsActive(self):
        return True

    def get_persistent_value(self, key, default):
        return App.ParamGet("User parameter:Plugins/Wakatime").GetBool(key, default)

    def set_persistent_value(self, key, value):
        App.ParamGet("User parameter:Plugins/Wakatime").SetBool(key, value)

    

Gui.addWorkbench(freecadWakatime())
Gui.addCommand('ActivateWakatime', ActivateWakatime())
