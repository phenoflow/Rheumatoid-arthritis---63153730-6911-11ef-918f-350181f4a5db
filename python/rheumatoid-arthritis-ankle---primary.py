# phekb, 2024.

import sys, csv, re

codes = [{"code":"M05.17","system":"conceptcd"},{"code":"M05.171","system":"conceptcd"},{"code":"M05.172","system":"conceptcd"},{"code":"M05.87","system":"conceptcd"},{"code":"M05.871","system":"conceptcd"},{"code":"M05.872","system":"conceptcd"},{"code":"M06.07","system":"conceptcd"},{"code":"M06.071","system":"conceptcd"},{"code":"M06.072","system":"conceptcd"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('rheumatoid-arthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["rheumatoid-arthritis-ankle---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["rheumatoid-arthritis-ankle---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["rheumatoid-arthritis-ankle---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
