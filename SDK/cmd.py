import sys
sys.dont_write_bytecode = True

cmds ={
    'xclicked0': "\x01\x05\x00\x0A\xFF\x00",#\x38\xAC
    'xrelease0': "\x01\x05\x00\x0A\x00\x00",
    'xclicked1': "\x01\x05\x00\x0B\xFF\x00",#0xF8FD
    'xrelease1': "\x01\x05\x00\x0B\x00\x00",
    'yclicked0': "\x01\x05\x00\x0C\xFF\x00",
    'yrelease0': "\x01\x05\x00\x0C\x00\x00",
    'yclicked1': "\x01\x05\x00\x0D\xFF\x00",
    'yrelease1': "\x01\x05\x00\x0D\x00\x00",
    'zclicked0': "\x01\x05\x00\x0E\xFF\x00",
    'zrelease0': "\x01\x05\x00\x0E\x00\x00",
    'zclicked1': "\x01\x05\x00\x0F\xFF\x00",
    'zrelease1': "\x01\x05\x00\x0F\x00\x00",
    'reset':     "\x01\x05\x00\x10\xFF\x00"
    }

cmdscrc = {
    'xclicked0': "\x01\x05\x00\x0A\xFF\x00\xac\x38",
    'xrelease0': "\x01\x05\x00\x0A\x00\x00\xed\xc8",
    'xclicked1': "\x01\x05\x00\x0B\xFF\x00\xfd\xf8",
    'xrelease1': "\x01\x05\x00\x0B\x00\x00\xbc\x08",
    'yclicked0': "\x01\x05\x00\x0C\xFF\x00\x4c\x39",
    'yrelease0': "\x01\x05\x00\x0C\x00\x00\x0d\xc9",
    'yclicked1': "\x01\x05\x00\x0D\xFF\x00\x1d\xf9",
    'yrelease1': "\x01\x05\x00\x0D\x00\x00\x5c\x09",
    'zclicked0': "\x01\x05\x00\x0E\xFF\x00\xed\xf9",
    'zrelease0': "\x01\x05\x00\x0E\x00\x00\xac\x09",
    'zclicked1': "\x01\x05\x00\x0F\xFF\x00\xbc\x39",
    'zrelease1': "\x01\x05\x00\x0F\x00\x00\xfd\xc9",
    'reset':     "\x01\x05\x00\x10\xFF\x00\x8D\xFF"
}


direction = {
    'xstart':     "\x00\xc8",
    'xforward':   "\x00\xc9",
    'xpulse':     "\x00\xca",
    'xfrequence': "\x00\xcc",
    'ystart':     "\x00\xd2",
    'yforward':   "\x00\xd3",
    'ypulse':     "\x00\xd4",
    'yfrequence': "\x00\xd6",
    'zstart':     "\x00\xdc",
    'zforward':   "\x00\xdd",
    'zpulse':     "\x00\xde",
    'zfrequence': "\x00\xe0",

}