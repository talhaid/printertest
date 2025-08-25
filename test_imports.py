#!/usr/bin/env python3
"""Test script to check available modules"""

print("Testing module imports...")

# Test win32print
try:
    import win32print
    import win32api
    print("✅ win32print: Available")
    # List printers
    printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)
    print(f"   Found {len(printers)} printers:")
    for printer in printers:
        print(f"     - {printer[2]}")
except Exception as e:
    print(f"❌ win32print: Failed - {e}")

# Test PIL/Pillow
try:
    from PIL import Image
    print("✅ PIL/Pillow: Available")
except Exception as e:
    print(f"❌ PIL/Pillow: Failed - {e}")

# Test PyMuPDF
try:
    import fitz
    print("✅ PyMuPDF (fitz): Available")
    print(f"   Version: {fitz.version}")
except Exception as e:
    print(f"❌ PyMuPDF (fitz): Failed - {e}")

# Try alternative import
try:
    import pymupdf
    print("✅ PyMuPDF (pymupdf): Available")
except Exception as e:
    print(f"❌ PyMuPDF (pymupdf): Failed - {e}")

print("\nModule test complete!")