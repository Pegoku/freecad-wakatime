import os
import FreeCAD as App
import FreeCADGui as Gui
import threading
import inspect

# def log_time_to_wakatimeOld():
#     import subprocess
#     import time
#     projectName = App.ActiveDocument.Name
#     while True:
#         App.Console.PrintMessage(f"Logging time to WakaTime. .. {projectName}\n")
#         try:
#             subprocess.call(['wakatime', '--write'])
#             App.Console.PrintMessage("Time logged to WakaTime\n")
#         except Exception as e:
#             App.Console.PrintError(f"Error logging time to WakaTime: {e}\n")
#         time.sleep(60)  # Log time every 60 seconds

class freecadWakatime(Workbench):
    MenuText = "Freecad Wakatime"
    ToolTip = "Configuration of Freecad Wakatime"
    Icon = os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), "resources", "Logo-32.png")
    
    App.Console.PrintMessage(
        "Log: Switching to freecadWakatime Workbench\n")

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
        self.is_active = False
        self.wakatime_thread = None
        
    def GetResources(self):
        return {
            'Pixmap': os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), "resources", "Logo-32.png"),
            'MenuText': 'Wakatime',
            'ToolTip': 'Activate/Desactivate Wakatime',
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
                self.wakatime_thread.join()
            self.is_active = False
            App.Console.PrintMessage("Wakatime desactivated\n")
        else:
            App.Console.PrintMessage("Activating Wakatime...\n")
            self.wakatime_thread = threading.Thread(target=log_time_to_wakatime)
            self.wakatime_thread.start()
            self.is_active = True  
            App.Console.PrintMessage("Wakatime Thread activated\n")
            

    def IsActive(self):
        return True

# class DesactivateWakatime:
#     def GetResources(self):
#         return {
#             'Pixmap': os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), "resources", "Logo-32.png"),
#             'MenuText': 'Wakatime',
#             'ToolTip': 'Desactivate Freecad Wakatime',
#         }
    

Gui.addWorkbench(freecadWakatime())
Gui.addCommand('ActivateWakatime', ActivateWakatime())
