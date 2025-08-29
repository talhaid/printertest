@echo off
echo ========================================
echo Zebra Printer GUI - Test Launcher
echo ========================================
echo.
echo Starting the Zebra Printer GUI...
echo.

cd /d "%~dp0"
if exist "ZebraPrinterGUI.exe" (
    echo ✅ Found ZebraPrinterGUI.exe
    echo 🚀 Launching application...
    start "" "ZebraPrinterGUI.exe"
    echo.
    echo ✅ Application started!
    echo You can close this window now.
) else (
    echo ❌ Error: ZebraPrinterGUI.exe not found!
    echo Make sure this batch file is in the same folder as ZebraPrinterGUI.exe
)

echo.
pause
