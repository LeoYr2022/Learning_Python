
# Python将不能修改的值称为不可变的 ，而不可变的列表被称为元组 。
dimensions = (200, 50) ;#Pay attention this is () not []
print(dimensions[0])
print(dimensions[1])

#TypeError: 'tuple' object does not support item assignment
# dimensions[0] = 250 ;

print("\n******************** Traverse the tuple ****************************")
dimensions = (200, 50)
for dimension in dimensions: ### {{{
    print(dimension)
### }}}

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100) #虽然不能修改元组的元素，但可以给存储元组的变量赋值。
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
