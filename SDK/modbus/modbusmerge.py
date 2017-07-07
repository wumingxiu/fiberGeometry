import struct
from collections import deque, OrderedDict

import serial
import crcmod

from SDK.modbus.directions import HEAD_DIR, MOTOR_GROUP, START_STOP, UP_DOWN
from SDK.modbusabs import ModbusConnectionException
import logging

logger = logging.getLogger(__name__)


class SendTranslater(object):
    def __init__(self):
        self.crc16 = crcmod.predefined.mkCrcFun('modbus')

    def __call__(self, station, head_dir, move):
        station = self._get_station(station)
        if head_dir not in HEAD_DIR.keys():
            raise ValueError("head direction error")
        head_dir = HEAD_DIR[head_dir]

        if isinstance(move, str):
            if move in ('start', 'stop'):
                result = self._dimension_motor_by_str(station, head_dir, move)
            elif move in ('up', 'down'):
                result = self._up_down_motor(station, head_dir, move)
            elif move == 'rest':
                result = self._rest_motor(station, head_dir, move)
            else:
                raise ValueError("error move command")
        elif isinstance(move, int):
            result = self._dimension_motor_by_int(station, head_dir, move)
        else:
            raise ValueError('error command type')
        crc = struct.pack('>H', self.crc16(result))
        result = result + crc[1:] + crc[:1]
        return result

    def _get_station(self, station):
        if station in MOTOR_GROUP[0]:
            return '\x01'
        elif station in MOTOR_GROUP[1]:
            return '\x02'
        else:
            raise ValueError("station code error")

    def _dimension_motor_by_str(self, station, head_dir, move):
        if move == 'start':
            move = START_STOP[0]
        else:
            move = START_STOP[1]
        cmd = station + '\x10' + head_dir + '\x00\x01\x02' + move
        return cmd

    def _dimension_motor_by_int(self, station, head_dir, move):
        for_invert = struct.pack('>I', move)
        move = for_invert[2:]
        cmd = station + '\x10' + head_dir + '\x00\x02\x04' + START_STOP[0] + move
        return cmd

    def _up_down_motor(self, station, head_dir, move):
        if move == 'up':
            move = UP_DOWN[0]
        else:
            move = UP_DOWN[1]
        cmd = station + '\x10' + head_dir + '\x00\x01\x02' + move
        return cmd

    def _rest_motor(self, station, head_dir, move):
        cmd = station + '\x10' + HEAD_DIR['rest'] + '\x00\x01\x02' + '\x00\x02'
        return cmd

class ReadTranslater(object):
    def __init__(self):
        self.axies = ('x', 'y', 'z')
        self.crc16 = crcmod.predefined.mkCrcFun('modbus')

    def __call__(self, axis):

        if axis not in self.axies:
            raise KeyError('axis input error')

        cmdline = '\x01\x03' \
              + HEAD_DIR[axis]\
              + '\x00\x02'
        crc = struct.pack('>H',self.crc16(cmdline))
        cmdline = cmdline + crc[1:] + crc[:1]
        return cmdline


class AbsModeBusModeByAxis(object):
    def __init__(self, port=None, baudrate=19200, store=None):
        super(AbsModeBusModeByAxis, self).__init__()
        self.IsWriting = True
        self.ser = serial.Serial(port, baudrate, timeout=0.05, parity='E')
        self.data_buffer = None
        # self.forward = False
        self.send_translater = SendTranslater()
        self.read_translater = ReadTranslater()
        self.direction = self.location() or 3000
        self.queue = deque(maxlen=15)
        print('init')

    # @mutex_lock
    def goto(self, direction, axis='x'):
        self.direction = direction
        send = self.send_translater(axis, self.direction)
        logger.info('mode send cmd' + " ".join("{:02x}".format(ord(c)) for c in send))
        self.ser.write(send)
        self.data_buffer = self._read_untill_data_in('\x10')

    def scram(self, axis):
        send = self.send_translater(axis, False)
        logger.info('send stop cmd' + " ".join("{:02x}".format(ord(c)) for c in send))
        self.ser.write(send)
        self.data_buffer = self._read_untill_data_in('\x10')

    # @mutex_lock
    def location(self, axis):
        logger.debug("lod ing location")
        read = self.read_translater(axis)
        info = 'mode send cmd ' + " ".join("{:02x}".format(ord(c)) for c in read)
        logger.debug(info)
        self.ser.write(read)

        self.data_buffer = self._read_untill_data_in('\x03')
        # info = 'mode get cmd '+" ".join("{:02x}".format(ord(c)) for c in self.data_buffer)
        logger.debug(info)
        if len(self.data_buffer) < 6:
            debug = "error " + " ".join("{:02x}".format(ord(c)) for c in self.data_buffer)
            logger.debug(debug)
            raise ModbusConnectionException("data buffer length error")
        # print 'master get cmd ', " ".join("{:02x}".format(ord(c)) for c in self.data_buffer)
        reversed = self.data_buffer[3:-2]
        if reversed:
            _ = struct.unpack('>I', reversed[2:] + reversed[:2])[0]
            # print 'get _', _
            return _
            # return None

    def _read_untill_data_in(self, mode='\x03'):
        IS = True
        while IS:
            _0 = self.ser.read(1)
            if _0 != '\x01':
                continue
            _1 = self.ser.read(1)
            if _1 == '\x03':
                _2 = self.ser.read(1)
                length = struct.unpack('>b', _2)[0]
                readed = self.ser.read(length * 2 + 2)
                return '\x01\x03' + _2 + readed
            elif _1 == '\x10':
                return '\x01\x03' + self.ser.read(6)
            else:
                raise ValueError('bad input data')
