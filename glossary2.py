glossary = {
    
    
    
    
    
    
    
    }
glossary['tuple'] = 'data stored in a tuple cannot be changed'
glossary['list'] = 'items are mainly stored in list'
glossary['keywords'] = 'they are permanent words for the programming language'
glossary['python'] = 'is an open source language'
glossary['GUI'] = 'graphical users interface'
print (glossary)
 
for v,l in glossary.items():
	print('\n'+v.title() + ': ' + l.lower())

glossary['dictionary']= 'is a collection of key pairs items' 
for v,l in glossary.items():
	print('\n'+v.title() + ': ' + l.lower())
