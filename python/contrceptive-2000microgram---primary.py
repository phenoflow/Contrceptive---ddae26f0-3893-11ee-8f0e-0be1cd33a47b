# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"1354","system":"gprdproduct"},{"code":"17756","system":"gprdproduct"},{"code":"22603","system":"gprdproduct"},{"code":"2354","system":"gprdproduct"},{"code":"25124","system":"gprdproduct"},{"code":"31902","system":"gprdproduct"},{"code":"33098","system":"gprdproduct"},{"code":"47281","system":"gprdproduct"},{"code":"58642","system":"gprdproduct"},{"code":"59383","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('contrceptive-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["contrceptive-2000microgram---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["contrceptive-2000microgram---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["contrceptive-2000microgram---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
