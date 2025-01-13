def log_time_to_wakatime():
    import subprocess
    import time
    while True:
        App.Console.PrintMessage("Logging time to WakaTime...\n")
        try:
            subprocess.call(['wakatime', '--write'])
            App.Console.PrintMessage("Time logged to WakaTime\n")
        except Exception as e:
            App.Console.PrintError(f"Error logging time to WakaTime: {e}\n")
        time.sleep(60)  # Log time every 60 seconds