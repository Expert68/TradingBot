class TimeFrameConverter:
    """docstring for TimeFrame."""
    def __init__(self, inputFile, timeFrame, outputFile):
        self.inputFile = inputFile
        self.timeFrame = timeFrame
        self.outputFile = outputFile
        print (self.inputFile + " " + self.timeFrame + " " + self.outputFile)
