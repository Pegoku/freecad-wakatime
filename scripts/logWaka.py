


def log_time_to_wakatime():
    import subprocess
    import time
    import os
    import FreeCAD as App
    import FreeCADGui as Gui
    import threading
    import inspect
    global freecad_wakatime_version
    freecad_wakatime_version = "0.1.0"
    global freecad_version
    freecad_version = ".".join(App.Version()[:3])
    
    global debug
    debug = App.ParamGet("User parameter:Plugins/Wakatime").GetBool("debug", False) 
    # global document_modified
    # document_modified = False
    global last_logged_time
    last_logged_time = time.time()
    global last_mod_time
    last_mod_time = time.time()
    global current_time
    current_time = time.time()
    
    projectName = ""
    class DocumentObserver:

        def slotChangedObject(self, obj, doc):
            global last_mod_time
            last_mod_time = time.time()
            if debug:
                App.Console.PrintMessage("Object changed\n")
                App.Console.PrintMessage(f"{last_mod_time}\n")
            # App.Console.PrintMessage(f"self: {self} obj: {obj} doc: {doc}\n")  
            # print("Object changed:", obj.Name)
            

    observer = DocumentObserver()
    App.addDocumentObserver(observer)
    App.Console.PrintMessage("Observer added\n")

    while True:
        # global last_logged_time
        # global document_modified
        
        projectNameTemp = ""

       
        while projectNameTemp == "" or projectNameTemp.startswith("Unnamed"):
            try:
                # projectName = App.ActiveDocument.Nam
                projectNameTemp = App.ActiveDocument.Label
            except Exception as e:
                App.Console.PrintError(f"Error getting project name: {e}\n")
                time.sleep(10)
                continue
            if projectNameTemp.startswith("Unnamed"):
                App.Console.PrintMessage("Project is not saved. Save to start.\n")
                time.sleep(10)
        
        if projectNameTemp != projectName:            
            App.Console.PrintMessage(f"Project name: {projectNameTemp}\n")
            projectName = projectNameTemp

        if projectName and projectName != 'NoneType':
            # global last_mod_time

            # global current_time
            current_time = time.time()

            if debug:
                App.Console.PrintMessage(f"{current_time} - {last_logged_time} = {current_time - last_logged_time}\n")
                App.Console.PrintMessage(f"{current_time} - {last_mod_time} = {current_time - last_mod_time}\n")
            if current_time - last_logged_time > 60 and current_time - last_mod_time < 60:
                # App.Console.PrintMessage(f"Document has unsaved changes. Saving document: {projectName}\n")
                # try:
                #     App.ActiveDocument.save()
                #     App.Console.PrintMessage("Document saved\n")
                # except Exception as e:
                #     App.Console.PrintError(f"Error saving document: {e}\n")
                
                App.Console.PrintMessage(f"Logging time to WakaTime as project: {projectName}... \n")
                
                try:
                    last_logged_time = time.time()
                    subprocess.call(['wakatime', '--plugin', f"freecad/{freecad_version} freecad-wakatime/{freecad_wakatime_version}", '--entity-type', 'app', '--entity', projectName, '--project', projectName, '--language', 'FreeCAD', '--write'])   
                    if debug:
                        App.Console.PrintMessage(['wakatime', '--plugin', f"freecad/{freecad_version} freecad-wakatime/{freecad_wakatime_version}", '--entity-type', 'app', '--entity', projectName, '--project', projectName, '--language', 'FreeCAD', '--write'])  
                    App.Console.PrintMessage("Time logged to WakaTime\n")
                    
                except Exception as e:
                    App.Console.PrintError(f"Error logging time to WakaTime: {e}\n")
                time.sleep(10)  # Log time every 60 seconds
            else:
                App.Console.PrintMessage("No changes in the document. Waiting...\n")
                time.sleep(10)
        else:
            App.Console.PrintMessage("No active document. Waiting...\n")
            time.sleep(10)  # Check after 10 seconds
            

def check_wakatime():
    import subprocess
    import FreeCAD as App
    try:
        subprocess.call(['wakatime', '--version'])
    except Exception as e:
        App.Console.PrintError(f"Error checking wakatime: {e}\n")
        return False
    return True
