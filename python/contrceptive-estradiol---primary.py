# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"11910","system":"gprdproduct"},{"code":"12631","system":"gprdproduct"},{"code":"13248","system":"gprdproduct"},{"code":"13810","system":"gprdproduct"},{"code":"14601","system":"gprdproduct"},{"code":"14670","system":"gprdproduct"},{"code":"14977","system":"gprdproduct"},{"code":"15886","system":"gprdproduct"},{"code":"15987","system":"gprdproduct"},{"code":"16110","system":"gprdproduct"},{"code":"18569","system":"gprdproduct"},{"code":"18823","system":"gprdproduct"},{"code":"19131","system":"gprdproduct"},{"code":"21733","system":"gprdproduct"},{"code":"23211","system":"gprdproduct"},{"code":"23218","system":"gprdproduct"},{"code":"23897","system":"gprdproduct"},{"code":"25263","system":"gprdproduct"},{"code":"2769","system":"gprdproduct"},{"code":"29499","system":"gprdproduct"},{"code":"31528","system":"gprdproduct"},{"code":"40512","system":"gprdproduct"},{"code":"40618","system":"gprdproduct"},{"code":"40650","system":"gprdproduct"},{"code":"42510","system":"gprdproduct"},{"code":"443","system":"gprdproduct"},{"code":"45059","system":"gprdproduct"},{"code":"57264","system":"gprdproduct"},{"code":"6596","system":"gprdproduct"},{"code":"6686","system":"gprdproduct"},{"code":"6716","system":"gprdproduct"},{"code":"7699","system":"gprdproduct"},{"code":"7776","system":"gprdproduct"},{"code":"7814","system":"gprdproduct"},{"code":"8176","system":"gprdproduct"},{"code":"8482","system":"gprdproduct"},{"code":"8718","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('contrceptive-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["contrceptive-estradiol---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["contrceptive-estradiol---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["contrceptive-estradiol---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
