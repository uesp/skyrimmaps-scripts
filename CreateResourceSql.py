import csv
import collections
import os.path


resources = []

with open('d:\\skyrimmaps\\resources\\skyrimresources.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        resources.append(row)
    
#for row in resources:
#    print row[0]

UniqueResources = {}
FormIDs = {}

for row in resources:
    FormIDs[row[0]] = row[1]
    if row[2] in UniqueResources:
        UniqueResources[row[2]].append(row[0])
    else:
        UniqueResources[row[2]] = []
        UniqueResources[row[2]].append(row[0])

UniqueResources = collections.OrderedDict(sorted(UniqueResources.items()))
       
for Name, EditorIDList in UniqueResources.iteritems():
    print Name, len(EditorIDList)
    ResourceCount = [[0 for x in xrange(94)] for x in xrange(119)]
    FilesLoaded = 0

    for i in range(0, len(EditorIDList)):
        CSVFilename = 'd:\\skyrimmaps\\resources\\all\\' + EditorIDList[i] + '.csv'

        if not os.path.isfile(CSVFilename):
            print '\tFile missing: ', CSVFilename
            continue
        
        print '\tLoading ', CSVFilename, '...'
        FilesLoaded += 1
        
        with open(CSVFilename, 'rb') as f:
            reader = csv.reader(f)
            y = 0
            for row in reader:
                x = 0
                for item in row:
                    if i == 0:
                        ResourceCount[y][x] = int(item)
                    else:
                        ResourceCount[y][x] += int(item)
                    x += 1
                y += 1

        if FilesLoaded == 0:
            print "\tSkipping...no files loaded for resource!"
            continue
       
        CSVFilename = 'd:\\skyrimmaps\\resources\\combine\\' + Name + '.csv'
        
        with open(CSVFilename, 'wb') as f:
            for row in ResourceCount:
                for j, item in enumerate(row):
                    if j : f.write(",")
                    f.write(str(item))
                    
                f.write("\n")

        SQLFilename = 'd:\\skyrimmaps\\resources\\sql\\' + Name + '.sql'
        
        with open(SQLFilename, 'wb') as f:
            f.write("INSERT INTO cellresource(formid, editorid, name, data) VALUES (")
            f.write("CAST(");
            f.write(str(FormIDs[EditorIDList[0]]));
            f.write(" AS UNSIGNED), '");
            f.write(EditorIDList[0]);
            f.write("', \"");
            f.write(Name);
            f.write("\", '[");
                    
            for m, row in enumerate(ResourceCount):
                if m : f.write(",\n")
                f.write("[")
                
                for j, item in enumerate(row):
                    if j : f.write(",")
                    f.write(str(item))
                    
                f.write("]")
            f.write("]');\n")
                    
    
for Name, EditorIDList in UniqueResources.iteritems():
    print Name, ",", EditorIDList[0]

for Name, EditorIDList in UniqueResources.iteritems():
    if Name == '': continue
    print "<option value='{0}'>{1}</option>".format(EditorIDList[0], Name)
