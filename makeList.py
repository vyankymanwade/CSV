import csv

htmlOutput = ''
names = []

with open('./contributors.csv','r') as dataFile:
    csvReader = csv.DictReader(dataFile,delimiter=',')
    # the first 2 lines contain unwanted data so we are ignoring this lines

    next(csvReader)

    for line in csvReader:
        if line['FirstName'] == 'No Reward':
            break
        names.append('{} {}'.format(line['FirstName'],line['LastName']))

htmlOutput += f'<p>There are currently {len(names)} public contributors. Thank you!!</p>'
htmlOutput += '\n<ul>'

for name in names:
    htmlOutput += f'\n\t<li>{name}</li>'

htmlOutput += '\n<ul>'

print(htmlOutput)