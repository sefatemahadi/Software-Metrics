class Class(object):
    def __init__(self,name):
        self.name =name
        self.methodCount =0
        self.depth =0
        self.children =0
        self.methods =[]

classes =dict()
lastClass =None

fileName =open('Enter file name\n')

file =open(fileName,'r')

#Weighted Average Method

for line in file:
    if 'class' in line:
        if lastClass != None:
            # classes.append(last_class)
            classes[lastClass.name] =lastClass
        line =line[line.index(' ')+1:]
        lastClass =Class(line[:line.index('(')])
        continue

    if 'def' in line:
        lastClass.methodCount+=1

classes[lastClass.name] = lastClass
file.close()
print(len(classes.keys()))

#print
for eachClass in classes.keys():
    classObject =classes[eachClass]
    print(classObject.name,classObject.methodCount)

#Count depth of inheritance

classes['object'] =Class('object')

file =open(fileName,'r')
for line in file:
    if 'class' in line:
        line =line[line.index(' ')+1:]
        className =line[:line.index('(')]
        inheritedClassName =line[line.index('(')+1:line.index(')')]
        print(className,inheritedClassName)
        classObject =classes[className]
        inheritedClassObject =classes[inheritedClassName]
        inheritedClassObject.children+=1
        classObject.depth=inheritedClassObject.depth+1
file.close()
maxDepth =-100
for eachClass in classes.keys():
    classObject =classes[eachClass]
    if maxDepth <= classObject.depth:
        maxDepth =classObject.depth

print('depth of Inheritance:',maxDepth)

#number of immediate sub-classes of a class

for eachClass in classes.keys():
    classObject =classes[eachClass]
    print(classObject.name,classObject.children)

#Total CK 4 ck metrics done. 2 left.
# Mood left.