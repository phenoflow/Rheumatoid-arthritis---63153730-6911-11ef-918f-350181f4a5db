# phekb, 2024.

import sys, csv, re

codes = [{"code":"M05.2","system":"conceptcd"},{"code":"M05.20","system":"conceptcd"},{"code":"M05.21","system":"conceptcd"},{"code":"M05.211","system":"conceptcd"},{"code":"M05.212","system":"conceptcd"},{"code":"M05.219","system":"conceptcd"},{"code":"M05.22","system":"conceptcd"},{"code":"M05.221","system":"conceptcd"},{"code":"M05.222","system":"conceptcd"},{"code":"M05.229","system":"conceptcd"},{"code":"M05.23","system":"conceptcd"},{"code":"M05.231","system":"conceptcd"},{"code":"M05.232","system":"conceptcd"},{"code":"M05.239","system":"conceptcd"},{"code":"M05.24","system":"conceptcd"},{"code":"M05.241","system":"conceptcd"},{"code":"M05.242","system":"conceptcd"},{"code":"M05.249","system":"conceptcd"},{"code":"M05.25","system":"conceptcd"},{"code":"M05.251","system":"conceptcd"},{"code":"M05.252","system":"conceptcd"},{"code":"M05.259","system":"conceptcd"},{"code":"M05.26","system":"conceptcd"},{"code":"M05.261","system":"conceptcd"},{"code":"M05.262","system":"conceptcd"},{"code":"M05.269","system":"conceptcd"},{"code":"M05.27","system":"conceptcd"},{"code":"M05.271","system":"conceptcd"},{"code":"M05.272","system":"conceptcd"},{"code":"M05.279","system":"conceptcd"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('rheumatoid-arthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["rheumatoid-arthritis-vasculitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["rheumatoid-arthritis-vasculitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["rheumatoid-arthritis-vasculitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
