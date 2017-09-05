import os, csv

class TimeFrameConverter:
    """docstring for TimeFrame."""
    def __init__(self, inputFile, timeFrame, outputFile):
        self.inputFile = inputFile
        self.timeFrame = timeFrame
        self.outputFile = outputFile

    def generate(self):
        with open(self.inputFile, newline='') as csvfile:
            out = open(self.outputFile, "w")
            reader = csv.reader(csvfile, delimiter=';')
            i = 0
            rows = []
            for row in reader:
                rows.append(row)
                i += 1
                if i == int(self.timeFrame):
                    new = self.__getNewValue(rows)
                    out.write(new + "\n")
                    rows.clear()
                    i = 0
            out.close()

    def __getNewValue(self, rows):
        #set datetime and open
        new = rows[0][0] + ';' + rows[0][1]
        high = float(rows[0][2])
        low = float(rows[0][3])
        for row in rows:
            if float(row[2]) > high:
                high = float(row[2])
            if float(row[3]) < low:
                low = float(row[3])

        new += ";{:.6f};{:.6f};".format(high,low) + rows[-1][4]
        return new
