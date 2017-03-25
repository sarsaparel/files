
import csv

#dictionary = [{"Печаль" : "это место, куда приходят корабли", "Ураган" : "это то, что мы кладем себе в чай", "Курага" : "отрывает машины от земли"}]

dictionary = [{'short': 'dict', 'long': 'dictionary'}]

with open('export.csv', 'w', encoding='utf-8') as f:

    #fields = ["Печаль", "Ураган", "Курага"]
    fields = ['short', 'long']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for a in dictionary:
        writer.writerow(a)


# при использовании кириллицы invalid syntax, а в файле csv краказябры 