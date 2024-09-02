# phekb, 2024.

import sys, csv, re

codes = [{"code":"M05.00","system":"conceptcd"},{"code":"M05.019","system":"conceptcd"},{"code":"M05.029","system":"conceptcd"},{"code":"M05.039","system":"conceptcd"},{"code":"M05.049","system":"conceptcd"},{"code":"M05.059","system":"conceptcd"},{"code":"M05.069","system":"conceptcd"},{"code":"M05.079","system":"conceptcd"},{"code":"M05.10","system":"conceptcd"},{"code":"M05.119","system":"conceptcd"},{"code":"M05.129","system":"conceptcd"},{"code":"M05.139","system":"conceptcd"},{"code":"M05.149","system":"conceptcd"},{"code":"M05.159","system":"conceptcd"},{"code":"M05.169","system":"conceptcd"},{"code":"M05.179","system":"conceptcd"},{"code":"M05.80","system":"conceptcd"},{"code":"M05.819","system":"conceptcd"},{"code":"M05.829","system":"conceptcd"},{"code":"M05.839","system":"conceptcd"},{"code":"M05.849","system":"conceptcd"},{"code":"M05.859","system":"conceptcd"},{"code":"M05.869","system":"conceptcd"},{"code":"M05.879","system":"conceptcd"},{"code":"M05.9","system":"conceptcd"},{"code":"M06.00","system":"conceptcd"},{"code":"M06.019","system":"conceptcd"},{"code":"M06.029","system":"conceptcd"},{"code":"M06.039","system":"conceptcd"},{"code":"M06.049","system":"conceptcd"},{"code":"M06.059","system":"conceptcd"},{"code":"M06.069","system":"conceptcd"},{"code":"M06.079","system":"conceptcd"},{"code":"M06.20","system":"conceptcd"},{"code":"M06.219","system":"conceptcd"},{"code":"M06.229","system":"conceptcd"},{"code":"M06.239","system":"conceptcd"},{"code":"M06.249","system":"conceptcd"},{"code":"M06.259","system":"conceptcd"},{"code":"M06.269","system":"conceptcd"},{"code":"M06.279","system":"conceptcd"},{"code":"M06.30","system":"conceptcd"},{"code":"M06.319","system":"conceptcd"},{"code":"M06.329","system":"conceptcd"},{"code":"M06.339","system":"conceptcd"},{"code":"M06.349","system":"conceptcd"},{"code":"M06.359","system":"conceptcd"},{"code":"M06.369","system":"conceptcd"},{"code":"M06.379","system":"conceptcd"},{"code":"M06.8","system":"conceptcd"},{"code":"M06.80","system":"conceptcd"},{"code":"M06.81","system":"conceptcd"},{"code":"M06.811","system":"conceptcd"},{"code":"M06.812","system":"conceptcd"},{"code":"M06.819","system":"conceptcd"},{"code":"M06.82","system":"conceptcd"},{"code":"M06.821","system":"conceptcd"},{"code":"M06.822","system":"conceptcd"},{"code":"M06.829","system":"conceptcd"},{"code":"M06.83","system":"conceptcd"},{"code":"M06.831","system":"conceptcd"},{"code":"M06.832","system":"conceptcd"},{"code":"M06.839","system":"conceptcd"},{"code":"M06.84","system":"conceptcd"},{"code":"M06.841","system":"conceptcd"},{"code":"M06.842","system":"conceptcd"},{"code":"M06.849","system":"conceptcd"},{"code":"M06.85","system":"conceptcd"},{"code":"M06.851","system":"conceptcd"},{"code":"M06.852","system":"conceptcd"},{"code":"M06.859","system":"conceptcd"},{"code":"M06.86","system":"conceptcd"},{"code":"M06.861","system":"conceptcd"},{"code":"M06.862","system":"conceptcd"},{"code":"M06.869","system":"conceptcd"},{"code":"M06.87","system":"conceptcd"},{"code":"M06.871","system":"conceptcd"},{"code":"M06.872","system":"conceptcd"},{"code":"M06.879","system":"conceptcd"},{"code":"M06.9","system":"conceptcd"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('rheumatoid-arthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["rheumatoid-arthritis-specified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["rheumatoid-arthritis-specified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["rheumatoid-arthritis-specified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
