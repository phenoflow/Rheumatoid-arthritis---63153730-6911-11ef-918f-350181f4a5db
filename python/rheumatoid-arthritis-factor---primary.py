# phekb, 2024.

import sys, csv, re

codes = [{"code":"M05","system":"conceptcd"},{"code":"M05.8","system":"conceptcd"},{"code":"M05.84","system":"conceptcd"},{"code":"M05.842","system":"conceptcd"},{"code":"M05.85","system":"conceptcd"},{"code":"M05.852","system":"conceptcd"},{"code":"M05.86","system":"conceptcd"},{"code":"M05.862","system":"conceptcd"},{"code":"M06.0","system":"conceptcd"},{"code":"M06.04","system":"conceptcd"},{"code":"M06.042","system":"conceptcd"},{"code":"M06.05","system":"conceptcd"},{"code":"M06.052","system":"conceptcd"},{"code":"M06.06","system":"conceptcd"},{"code":"M06.062","system":"conceptcd"},{"code":"15205-8","system":"conceptcd"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('rheumatoid-arthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["rheumatoid-arthritis-factor---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["rheumatoid-arthritis-factor---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["rheumatoid-arthritis-factor---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
