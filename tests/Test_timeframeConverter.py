from source.converters.timeframeConverter import TimeFrameConverter
import unittest

class TestTimeFrameConverter(unittest.TestCase):
    def test_init(self):
        inputPath = "resources/TestData.csv"
        timeframe = "5"
        outputPath = "output.csv"
        con = TimeFrameConverter(inputPath, timeframe, outputPath)
        self.assertEqual(inputPath, con.inputFile)
        self.assertEqual(timeframe, con.timeFrame)
        self.assertEqual(outputPath, con.outputFile)
