#!/usr/bin/env python3
"""
ZPL Examples and Quick Start Guide
==================================

This script demonstrates various ZPL label types you can create and print
with your Zebra GC420T printer.

Examples include:
- Simple text labels
- Barcode labels
- Product labels
- Shipping labels
- Custom ZPL commands
"""

from zebra_zpl import ZebraZPL
import datetime


def demo_text_label():
    """Demonstrate simple text label printing."""
    print("\n=== Text Label Demo ===")
    
    printer = ZebraZPL()
    if not printer.printer_name:
        print("❌ No Zebra printer found")
        return False
    
    # Create a simple text label
    title = "INVENTORY LABEL"
    text_lines = [
        "Item: Office Chair",
        "Location: Warehouse A-12",
        "Date: " + datetime.datetime.now().strftime("%Y-%m-%d"),
        "Status: In Stock"
    ]
    
    print(f"Creating text label: {title}")
    for line in text_lines:
        print(f"  {line}")
    
    response = input("Print this text label? (y/N): ")
    if response.lower() == 'y':
        success = printer.print_text_label(title, text_lines)
        return success
    return True


def demo_barcode_label():
    """Demonstrate barcode label printing."""
    print("\n=== Barcode Label Demo ===")
    
    printer = ZebraZPL()
    if not printer.printer_name:
        print("❌ No Zebra printer found")
        return False
    
    # Create a barcode label
    title = "ASSET TAG"
    barcode_data = "ASSET123456789"
    text_lines = [
        "Department: IT",
        "Type: Laptop",
        "Assigned: John Doe"
    ]
    
    print(f"Creating barcode label: {title}")
    print(f"Barcode: {barcode_data}")
    for line in text_lines:
        print(f"  {line}")
    
    response = input("Print this barcode label? (y/N): ")
    if response.lower() == 'y':
        success = printer.print_barcode_label(title, barcode_data, text_lines)
        return success
    return True


def demo_product_label():
    """Demonstrate product label printing."""
    print("\n=== Product Label Demo ===")
    
    printer = ZebraZPL()
    if not printer.printer_name:
        print("❌ No Zebra printer found")
        return False
    
    # Create a product label
    product_name = "Wireless Mouse"
    sku = "MOUSE-WL-001"
    price = "$29.99"
    description = "Ergonomic wireless mouse"
    
    print(f"Creating product label:")
    print(f"  Product: {product_name}")
    print(f"  SKU: {sku}")
    print(f"  Price: {price}")
    print(f"  Description: {description}")
    
    response = input("Print this product label? (y/N): ")
    if response.lower() == 'y':
        success = printer.print_product_label(product_name, sku, price, description=description)
        return success
    return True


def demo_shipping_label():
    """Demonstrate shipping label printing."""
    print("\n=== Shipping Label Demo ===")
    
    printer = ZebraZPL()
    if not printer.printer_name:
        print("❌ No Zebra printer found")
        return False
    
    # Create shipping label data
    from_info = {
        'name': 'ABC Company',
        'address1': '123 Business St',
        'address2': 'Suite 100',
        'city_state_zip': 'New York, NY 10001'
    }
    
    to_info = {
        'name': 'John Customer',
        'address1': '456 Home Ave',
        'address2': 'Apt 5B',
        'city_state_zip': 'Los Angeles, CA 90210'
    }
    
    tracking = "1Z999AA1234567890"
    
    print("Creating shipping label:")
    print(f"From: {from_info['name']}")
    print(f"To: {to_info['name']}")
    print(f"Tracking: {tracking}")
    
    response = input("Print this shipping label? (y/N): ")
    if response.lower() == 'y':
        success = printer.print_shipping_label(from_info, to_info, tracking)
        return success
    return True


def demo_custom_zpl():
    """Demonstrate custom ZPL commands."""
    print("\n=== Custom ZPL Demo ===")
    
    printer = ZebraZPL()
    if not printer.printer_name:
        print("❌ No Zebra printer found")
        return False
    
    # Custom ZPL for a warning label
    custom_zpl = """
^XA
^LH30,30
^FO50,20^ADN,30,15^FDWARNING^FS
^FO50,60^GB200,2,2^FS
^FO50,80^ADN,16,8^FDHIGH VOLTAGE^FS
^FO50,105^ADN,16,8^FDDANGER AREA^FS
^FO50,130^ADN,14,7^FDAuthorized Personnel Only^FS
^FO50,155^GB200,2,2^FS
^FO50,175^ADN,12,6^FDDate: """ + datetime.datetime.now().strftime("%Y-%m-%d") + """^FS
^XZ
"""
    
    print("Custom ZPL Warning Label:")
    print("  WARNING")
    print("  HIGH VOLTAGE")
    print("  DANGER AREA")
    print("  Authorized Personnel Only")
    
    response = input("Print this custom ZPL label? (y/N): ")
    if response.lower() == 'y':
        success = printer.send_zpl(custom_zpl)
        return success
    return True


def show_zpl_templates():
    """Show ZPL code examples for different label types."""
    print("\n=== ZPL Templates ===")
    
    print("\n1. Simple Text Label:")
    print("""
^XA
^LH30,30
^FO20,10^ADN,36,20^FDMy Label Title^FS
^FO20,60^ADN,18,10^FDLine 1 of text^FS
^FO20,85^ADN,18,10^FDLine 2 of text^FS
^XZ
""")
    
    print("\n2. Barcode Label:")
    print("""
^XA
^LH30,30
^FO20,10^ADN,24,12^FDProduct Code^FS
^FO20,50^ADN,18,10^FDSKU: ABC123^FS
^FO20,90^BY2^BCN,70,Y,N,N^FD123456789012^FS
^XZ
""")
    
    print("\n3. ZPL Command Reference:")
    print("^XA          - Start format")
    print("^XZ          - End format")
    print("^LH30,30     - Label home position")
    print("^FO20,10     - Field origin (x,y coordinates)")
    print("^ADN,36,20   - Font (A=font, D=default, N=normal, size, width)")
    print("^FD...^FS    - Field data")
    print("^BCN,70      - Barcode Code 128, height 70")
    print("^BY2         - Barcode bar width 2")
    print("^GB200,2,2   - Graphic box (width, height, thickness)")


def main():
    """Main function to run ZPL examples."""
    print("🏷️  Zebra GC420T ZPL Printer - Examples & Quick Start")
    print("=" * 60)
    
    # Check printer availability
    printer = ZebraZPL()
    if not printer.printer_name:
        print("❌ No Zebra printer found!")
        print("\nAvailable printers:")
        for p in printer.list_printers():
            print(f"  - {p}")
        print("\nPlease ensure your Zebra GC420T is connected and drivers are installed.")
        return
    
    print(f"✅ Found Zebra printer: {printer.printer_name}")
    
    while True:
        print("\n" + "=" * 60)
        print("Choose an example to run:")
        print("1. Simple Text Label")
        print("2. Barcode Label") 
        print("3. Product Label")
        print("4. Shipping Label")
        print("5. Custom ZPL Commands")
        print("6. Show ZPL Templates")
        print("7. Quick Command Line Examples")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-7): ").strip()
        
        if choice == '0':
            print("Goodbye!")
            break
        elif choice == '1':
            demo_text_label()
        elif choice == '2':
            demo_barcode_label()
        elif choice == '3':
            demo_product_label()
        elif choice == '4':
            demo_shipping_label()
        elif choice == '5':
            demo_custom_zpl()
        elif choice == '6':
            show_zpl_templates()
        elif choice == '7':
            show_command_examples()
        else:
            print("Invalid choice. Please try again.")


def show_command_examples():
    """Show command line usage examples."""
    print("\n=== Command Line Examples ===")
    
    print("\n1. List available printers:")
    print("python zebra_zpl.py --list-printers")
    
    print("\n2. Print simple text label:")
    print('python zebra_zpl.py --text "OFFICE SUPPLIES" "Item: Stapler" "Location: Desk 5"')
    
    print("\n3. Print barcode label:")
    print('python zebra_zpl.py --barcode "INVENTORY" "ITEM123456789"')
    
    print("\n4. Print product label:")
    print('python zebra_zpl.py --product "USB Cable" "USB-C-001" "$9.99"')
    
    print("\n5. Print multiple copies:")
    print('python zebra_zpl.py --text "COPY TEST" "This is a test" --copies 3')
    
    print("\n6. Send raw ZPL commands:")
    print('python zebra_zpl.py --raw-zpl "^XA^FO50,50^ADN,36,20^FDHello World^FS^XZ"')
    
    print("\n7. Print from ZPL file:")
    print('python zebra_zpl.py --zpl-file my_label.zpl')
    
    print("\n8. Specify printer:")
    print('python zebra_zpl.py --printer "ZDesigner GC420t (EPL)" --text "TEST" "Hello"')


if __name__ == "__main__":
    main()