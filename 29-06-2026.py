# # Memory management
x=10
print(x)
print(id(x))
x=20
print(x)
print(id(x))
x=x+20
print(x)
print(id(x))

# shallow copy
org_msgs=[['hi','how are you'],['wyd','hello']]
print(org_msgs)

import copy
shal_cpy=copy.copy(org_msgs)
shal_cpy[0][1]='ajay'
print(shal_cpy)
print(org_msgs)

#deep copy
org_msgs1=[['hi','how are you'],['wyd','hello']]
print(org_msgs1)

import copy
deep_cpy=copy.deepcopy(org_msgs1)
deep_cpy[0][1]='ajay'
print(deep_cpy)
print(org_msgs1)