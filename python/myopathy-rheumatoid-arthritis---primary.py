# phekb, 2024.

import sys, csv, re

codes = [{"code":"M05.4","system":"conceptcd"},{"code":"M05.40","system":"conceptcd"},{"code":"M05.41","system":"conceptcd"},{"code":"M05.411","system":"conceptcd"},{"code":"M05.412","system":"conceptcd"},{"code":"M05.419","system":"conceptcd"},{"code":"M05.42","system":"conceptcd"},{"code":"M05.421","system":"conceptcd"},{"code":"M05.422","system":"conceptcd"},{"code":"M05.429","system":"conceptcd"},{"code":"M05.43","system":"conceptcd"},{"code":"M05.431","system":"conceptcd"},{"code":"M05.432","system":"conceptcd"},{"code":"M05.439","system":"conceptcd"},{"code":"M05.44","system":"conceptcd"},{"code":"M05.441","system":"conceptcd"},{"code":"M05.442","system":"conceptcd"},{"code":"M05.449","system":"conceptcd"},{"code":"M05.45","system":"conceptcd"},{"code":"M05.451","system":"conceptcd"},{"code":"M05.452","system":"conceptcd"},{"code":"M05.459","system":"conceptcd"},{"code":"M05.46","system":"conceptcd"},{"code":"M05.461","system":"conceptcd"},{"code":"M05.462","system":"conceptcd"},{"code":"M05.469","system":"conceptcd"},{"code":"M05.47","system":"conceptcd"},{"code":"M05.471","system":"conceptcd"},{"code":"M05.472","system":"conceptcd"},{"code":"M05.479","system":"conceptcd"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('rheumatoid-arthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["myopathy-rheumatoid-arthritis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["myopathy-rheumatoid-arthritis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["myopathy-rheumatoid-arthritis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
