# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Part 1 
scored_first = "Ruud Gullit"
scored_second = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = scored_first + " " + str(goal_0) + ', ' + scored_second + " " + str(goal_1)


report = f'{scored_first}' + ' ' + 'scored in the' + ' ' + f'{goal_0}' + 'nd minute' + '\n' + f'{scored_second}' + ' '+ 'scored in the'+' '+ f'{goal_1}'+ 'th minute'
#print(report)
# Part 2
# 1.
player = "Ruud Gullit"
# 2.
first_name = player[:player.find(' ')]
# 3.
last_name_len = len((player)[player.find(' '):-1])
# 4.
name_short = player[0] + '. ' + player[-last_name_len:]
# 5.
chant = (len(first_name) * (first_name + "!" + " "))[:-1]
# 6 
good_chant = (chant[-1] != ' ')

print(good_chant)