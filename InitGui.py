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
            App.Console.PrintLog("Deactivating Wakatime...\n")
            if self.wakatime_thread and self.wakatime_thread.is_alive():
                self.wakatime_thread.join(1)
            self.is_active = False
            self.set_persistent_value("is_active", self.is_active)
            App.Console.PrintLog("Wakatime deactivated\n")
            # Gui.updateGui()
        else:
            App.Console.PrintLog("Activating Wakatime...\n")
            self.wakatime_thread = threading.Thread(target=log_time_to_wakatime)
            self.wakatime_thread.start()
            self.is_active = True  
            self.set_persistent_value("is_active", self.is_active)
            App.Console.PrintLog("Wakatime Thread activated\n")
        
        # Gui.addCommand('ActivateWakatime', self)
            
    def IsActive(self):
        return True

    def get_persistent_value(self, key, default):
        return App.ParamGet("User parameter:Plugins/Wakatime").GetBool(key, default)

    def set_persistent_value(self, key, value):
        App.ParamGet("User parameter:Plugins/Wakatime").SetBool(key, value)

    

Gui.addWorkbench(freecadWakatime())
Gui.addCommand('ActivateWakatime', ActivateWakatime())
