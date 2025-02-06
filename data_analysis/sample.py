import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ucl_data.csv')

# winners_count = df.groupby('Winners')['Season'].count()
# winners_count
labels = df['Winners'].unique()
values = df['Winners'].value_counts().to_dict()
clubs = values.keys()
winners_count = list(values.values())
winners_count
my_clubs = list(clubs)
my_my_clubs = []
print(my_clubs)
for club in my_clubs:
    club = club[0] + club[len(club) - 1]
    my_my_clubs.append(club.upper())
    
my_my_clubs


# (club[len(club)//2 + 1] if  club[len(club)//2 + 1] == ' ' else club[len(club)//2])
plt.bar(my_my_clubs,winners_count,color = 'lightcoral',align='center',width= 0.6)

plt.xlabel('Winner Clubs')
plt.ylabel('Trophies Won')
plt.title('Champions League Winners Count')

plt.show()
