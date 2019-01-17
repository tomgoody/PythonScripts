
def fwf_to_csv(input_file, widths, output_file):
    import csv

    def delimit(line):
        start  = 0
        end    = widths[0]
        row    = []

        for width in widths[1:]:
            row.append(line[start:end])
            start = end
            end += width
        row.append(line[start:end])

        return row

    with open(input_file) as fh, open(output_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for line in fh:
            row = delimit(line.rstrip('\n'))
            writer.writerow(row)

input_file  = '/filepath/filename.txt'
output_file = '/filepath/filename.csv'

"""The widths values can be changed to the number of character spaces needed to delimit the file."""
widths      = [20, 25, 50, 2, 8, 50, 2, 40, 20, 20, 40,
               30, 3, 3, 10, 80,
               1, 2, 8, 8, 8, 8, 8,
			   2, 5, 5, 8, 20,
               2, 5, 8, 8, 2, 8, 8, 1,
			   3, 3, 3, 3, 3, 3,
               1, 1, 1, 1, 1, 1,
			   2, 1, 1, 1, 1, 8, 8, 129,
			   1, 2, 8, 20, 2, 255, 2, 1,
               8, 1, 255, 1, 10, 255,
			   1, 255, 8, 1]

fwf_to_csv(input_file=input_file, widths=widths, output_file=output_file)
