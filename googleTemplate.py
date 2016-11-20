import sys, getopt

def main(argv):
    global month, day, year
    try:
        opts, args = getopt.getopt(argv, "m:d:y", ["month=","day=","year="])
    except getopt.GetoptError:
        print('option error')
        sys.exit(2)
    for opt, arg in opts:
        if len(opts) < 3:
            print('arg error')
            sys.exit(2)
        if opt in ("-m", "--month"):
            month = arg
        elif opt in ("-d", "--day"):
            day = arg
        elif opt in ("-y", "--year"):
            year = arg
    doDates()

def doDates():
    from datetime import date
    import os, html
    
    global day, month, year
    
    currdate = date(eval(year), eval(month), eval(day))
    table_data = []
    for i in range(0, 40):
        if (i % 5 == 0):
            table_data.append(['Week '])
        rowlist = [].append(currdate)
        rowlist.append('Unit:  <br /> Topic')
        rowlist.append('')
        table_data.append(rowlist)
    h = HTML.table(table_data,header_row=['Date', 'Learning Plan', 'HW/Notes'])
    copy(h)

def copy(text):
    GMEM_DDESHARE = 0x2000
    CF_UNICODETEXT = 13
    d = ctypes.windll # cdll expects 4 more bytes in user32.OpenClipboard(None)
    try:  # Python 2
        if not isinstance(text, unicode):
            text = text.decode('mbcs')
    except NameError:
        if not isinstance(text, str):
            text = text.decode('mbcs')
    d.user32.OpenClipboard(0)
    d.user32.EmptyClipboard()
    hCd = d.kernel32.GlobalAlloc(GMEM_DDESHARE, len(text.encode('utf-16-le')) + 2)
    pchData = d.kernel32.GlobalLock(hCd)
    ctypes.cdll.msvcrt.wcscpy(ctypes.c_wchar_p(pchData), text)
    d.kernel32.GlobalUnlock(hCd)
    d.user32.SetClipboardData(CF_UNICODETEXT, hCd)
    d.user32.CloseClipboard()


if __name__ == "__main__":
	main(sys.argv[1:])
