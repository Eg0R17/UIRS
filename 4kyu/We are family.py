from itertools import combinations

isclose=lambda a, b:abs(a-b)<=10e-6
from copy import deepcopy

class Person:
    def __init__(self, name="", gender=None):
        self.name = name
        self.gender = gender

        self.parents = []
        self.children = []


class Family:
    def __init__(self):
        self.members = {}
    
    def male(self, name):
        if name not in self.members:
            person = Person(name, gender="male")
            self.members[name] = person
            return True
        
        if self.members[name].gender is "female":
            return False
        elif self.members[name].gender is None:
            self.members[name].gender = "male"
            self.deduce()
        return True
    
    def is_male(self, name):
        return name in self.members and self.members[name].gender == "male"
        
    def female(self, name):
        if name not in self.members:
            person = Person(name, gender="female")
            self.members[name] = person
            return True
        
        if self.members[name].gender is "male":
            return False
        elif self.members[name].gender is None:
            self.members[name].gender = "female"
            self.deduce()
        return True
    
    def is_female(self, name):
        return name in self.members and self.members[name].gender == "female"
    
    def set_parent_of(self, child_name, parent_name):
        if child_name == parent_name:
            return False
        
        if child_name not in self.members:
            self.members[child_name] = Person(child_name)
                    
        if parent_name not in self.members:
            self.members[parent_name] = Person(parent_name)

        child = self.members[child_name]
        parent = self.members[parent_name]
            
        if parent in child.parents:
            return True
        
        if len(child.parents) > 1 or child_name in self.get_ancestors_of(parent_name):
            return False
        elif child.parents:
            other_parent = child.parents[0]
        
        child.parents.append(parent)
        parent.children.append(child)
        
        if not self.test(parent.name):
            child.parents.pop()
            parent.children.pop()
            return False
        
        self.deduce()
        return True
        
    
    def get_children_of(self, name):
        if name in self.members:
            names = [child.name for child in self.members[name].children]
            names.sort()
            return names
        return []
    
    def get_parents_of(self, name):
        if name in self.members:
            names = [parent.name for parent in self.members[name].parents]
            names.sort()
            return names
        return []
    
    def get_ancestors_of(self, name):
        if name in self.members:
            me = self.members[name]
            names = sum([self.get_ancestors_of(p.name) for p in me.parents], [p.name for p in me.parents])
            return names
        return []
    
    def deduce(self):
        while True:
            update_count = 0
            for member in self.members.values():
                if len(member.parents) == 2:
                    p1, p2 = member.parents
                
                    if p1.gender is None and p2.gender is not None:
                        update_count += 1
                        p1.gender = "male" if p2.gender == "female" else "female"                
                    elif p2.gender is None and p1.gender is not None:
                        update_count += 1
                        p2.gender = "male" if p1.gender == "female" else "female"
            
            if not update_count:
                break
    
    def test(self, name, gender="male"):
        if name not in self.members:
            return True

        test_family = deepcopy(self)
        
        test_family.deduce()
        
        if test_family.members[name].gender is None:
            test_family.members[name].gender = gender
        test_family.deduce()
        
        for member in test_family.members.values():
            if len(member.parents) == 2:
                p1, p2 = member.parents
                
                if p1.gender == p2.gender and p1.gender is not None:
                    return False
        
        return True