class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father
person_a = Person('User', '1', None)
person_b = Person('User', '2', person_a)
person_c=Person('User', '3', person_b)

a = {'key1': 1,'key2': {'key3': 1,'key4': {'key5': 4}}}
b = {
'key1': 1,
'key2':
    {
    'key3': 1,
    'key4': 
        {
        'key5': 4,
        'user': person_b,
        'key6':5,
        }
        
    },
'key7':
    {
    'key8': 1,
    'key9': 
        {
        'key10': 4,
        'user2': person_b,
        'key11':5,
        },
    'key12': 
        {
        'key13': 4,
        'user3': person_c,
        'key14':5,
        }
    }
    
}

def depth(d,level):
    i=level+1
    
    if isinstance(d,Person):
        
        print("{} {}".format('first_name:',i))
        print("{} {}".format('last_name:',i))
        if d.father!=None:
            print("{} {}".format('father:',i))
            depth(d.father,i)
        else:
            print("{} {}".format('father:',i))
            
            
            
    elif isinstance(d,dict):
    
        for key in d:
            
            print("{}: {}".format(key,i))
            
            if isinstance(d[key],dict):
                depth(d[key],i)
                
            if isinstance(d[key],Person):
                print("{} {}".format(key,i))
                depth(d[key],i)
          
        
depth(b,0)   