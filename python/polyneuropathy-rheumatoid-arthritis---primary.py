# phekb, 2024.

import sys, csv, re

codes = [{"code":"M05.5","system":"conceptcd"},{"code":"M05.50","system":"conceptcd"},{"code":"M05.51","system":"conceptcd"},{"code":"M05.511","system":"conceptcd"},{"code":"M05.512","system":"conceptcd"},{"code":"M05.519","system":"conceptcd"},{"code":"M05.52","system":"conceptcd"},{"code":"M05.521","system":"conceptcd"},{"code":"M05.522","system":"conceptcd"},{"code":"M05.529","system":"conceptcd"},{"code":"M05.53","system":"conceptcd"},{"code":"M05.531","system":"conceptcd"},{"code":"M05.532","system":"conceptcd"},{"code":"M05.539","system":"conceptcd"},{"code":"M05.54","system":"conceptcd"},{"code":"M05.541","system":"conceptcd"},{"code":"M05.542","system":"conceptcd"},{"code":"M05.549","system":"conceptcd"},{"code":"M05.55","system":"conceptcd"},{"code":"M05.551","system":"conceptcd"},{"code":"M05.552","system":"conceptcd"},{"code":"M05.559","system":"conceptcd"},{"code":"M05.56","system":"conceptcd"},{"code":"M05.561","system":"conceptcd"},{"code":"M05.562","system":"conceptcd"},{"code":"M05.569","system":"conceptcd"},{"code":"M05.57","system":"conceptcd"},{"code":"M05.571","system":"conceptcd"},{"code":"M05.572","system":"conceptcd"},{"code":"M05.579","system":"conceptcd"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('rheumatoid-arthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["polyneuropathy-rheumatoid-arthritis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["polyneuropathy-rheumatoid-arthritis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["polyneuropathy-rheumatoid-arthritis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
