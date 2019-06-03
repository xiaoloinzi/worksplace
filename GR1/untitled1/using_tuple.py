#encoding=utf-8
zoo = ('wolf','elephant','penguin')
print("number of animals in the zoo is",len(zoo))
new_zoo = ('monkey','dolphin',zoo)
print("number oof animals in the new zoo is",len(new_zoo))
print("all animals in new zoo are ",new_zoo)
print("animals brought from old zoo are",new_zoo[2])
print("Last animal brought from old zoo are",new_zoo[2][2])