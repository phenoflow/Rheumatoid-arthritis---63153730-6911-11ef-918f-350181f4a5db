# phekb, 2024.

import sys, csv, re

codes = [{"code":"M05.6","system":"conceptcd"},{"code":"M05.60","system":"conceptcd"},{"code":"M05.61","system":"conceptcd"},{"code":"M05.611","system":"conceptcd"},{"code":"M05.612","system":"conceptcd"},{"code":"M05.619","system":"conceptcd"},{"code":"M05.62","system":"conceptcd"},{"code":"M05.621","system":"conceptcd"},{"code":"M05.622","system":"conceptcd"},{"code":"M05.629","system":"conceptcd"},{"code":"M05.63","system":"conceptcd"},{"code":"M05.631","system":"conceptcd"},{"code":"M05.632","system":"conceptcd"},{"code":"M05.639","system":"conceptcd"},{"code":"M05.64","system":"conceptcd"},{"code":"M05.641","system":"conceptcd"},{"code":"M05.642","system":"conceptcd"},{"code":"M05.649","system":"conceptcd"},{"code":"M05.65","system":"conceptcd"},{"code":"M05.651","system":"conceptcd"},{"code":"M05.652","system":"conceptcd"},{"code":"M05.659","system":"conceptcd"},{"code":"M05.66","system":"conceptcd"},{"code":"M05.661","system":"conceptcd"},{"code":"M05.662","system":"conceptcd"},{"code":"M05.669","system":"conceptcd"},{"code":"M05.67","system":"conceptcd"},{"code":"M05.671","system":"conceptcd"},{"code":"M05.672","system":"conceptcd"},{"code":"M05.679","system":"conceptcd"},{"code":"M05.69","system":"conceptcd"},{"code":"M05.7","system":"conceptcd"},{"code":"M05.70","system":"conceptcd"},{"code":"M05.71","system":"conceptcd"},{"code":"M05.711","system":"conceptcd"},{"code":"M05.712","system":"conceptcd"},{"code":"M05.719","system":"conceptcd"},{"code":"M05.72","system":"conceptcd"},{"code":"M05.721","system":"conceptcd"},{"code":"M05.722","system":"conceptcd"},{"code":"M05.729","system":"conceptcd"},{"code":"M05.73","system":"conceptcd"},{"code":"M05.731","system":"conceptcd"},{"code":"M05.732","system":"conceptcd"},{"code":"M05.739","system":"conceptcd"},{"code":"M05.74","system":"conceptcd"},{"code":"M05.741","system":"conceptcd"},{"code":"M05.742","system":"conceptcd"},{"code":"M05.749","system":"conceptcd"},{"code":"M05.75","system":"conceptcd"},{"code":"M05.751","system":"conceptcd"},{"code":"M05.752","system":"conceptcd"},{"code":"M05.759","system":"conceptcd"},{"code":"M05.76","system":"conceptcd"},{"code":"M05.761","system":"conceptcd"},{"code":"M05.762","system":"conceptcd"},{"code":"M05.769","system":"conceptcd"},{"code":"M05.77","system":"conceptcd"},{"code":"M05.771","system":"conceptcd"},{"code":"M05.772","system":"conceptcd"},{"code":"M05.779","system":"conceptcd"},{"code":"M05.79","system":"conceptcd"},{"code":"714.2","system":"conceptcd"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('rheumatoid-arthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["systemic-rheumatoid-arthritis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["systemic-rheumatoid-arthritis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["systemic-rheumatoid-arthritis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
