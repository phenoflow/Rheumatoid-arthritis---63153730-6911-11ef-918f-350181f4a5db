# phekb, 2024.

import sys, csv, re

codes = [{"code":"M05.0","system":"conceptcd"},{"code":"M05.01","system":"conceptcd"},{"code":"M05.011","system":"conceptcd"},{"code":"M05.012","system":"conceptcd"},{"code":"M05.02","system":"conceptcd"},{"code":"M05.021","system":"conceptcd"},{"code":"M05.022","system":"conceptcd"},{"code":"M05.03","system":"conceptcd"},{"code":"M05.031","system":"conceptcd"},{"code":"M05.032","system":"conceptcd"},{"code":"M05.04","system":"conceptcd"},{"code":"M05.041","system":"conceptcd"},{"code":"M05.042","system":"conceptcd"},{"code":"M05.05","system":"conceptcd"},{"code":"M05.051","system":"conceptcd"},{"code":"M05.052","system":"conceptcd"},{"code":"M05.06","system":"conceptcd"},{"code":"M05.061","system":"conceptcd"},{"code":"M05.062","system":"conceptcd"},{"code":"M05.07","system":"conceptcd"},{"code":"M05.071","system":"conceptcd"},{"code":"M05.072","system":"conceptcd"},{"code":"714.1","system":"conceptcd"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('rheumatoid-arthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["rheumatoid-arthritis-felty---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["rheumatoid-arthritis-felty---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["rheumatoid-arthritis-felty---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
