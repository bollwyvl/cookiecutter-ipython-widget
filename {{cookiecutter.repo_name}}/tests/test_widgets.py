import glob
import os
import re
import sys
import time

from IPython.testing import iptestcontroller

test_root = os.path.dirname(__file__)

tests = glob.glob(os.path.join(test_root, 'test_*.coffee')) + \
    glob.glob(os.path.join(test_root, 'test_*.js'))

class JSController(iptestcontroller.JSController):
    def __init__(self, section, xunit=True, engine='phantomjs'):
        """Create new test runner."""
        iptestcontroller.TestController.__init__(self)

        self.engine = engine
        self.section = section
        self.xunit = xunit
        self.slimer_failure = re.compile('^FAIL.*', flags=re.MULTILINE)

        ip_test_dir = iptestcontroller.get_js_test_dir()

        extras = [
            '--includes=' + os.path.join(ip_test_dir, 'util.js'),
            '--engine=%s' % self.engine
        ]

        self.cmd = ['casperjs', 'test'] + extras + tests


def main():
    controller = JSController("custom")
    exitcode = 1
    try:
        controller.setup()
        controller.launch(buffer_output=False)
        exitcode = controller.wait()
        controller.cleanup()
    except Exception as err:
        print(err)
        exitcode = 1
    finally:
        sys.exit(exitcode)

if __name__ == '__main__':
    main()
