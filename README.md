# Zebra GC420T PDF Printer for Python

A Python application for printing PDF files to your Zebra GC420T thermal printer.

## Features

- 🖨️ Print PDF files directly to Zebra GC420T
- 📄 Convert PDF pages to thermal printer-compatible images
- 🔧 Automatic printer detection
- 📋 Support for multiple copies
- 🎯 Optimized for 203 DPI thermal printing
- 💾 Raw ZPL command support
- 🖥️ Windows printer integration

## Requirements

- Windows OS (tested on Windows 10/11)
- Python 3.7+
- Zebra GC420T printer connected via USB or network
- Zebra printer drivers installed

## Installation

1. **Clone or download this project**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start

### 1. Basic Usage (Command Line)

```bash
# Print a PDF file
python zebra_printer.py your_document.pdf

# Print multiple copies
python zebra_printer.py your_document.pdf --copies 3

# List available printers
python zebra_printer.py --list-printers

# Specify printer manually
python zebra_printer.py your_document.pdf --printer "Zebra GC420T"
```

### 2. Using the Python Module

```python
from zebra_printer import ZebraPrinter

# Initialize printer (auto-detects Zebra)
printer = ZebraPrinter()

# Or specify printer name
printer = ZebraPrinter("Zebra GC420T (ZPL)")

# Print a PDF
success = printer.print_pdf("label.pdf", copies=2)

# Check printer status
status = printer.get_printer_status()
print(status)
```

### 3. Run Examples

```bash
# Run all demos
python example.py

# Print specific PDF
python example.py my_label.pdf

# Print multiple copies
python example.py my_label.pdf --copies 5
```

## Printer Setup

1. **Connect your Zebra GC420T:**
   - USB: Connect via USB cable
   - Network: Configure IP settings

2. **Install Zebra drivers:**
   - Download from [zebra.com](https://www.zebra.com/us/en/support-downloads.html)
   - Install the GC420T drivers for Windows

3. **Verify printer in Windows:**
   - Go to Settings > Printers & Scanners
   - Ensure your Zebra printer appears in the list
   - Print a test page to confirm connectivity

## Supported Features

### PDF Processing
- ✅ Multi-page PDF support
- ✅ Automatic image conversion
- ✅ DPI optimization (203 DPI for GC420T)
- ✅ Monochrome conversion for thermal printing

### Printer Communication
- ✅ Windows printer spooler integration
- ✅ Raw data printing
- ✅ ZPL command support
- ✅ Error handling and logging

### Print Settings
- ✅ Copy count control
- ✅ Resolution settings
- ✅ Image resizing for printer width
- ✅ Automatic paper size detection

## Troubleshooting

### Common Issues

1. **"No Zebra printer found"**
   - Check printer is connected and powered on
   - Verify drivers are installed
   - Run `python zebra_printer.py --list-printers` to see available printers

2. **"Print job failed"**
   - Ensure printer has paper loaded
   - Check for paper jams
   - Verify printer is online in Windows

3. **"win32print not available"**
   - Install pywin32: `pip install pywin32`
   - This is required for Windows printer communication

4. **Poor print quality**
   - Verify you're using thermal transfer or direct thermal labels
   - Check print density settings on the printer
   - Ensure PDF resolution matches printer (203 DPI)

### Printer Configuration

- **Media Type:** Direct thermal or thermal transfer labels
- **Print Method:** Thermal transfer (for durability) or direct thermal
- **Print Width:** Up to 4.09" (104mm)
- **Resolution:** 203 dpi (8 dots/mm)
- **Print Speed:** 2-5 ips (50-127 mm/sec)

## Label Design Tips

1. **Size:** Design labels to match your media (common: 4"x6", 4"x3", 2"x1")
2. **Resolution:** Use 203 DPI for crisp text and graphics
3. **Colors:** Use black and white only (thermal printers don't support color)
4. **Fonts:** Use clear, readable fonts (Arial, Helvetica work well)
5. **Margins:** Leave 0.1" margins for reliable printing

## Advanced Usage

### Custom ZPL Commands

```python
printer = ZebraPrinter()

# Send raw ZPL commands
zpl = """
^XA
^FO50,50^ADN,36,20^FDHello World^FS
^XZ
"""
printer.send_raw_zpl(zpl)
```

### Batch Printing

```python
import os
from zebra_printer import ZebraPrinter

printer = ZebraPrinter()

# Print all PDFs in a folder
pdf_folder = "labels"
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder, filename)
        print(f"Printing {filename}...")
        printer.print_pdf(pdf_path)
```

## File Structure

```
printertest/
├── zebra_printer.py    # Main printer module
├── example.py          # Usage examples and demos
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Dependencies

- **PyMuPDF** - PDF processing and image extraction
- **Pillow** - Image manipulation and conversion
- **pywin32** - Windows printer communication

## License

This project is provided as-is for educational and commercial use.

## Support

For issues with:
- **Printer hardware:** Contact Zebra support
- **Driver issues:** Download latest drivers from zebra.com
- **Software issues:** Check printer connection and Windows settings

---

**Happy Printing! 🏷️**