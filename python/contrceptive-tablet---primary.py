# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"14459","system":"gprdproduct"},{"code":"1752","system":"gprdproduct"},{"code":"19551","system":"gprdproduct"},{"code":"1988","system":"gprdproduct"},{"code":"3436","system":"gprdproduct"},{"code":"3538","system":"gprdproduct"},{"code":"36829","system":"gprdproduct"},{"code":"3693","system":"gprdproduct"},{"code":"37073","system":"gprdproduct"},{"code":"44046","system":"gprdproduct"},{"code":"44278","system":"gprdproduct"},{"code":"4964","system":"gprdproduct"},{"code":"5576","system":"gprdproduct"},{"code":"56311","system":"gprdproduct"},{"code":"56539","system":"gprdproduct"},{"code":"5862","system":"gprdproduct"},{"code":"59503","system":"gprdproduct"},{"code":"8103","system":"gprdproduct"},{"code":"9119","system":"gprdproduct"},{"code":"937","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('contrceptive-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["contrceptive-tablet---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["contrceptive-tablet---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["contrceptive-tablet---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
