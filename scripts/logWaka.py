


def log_time_to_wakatime():
    import subprocess
    import time
    import os
    import FreeCAD as App
    from Freecad import DocumentObserver
    import FreeCADGui as Gui
    import threading
    import inspect

    global document_modified
    document_modified = False

    class MyDocumentObserver(DocumentObserver):
        # _instance = None

        # def __new__(cls, *args, **kwargs):
        #     if not cls._instance:
        #         cls._instance = super(DocumentObserver, cls).__new__(cls, *args, **kwargs)
        #         cls._instance.__initialized = False
        #     return cls._instance

        # def __init__(self):
        #     if self.__initialized:
        #         return
        #     self.__initialized = True
        #     self.doc = App.ActiveDocument
        #     App.Console.PrintMessage("Document observer created\n")

        def slotDocumentModified(self, doc):
            global document_modified
            document_modified = True
            App.Console.PrintMessage("Document modified\n")
        
        def slotChangedDocument(self, doc):
            print("Document changed:", doc.Name)

        def slotChangedObject(self, obj):
            print("Object changed:", obj.Name)

    observer = MyDocumentObserver()
    App.addDocumentObserver(observer)
    App.Console.PrintMessage("Observer added\n")

    while True:
        last_logged_time = time.time()

        try:
            projectName = App.ActiveDocument.Name
        except Exception as e:
            App.Console.PrintError(f"Error getting project name: {e}\n")
            for _ in range(100):
                time.sleep(0.1)
                if document_modified:
                    break
            continue

        if projectName and projectName != 'NoneType':
            current_time = time.time()
                      
            if document_modified:
                App.Console.PrintMessage(f"Document has unsaved changes. Saving document: {projectName}\n")
                try:
                    App.ActiveDocument.save()
                    App.Console.PrintMessage("Document saved\n")
                    document_modified = False # reset
                except Exception as e:
                    App.Console.PrintError(f"Error saving document: {e}\n")
                
                App.Console.PrintMessage(f"Logging time to WakaTime...\n")
                try:
                    subprocess.call(['wakatime', '--plugin', 'FreeCAD', '--entity', projectName, '--project', projectName, '--plugin', 'Freecad' '--write'])
                    App.Console.PrintMessage("Time logged to WakaTime\n")
                    
                except Exception as e:
                    App.Console.PrintError(f"Error logging time to WakaTime: {e}\n")
                time.sleep(60)  # Log time every 60 seconds
            else:
                App.Console.PrintMessage("No changes in the document. Waiting...\n")
                time.sleep(10)
        else:
            App.Console.PrintMessage("No active document. Waiting...\n")
            time.sleep(10)  # Check after 10 seconds
            
def check_wakatime():
    import subprocess
    import os
    import FreeCAD as App
    import FreeCADGui as Gui
    import threading
    import inspect
    try:
        subprocess.call(['wakatime', '--version'])
    except Exception as e:
        App.Console.PrintError(f"Error checking wakatime: {e}\n")
        return False
    return True
