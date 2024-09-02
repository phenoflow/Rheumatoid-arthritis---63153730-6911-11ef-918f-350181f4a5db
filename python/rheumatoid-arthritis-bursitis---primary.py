# phekb, 2024.

import sys, csv, re

codes = [{"code":"M06.2","system":"conceptcd"},{"code":"M06.21","system":"conceptcd"},{"code":"M06.211","system":"conceptcd"},{"code":"M06.212","system":"conceptcd"},{"code":"M06.22","system":"conceptcd"},{"code":"M06.221","system":"conceptcd"},{"code":"M06.222","system":"conceptcd"},{"code":"M06.23","system":"conceptcd"},{"code":"M06.231","system":"conceptcd"},{"code":"M06.232","system":"conceptcd"},{"code":"M06.24","system":"conceptcd"},{"code":"M06.241","system":"conceptcd"},{"code":"M06.242","system":"conceptcd"},{"code":"M06.25","system":"conceptcd"},{"code":"M06.251","system":"conceptcd"},{"code":"M06.252","system":"conceptcd"},{"code":"M06.26","system":"conceptcd"},{"code":"M06.261","system":"conceptcd"},{"code":"M06.262","system":"conceptcd"},{"code":"M06.27","system":"conceptcd"},{"code":"M06.271","system":"conceptcd"},{"code":"M06.272","system":"conceptcd"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('rheumatoid-arthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["rheumatoid-arthritis-bursitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["rheumatoid-arthritis-bursitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["rheumatoid-arthritis-bursitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
