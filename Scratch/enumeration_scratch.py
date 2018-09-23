# fun with enumeration
import code
fruits = ['apple','banana','orange','grape']
longest_fruit = None
longest_fruit_position = None

# enumerate returns a tuple as [(1, 'apple')]
# example includes [(1, 'apple')] ## 1 returns because we feed it a starting position of 1
for fruit_postion, fruit in enumerate(fruits,1):
    print fruit, fruit_postion
    if fruit > longest_fruit:
        longest_fruit = fruit
        longest_fruit_position = fruit_postion

code.interact(local=locals())