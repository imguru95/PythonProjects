qualities = ["Progressive", "Perfectionist", "Traveller", "Foodie", "Extrovert", "Workaholic", "Ambitious", "Fitness-freak", "Book-reader", "Writer", "Spiritual"]
print("List of qualities:")
for i in range(len(qualities)):
    print(str(i+1) + ") " + qualities[i])
    
m1 = [{"Progressive":2, "Perfectionist":9, "Traveller":7, "Foodie":8, "Fitness-freak":5}, {"Progressive":7, "Perfectionist":8, "Traveller":7, "Writer":9, "Fitness-freak":9, "Workaholic":7}]
m2 = [{"Progressive":8, "Perfectionist":6, "Traveller":1, "Writer":4, "Book-reader":9}, {"Ambitious":8, "Extrovert":9, "Foodie":8, "Fitness-freak":4, "Workaholic":6}]
m3 = [{"Progressive":4, "Perfectionist":8, "Traveller":7, "Writer":8, "Foodie":6, "Ambitious":10}, {"Ambitious":8, "Spiritual":8, "Foodie":8, "Fitness-freak":9, "Workaholic":3}]
m4 = [{"Progressive":8, "Traveller":2, "Writer":8, "Workaholic":6, "Ambitious":3}, {"Perfectionist":9, "Progressive":7, "Foodie":2, "Fitness-freak":9, "Workaholic":1}]

f1 = [{"Workaholic":9, "Spiritual":8, "Book-reader":7, "Progressive":6, "Traveller":5}, {"Workaholic":3, "Spiritual":8, "Progressive":9, "Foodie":7}]
f2 = [{"Spiritual":10, "Progressive":2, "Foodie":8, "Writer":7, "Traveller":8}, {"Fitness-freak":8, "Extrovert":9, "Foodie":8, "Spiritual":8, "Ambitious":7}]
f3 = [{"Spiritual":1, "Progressive":9, "Foodie":2, "Book-reader":9, "Traveller":9}, {"Fitness-freak":8, "Extrovert":9, "Foodie":8, "Spiritual":1, "Ambitious":8, "Perfectionist":7}]
f4 = [{"Spiritual":9, "Progressive":9, "Fitness-freak":2, "Book-reader":2, "Traveller":9}, {"Traveller":8, "Spiritual":9, "Progressive":7, "Ambitious":2, "Perfectionist":9}]

male_dict = {0:m1, 1:m2, 2:m3, 3:m4}
female_dict = {0:f1, 1:f2, 2:f3, 3:f4}
num_male = len(male_dict)
num_female = len(female_dict)
print("\nNo. of males = {}\nNo. of females = {}".format(num_male, num_female))
for i in range(len(male_dict.values())):
    print("\nSummary of male {}'s qualities:".format(i+1))
    print("Quality                            Rating")
    print("-----------------------------------------")
    for quality in qualities:
        if quality in male_dict[i][0]:
            print(quality.ljust(25) + "|             " + str(male_dict[i][0][quality]))
        else:
            print(quality.ljust(25) + "|             " + "0")
    print("\nSummary of male {}'s desired qualities:".format(i+1))
    print("Quality                            Rating")
    print("-----------------------------------------")
    for quality in qualities:
        if quality in male_dict[i][1]:
            print(quality.ljust(25) + "|             " + str(male_dict[i][1][quality]))
        else:
            print(quality.ljust(25) + "|             " + "0")
    print("\nSummary of female {}'s qualities:".format(i+1))
    print("Quality                            Rating")
    print("-----------------------------------------")
    for quality in qualities:
        if quality in female_dict[i][0]:
            print(quality.ljust(25) + "|             " + str(female_dict[i][0][quality]))
        else:
            print(quality.ljust(25) + "|             " + "0")
    print("\nSummary of female {}'s desired qualities:".format(i+1))
    print("Quality                            Rating")
    print("-----------------------------------------")
    for quality in qualities:
        if quality in female_dict[i][1]:
            print(quality.ljust(25) + "|             " + str(female_dict[i][1][quality]))
        else:
            print(quality.ljust(25) + "|             " + "0")

#female to male compatibility scores
male_pref_record = []
for i in range(num_male):
    male_pref_record_dict = {}
    for j in range(num_female):
        print("-----------------------------------------o-----------------------------------------o-----------------------------------------")
        print("\n")
        print("Female {} to male {}'s match(How much is Female {} compatible to male {}?)".format(j+1, i+1, j+1, i+1), end='')
        sum = 0
        for quality in qualities:
            if quality in male_dict[i][1]:
                if quality in female_dict[j][0]:
                    sum = sum + abs(female_dict[j][0][quality] - male_dict[i][1][quality])
                else:
                    sum = sum + abs(male_dict[i][1][quality])
            else:
                if quality in female_dict[j][0]:
                    sum = sum + abs(female_dict[j][0][quality])
        male_pref_record_dict[j+1] = sum
        print(" : Match variance = ", sum)
    male_pref_record_dict_sorted = dict(sorted(male_pref_record_dict.items(), key=lambda item: item[1]))
    male_pref_record.append(male_pref_record_dict_sorted)

#male to female compatibility scores
female_pref_record = []
for i in range(num_female):
    female_pref_record_dict = {}
    for j in range(num_male):
        print("-----------------------------------------o-----------------------------------------o-----------------------------------------")
        print("\n")
        print("Male {} to female {}'s match(How much is male {} compatible to female {}?)".format(j+1, i+1, j+1, i+1), end='')
        sum = 0
        for quality in qualities:
            if quality in female_dict[i][1]:
                if quality in male_dict[j][0]:
                    sum = sum + abs(male_dict[j][0][quality] - female_dict[i][1][quality])
                else:
                    sum = sum + abs(female_dict[i][1][quality])
            else:
                if quality in male_dict[j][0]:
                    sum = sum + abs(male_dict[j][0][quality])
        female_pref_record_dict[j+1] = sum
        print(" : Match variance = ", sum)
    female_pref_record_dict_sorted = dict(sorted(female_pref_record_dict.items(), key=lambda item: item[1]))
    female_pref_record.append(female_pref_record_dict_sorted)

matches_made = {}
print("-----------------------------------------o-----------------------------------------o-----------------------------------------")
print("Gale-Shapley Algorithm for Stable Matching")
print("-----------------------------------------o-----------------------------------------o-----------------------------------------")
print("Male set is the proposing set")
print("Note that the matching is optimal from the proposers' perspective")
#Gale-Shapley Algorithm
a = 1
itr = 0
while len(matches_made) != len(male_pref_record):
    if a > len(male_pref_record):
        a = 1
    if (not a in matches_made.keys()):
        f_match = (list(male_pref_record[a-1].keys()))[itr]
        #checking if f_match exists in values of matches_made dictionary
        if (not f_match in matches_made.values()):
            matches_made[a] = f_match
        else:
            #fetch the male to whom f_match is matched to
            m_match = {v:k for k, v in matches_made.items()}[f_match]
            ind_1 = list(female_pref_record[f_match-1].keys()).index(m_match)
            ind_2 = list(female_pref_record[f_match-1].keys()).index(a)
            #if the current match is a better option for f_match
            if ind_1 > ind_2:
                matches_made[a] = f_match
                #delete from matches_made, the match given to m_match and make him matchless
                matches_made.pop(m_match, None)
                a = a + 1
            else:
                itr = itr + 1
    else:
        a = a + 1

print("*********************Summary of matches made*********************")
for male, female in sorted(matches_made.items()):
    print("Male", male, "marries female", female)
