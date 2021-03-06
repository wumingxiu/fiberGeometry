from simulator.client import Client
from simulator.server import ImgServer, SeverMain, SharpSever
from threading import Thread
import multiprocessing
from tornado.ioloop import IOLoop
from functools import partial
from simulator.methods import getImage
from tornado.iostream import StreamClosedError
import time
import logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

def test_sharpserver():
    ss = SharpSever()
    ss.getAll()


def test_imgserver():
    port = 9880
    # port = 9801
    Thread(target = SeverMain, args=(port,)).start()
    # multiprocessing.Process(target=servermain).start()
    # time.sleep(1)
    img = getImage('IMG/midoc.BMP')
    imgstr = img.tobytes()
    result = IOLoop.current().run_sync(Client(port=port).get_img_once)
    assert len(result) == len(imgstr)
    assert imgstr != result
    print len(result)
    para = ('getImage', 'IMG/midoc.BMP')
    IOLoop.current().run_sync(partial(Client(port=port).get_change,para))
    result = IOLoop.current().run_sync(Client(port=port).get_img_once)
    assert len(result) == len(imgstr)
    assert imgstr == result
    para = ('randomImg', 'IMG/G652/pk/')
    IOLoop.current().run_sync(partial(Client(port=port).get_change, para))
    result = IOLoop.current().run_sync(Client(port=port).get_img_once)
    assert len(result) == len(imgstr)
    assert imgstr != result
    IOLoop.current().run_sync(Client(port=port).close_server)


def test_getimg_multi_connect():
    port = 9881
    # port = 9801
    img = getImage('IMG/midoc.BMP')
    imgstr = img.tobytes()
    Thread(target = SeverMain, args=(port,)).start()
    # multiprocessing.Process(target=SeverMain, args=(port,)).start()
    print 'start multi connect'
    for x in range(0,300):
        try:
            # time.sleep(0.5)
            result = IOLoop.current().run_sync(Client(port=port).get_img_once)
            assert len(result) == len(imgstr)
        except StreamClosedError:
            logger.warning("Lost host at client %s")
            return
        except Exception as e:
            print 'range time', x
            raise e
        if x%50 == 0:
            print 'create times',x, time.time()
    IOLoop.current().run_sync(Client(port=port).close_server)



# def test_imgserver():
#     Thread(target = SeverMain).start()
    # multiprocessing.Process(target=servermain).start()
    # time.sleep(1)

if __name__ == "__main__":
    port = 9880
    para = ('randomImg', 'IMG/emptytuple/eptlight2')
    IOLoop.current().run_sync(partial(Client(port=port).get_change, para))