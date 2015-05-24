import shutil

def patch(filename, chunk, replacement):
    f = open(filename, 'r+b')
    a = f.read()
    z = ''.join(chr(int(b, 16)) for b in chunk.split())
    p = a.find(z)
    if p == -1 or a.find(z, p+len(z)) != -1:
        print 'patch doesn\'t fit or file already patched'
    else:
        if raw_input('chunk found (offset %#x), patch? (Y/n) ' % p) != 'n':
            shutil.copy(filename, filename + '.bak')
            f.seek(p)
            f.write(replacement)
            print 'patch successful'
        else:
            print 'patching cancelled'
    f.close()

patch('c:/windows/syswow64/cmd.exe', '68 28 23 00 00 68 7B 23 00 00', '\x90' * 0x1A)
patch('c:/windows/system32/cmd.exe', 'BA 7B 23 00 00 33 C9', '\x90' * 0x20)
