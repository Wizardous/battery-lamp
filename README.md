# Battery Lamp

A Python project to add a battery status icon to the system tray on your Windows device.

**Preview**  
![](assets/images/screenshot/battery_lamp_pinned_not_charging_71.png)

## Motivation

'Battery Lamp' was created out of the need to have an effortless and clear view of my device’s exact battery percentage directly on the taskbar. Windows doesn't provide this information without an extra click and only shows a vague icon. By having 'Battery Lamp' update the battery status in real-time, it ensures that I know precisely when to plug in my charger and avoid the stress of surprise low battery notifications.

## How to Use Battery Lamp

**Requirements:** 
- Operating System: **Windows 10 or 11**.
- [Python 3](https://www.python.org/downloads/windows/) installed on the system.

*It is recommended to install Python with version 3.9 or higher. Python 3.8 and older version have reached their end of life.*

**Execution Steps:**


1. Clone the project or download `battery_percentage.pyw` from the src directory.

2. Install the dependencies mentioned in the `requirements.txt` file.

3. (Optional but recommended) **Set up Battery Lamp to run automatically at startup:**
   - Use the provided automation script: Run `setup-startup.py` from the `utils` directory. This script will add Battery Lamp to your Windows startup folder, so it launches automatically when you log in.
   - The script uses the `setup_config.json` file to determine the configuration, such as the path to your Python executable and the script location. You can edit `setup_config.json` to customize these settings before running the script.
   - To run the script, open a terminal in the project directory and execute:
     ```powershell
     python utils/setup-startup.py
     ```
   - If you wish to remove Battery Lamp from startup, you can run the script again and follow the prompts.

4. If you do **not** wish to use the automation script, you can manually add Battery Lamp to Windows startup:
   - Press `Win + R`, type `shell:startup`, and press Enter. This opens your Startup folder.
   - Create a shortcut in this folder that points to your Pythonw executable and the `battery_percentage.pyw` script. For example:
     - Target: `C:\Path\To\pythonw.exe C:\Path\To\battery_percentage.pyw`
   - Make sure the shortcut uses `pythonw.exe` (not `python.exe`) to avoid opening a console window.
   - Optionally, set an icon for the shortcut using the provided icon in `assets/images/icon/battery_lamp_icon.ico`.

5. To run Battery Lamp immediately (without rebooting), execute the script using a Command Prompt or PowerShell instance with the command:

   ```powershell
   pythonw src/battery_percentage.pyw
   ```

   This step is useful if you want to test or use Battery Lamp right away, without waiting for your next Windows restart or login. Running this command will immediately launch the tray icon and start showing your battery percentage, so you can confirm everything is working as expected. The program will run in the background, and you can close the terminal window after running the command.

> [!NOTE]  
> The 'w' in `pythonw` is crucial as it ensures the script runs without keeping the console busy. In other words, you can continue using the terminal after you ran the above command or close it, the lamp will run in the background.

**Result:**

If all the above steps are completed correctly, a new icon will appear in the system tray displaying the battery percentage.

> [!TIP]  
> You might need to pin the icon to the taskbar by dragging it out from the hidden icons list in the system tray panel.  
> <img src="assets/images/screenshot/drag_out_to_pin.gif" width=250>

**Closing the Program:**

Right-clicking on the icon will display a context menu with an "Exit" option. Clicking "Exit" will close the program.

## Preview

Here are different ways the Battery Lamp will glow under different battery status conditions.

|              |Not Charging|Charging|
|--------------|------------|--------|
|Charge at 100%|![](/assets/images/preview/100_not_charging_64x64.png)|![](/assets/images/preview/100_charging_64x64.png)|
|Charge at 71% |![](/assets/images/preview/71_not_charging_64x64.png)|![](/assets/images/preview/71_charging_64x64.png)|
|Charge at 15%^|![](/assets/images/preview/15_not_charging_64x64.png)|![](/assets/images/preview/15_charging_64x64.png)|

> *^ Below critical charge threshold of 20%, later versions should provide an option to change this threshold.*

## Roadmap

Here are some exciting features being considered for future versions, ordered by complexity of implementation:

1. Ability to set custom critical battery threshold.
2. Customizable update frequency for battery status checks.
3. More themes.
4. Themes customiser and preview UI.
5. More options in the context menu.
6. Quick access settings from the system tray.
7. Detailed battery health statistics report exports.
8. Graphical dashboard for detailed statistics.
9. Actions server.
