import yaml  
f = open('test.yaml')  
x = yaml.load(f)    
print x.values()  