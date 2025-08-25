#!/usr/bin/env python3
"""
Example Usage of Zebra GC420T PDF Printer
==========================================

This script demonstrates how to use the zebra_printer module to print PDF files
to your Zebra GC420T thermal printer.

Usage Examples:
1. Basic printing: python example.py
2. Print specific PDF: python example.py path/to/your/file.pdf
3. Print multiple copies: python example.py path/to/your/file.pdf --copies 3
"""

import os
import sys
from zebra_printer import ZebraPrinter


def create_sample_pdf():
    """Create a sample PDF for testing if none is provided."""
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        
        filename = "sample_label.pdf"
        c = canvas.Canvas(filename, pagesize=(4*72, 3*72))  # 4x3 inch label
        
        # Add some content
        c.setFont("Helvetica", 12)
        c.drawString(50, 150, "Zebra GC420T Test Label")
        c.setFont("Helvetica", 10)
        c.drawString(50, 130, "Date: August 25, 2025")
        c.drawString(50, 110, "Status: Testing PDF Print")
        
        # Add a simple barcode-like pattern
        c.setFont("Helvetica", 8)
        c.drawString(50, 90, "|||| || ||| | |||| |||")
        c.drawString(50, 70, "123456789012")
        
        c.save()
        print(f"Created sample PDF: {filename}")
        return filename
        
    except ImportError:
        print("ReportLab not available. Creating simple text file instead.")
        # Create a simple text file that can be converted to PDF
        filename = "sample_text.txt"
        with open(filename, 'w') as f:
            f.write("Zebra GC420T Test Label\n")
            f.write("Date: August 25, 2025\n")
            f.write("Status: Testing PDF Print\n")
            f.write("|||| || ||| | |||| |||\n")
            f.write("123456789012\n")
        print(f"Created sample text file: {filename}")
        print("Note: You'll need to convert this to PDF manually or install ReportLab")
        return None


def demo_basic_usage():
    """Demonstrate basic usage of the ZebraPrinter class."""
    print("=== Zebra GC420T PDF Printer Demo ===\n")
    
    # Initialize the printer
    print("1. Initializing printer...")
    printer = ZebraPrinter()
    
    # List available printers
    print("2. Available printers:")
    printers = printer.list_printers()
    for i, p in enumerate(printers, 1):
        marker = " <- Zebra" if 'zebra' in p.lower() or 'gc420' in p.lower() else ""
        print(f"   {i}. {p}{marker}")
    
    if not printer.printer_name:
        print("\n❌ No Zebra printer found automatically.")
        print("Please ensure your Zebra GC420T is:")
        print("   - Connected via USB or network")
        print("   - Properly installed in Windows")
        print("   - Set as a printer in Windows settings")
        return False
    
    print(f"\n3. Using printer: {printer.printer_name}")
    
    # Get printer status
    status = printer.get_printer_status()
    if status:
        print("4. Printer status:")
        for key, value in status.items():
            print(f"   {key}: {value}")
    
    return True


def demo_pdf_printing(pdf_file=None, copies=1):
    """Demonstrate PDF printing functionality."""
    print("\n=== PDF Printing Demo ===\n")
    
    # Initialize printer
    printer = ZebraPrinter()
    
    if not printer.printer_name:
        print("❌ No Zebra printer available for printing demo")
        return False
    
    # Use provided PDF or create a sample
    if not pdf_file:
        print("No PDF file specified, creating sample...")
        pdf_file = create_sample_pdf()
        if not pdf_file:
            print("❌ Could not create sample PDF")
            return False
    
    if not os.path.exists(pdf_file):
        print(f"❌ PDF file not found: {pdf_file}")
        return False
    
    print(f"📄 PDF file: {pdf_file}")
    print(f"🖨️  Printer: {printer.printer_name}")
    print(f"📋 Copies: {copies}")
    
    # Confirm before printing
    response = input("\nProceed with printing? (y/N): ")
    if response.lower() != 'y':
        print("Printing cancelled.")
        return False
    
    # Print the PDF
    print("\n🖨️  Starting print job...")
    success = printer.print_pdf(pdf_file, copies=copies)
    
    if success:
        print("✅ Print job completed successfully!")
    else:
        print("❌ Print job failed!")
    
    return success


def demo_zpl_commands():
    """Demonstrate sending raw ZPL commands to the printer."""
    print("\n=== ZPL Commands Demo ===\n")
    
    printer = ZebraPrinter()
    
    if not printer.printer_name:
        print("❌ No Zebra printer available for ZPL demo")
        return False
    
    # Sample ZPL command for a simple label
    zpl_commands = """
^XA
^LH30,30
^FO20,10^ADN,36,20^FDZEBRA GC420T TEST^FS
^FO20,60^ADN,18,10^FDDate: August 25, 2025^FS
^FO20,90^ADN,18,10^FDStatus: ZPL Command Test^FS
^FO20,120^BY2^BCN,70,Y,N,N^FD123456789012^FS
^XZ
"""
    
    print("ZPL Commands to send:")
    print(zpl_commands)
    
    response = input("Send ZPL commands to printer? (y/N): ")
    if response.lower() != 'y':
        print("ZPL command sending cancelled.")
        return False
    
    print("\n📡 Sending ZPL commands...")
    success = printer.send_raw_zpl(zpl_commands)
    
    if success:
        print("✅ ZPL commands sent successfully!")
    else:
        print("❌ Failed to send ZPL commands!")
    
    return success


def main():
    """Main function to run examples."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Zebra GC420T PDF Printer Examples')
    parser.add_argument('pdf_file', nargs='?', help='PDF file to print (optional)')
    parser.add_argument('--copies', '-c', type=int, default=1, help='Number of copies')
    parser.add_argument('--demo', '-d', choices=['basic', 'pdf', 'zpl', 'all'], 
                       default='all', help='Which demo to run')
    
    args = parser.parse_args()
    
    print("🏷️  Zebra GC420T PDF Printer - Example Usage")
    print("=" * 50)
    
    success = True
    
    if args.demo in ['basic', 'all']:
        success &= demo_basic_usage()
    
    if args.demo in ['pdf', 'all'] and success:
        success &= demo_pdf_printing(args.pdf_file, args.copies)
    
    if args.demo in ['zpl', 'all'] and success:
        success &= demo_zpl_commands()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ All demos completed successfully!")
    else:
        print("❌ Some demos failed. Check printer connection and setup.")
    
    print("\nTips for using your Zebra GC420T:")
    print("1. Ensure the printer is connected via USB or network")
    print("2. Install the latest Zebra drivers from zebra.com")
    print("3. Use 203 DPI for optimal print quality")
    print("4. For labels, use thermal transfer or direct thermal media")
    print("5. Adjust label size in your PDF to match your media")


if __name__ == "__main__":
    main()