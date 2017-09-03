from source.converters.timeframeConverter import TimeFrameConverter
import unittest

class TestTimeFrameConverter(unittest.TestCase):
    def test_init(self):
        con = TimeFrameConverter("hello")
