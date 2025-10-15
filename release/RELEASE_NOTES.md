# Zebra Printer System - Release v2.1.0

**Release Date**: October 15, 2025
**Build**: Production Ready
**Executable Size**: 42.0 MB

## 🎉 What's New in v2.1.0

### ✅ Enhanced Pattern Matching
- Support for 6+ different data formats
- Automatic ATS prefix addition
- Multiple backup patterns for compatibility
- Flexible delimiter and separator support

### ✅ Improved Serial Communication
- Timeout-based data processing
- Multiple line ending support (\n, \r\n, \r)
- Enhanced buffering for fragmented data
- Comprehensive debug logging

### ✅ Debug Tools Included
- **debug_serial_monitor.py**: Complete serial debugging tool
- **test_pattern_matching.py**: Pattern verification utility
- Remote troubleshooting capabilities

### ✅ Tested & Verified
- ✅ GUI launches successfully
- ✅ Zebra printer detection working
- ✅ Serial communication established
- ✅ Pattern matching handles multiple formats
- ✅ File system properly initialized
- ✅ Template loading functional

## 📁 Release Contents

```
release/
├── ZebraPrinterGUI.exe          # Main application (42MB)
├── debug_serial_monitor.py      # Serial debugging tool
├── test_pattern_matching.py     # Pattern testing utility
├── requirements.txt             # Python dependencies (for debug tools)
├── README.md                    # Complete documentation
└── templates/
    ├── device_label_template.zpl
    └── manual_box_label_template.html
```

## 🚀 Quick Start

1. **Download** the release folder
2. **Run** `ZebraPrinterGUI.exe`
3. **Connect** your device to serial port
4. **Select** Auto Print or Queue Mode
5. **Start printing** device labels!

## 🔧 If Issues Occur

1. **Run debug tools** on the target system:
   ```bash
   python debug_serial_monitor.py
   ```

2. **Check pattern matching**:
   ```bash
   python test_pattern_matching.py
   ```

3. **Verify serial settings**:
   - Baud rate: 115200 (default)
   - Data format: `##SERIAL|IMEI|IMSI|CCID|MAC##`

## 📋 Supported Data Formats

The system handles these formats automatically:
- `##ATS986063608048|867315088718139|286016570186236|8990011418220012368F|24:5D:F9:7D:78:50##`
- `##986063608048|867315088718139|286016570186236|8990011418220012368F|24:5D:F9:7D:78:50##`
- `986063608048|867315088718139|286016570186236|8990011418220012368F|24:5D:F9:7D:78:50`
- And more variants with different delimiters and separators

## 💡 Support

For issues or questions:
1. Check README.md for troubleshooting
2. Use debug tools to gather information
3. Provide debug output for assistance

---
**Built with Python 3.11+ | Tested on Windows | Compatible with Zebra GC420T**