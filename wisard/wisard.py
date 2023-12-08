import os
import time
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    target = os.path.join(os.getenv("LOCALAPPDATA"), "leadaw") 
    input(f"Press enter to start download to {target}")
    if not os.path.exists(target):
        os.mkdir(target)
    else:
        import glob
        files = glob.glob(target)
        for f in files:
            os.remove(f)

    os.system("curl https://github.com/leadattic/leadaw/archive/refs/heads/release.zip --output "+ os.path.join(target, "download.zip"))

    time.sleep(1)
    input()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

