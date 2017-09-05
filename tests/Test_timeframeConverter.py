from source.converters.timeframeConverter import TimeFrameConverter
import unittest, os

class TestTimeFrameConverter(unittest.TestCase):
    def setUp(self):
        pre = os.path.dirname(__file__)
        inputPath = pre + "/resources/TestData.csv"
        timeframe = "5"
        self.outputPath = pre + "/result.csv"
        self.con = TimeFrameConverter(inputPath, timeframe, self.outputPath)

    def tearDown(self):
        if os.path.exists(self.outputPath):
            os.remove(self.outputPath)

    def test_init(self):
        inputPath = "Test/inputpath.csv"
        timeframe = "15"
        outputPath = "output.csv"
        con = TimeFrameConverter(inputPath, timeframe, outputPath)
        self.assertEqual(inputPath, con.inputFile)
        self.assertEqual(timeframe, con.timeFrame)
        self.assertEqual(outputPath, con.outputFile)

    def test_generate(self):
        self.con.generate()
        expected = "20170601 000000;1.100000;1.125000;1.099900;1.110000"
        expected2 = "20170601 000500;1.100000;1.120000;1.099900;1.110000"
        expected3 = "20170601 001000;1.100000;1.125000;1.000000;1.110000"
        result = open(self.outputPath)
        line = result.readline().strip()
        line2 = result.readline().strip()
        line3 = result.readline().strip()
        line4 = result.readline().strip()
        result.close()
        self.assertEqual("", line4)
        self.assertEqual(expected3, line3)
        self.assertEqual(expected2, line2)
        self.assertEqual(expected, line)
