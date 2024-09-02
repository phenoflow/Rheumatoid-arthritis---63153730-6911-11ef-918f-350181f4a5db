# phekb, 2024.

import sys, csv, re

codes = [{"code":"M06.3","system":"conceptcd"},{"code":"M06.31","system":"conceptcd"},{"code":"M06.311","system":"conceptcd"},{"code":"M06.312","system":"conceptcd"},{"code":"M06.32","system":"conceptcd"},{"code":"M06.321","system":"conceptcd"},{"code":"M06.322","system":"conceptcd"},{"code":"M06.33","system":"conceptcd"},{"code":"M06.331","system":"conceptcd"},{"code":"M06.332","system":"conceptcd"},{"code":"M06.34","system":"conceptcd"},{"code":"M06.341","system":"conceptcd"},{"code":"M06.342","system":"conceptcd"},{"code":"M06.35","system":"conceptcd"},{"code":"M06.351","system":"conceptcd"},{"code":"M06.352","system":"conceptcd"},{"code":"M06.36","system":"conceptcd"},{"code":"M06.361","system":"conceptcd"},{"code":"M06.362","system":"conceptcd"},{"code":"M06.37","system":"conceptcd"},{"code":"M06.371","system":"conceptcd"},{"code":"M06.372","system":"conceptcd"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('rheumatoid-arthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["rheumatoid-arthritis-nodule---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["rheumatoid-arthritis-nodule---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["rheumatoid-arthritis-nodule---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
