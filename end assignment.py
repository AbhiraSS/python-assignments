
feedback_data = {
'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
'Feedback': [
' Very GOOD Service!!!',
'poor support, not happy ',
'GREAT experience! will come again.',
'okay okay...',
' not BAD',
'Excellent care, excellent staff!',
'good food and good ambience!',
'Poor response and poor handling of issue',
'Satisfied. But could be better.',
'Good support... quick service.'
],
'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


n=int(input("How many more feedbacks do you want to add?"))

for i in range(n):
    print("Enter details for feedback :",i+1)
    name=input("Enter name :")
    feedback=input("Enter feedback :")

    while True:
        rating=int(input("Enter rating (1:5):"))

        if 1<=rating<=5:
            break
        else:
            print("invalid rating!")

    S_No= len(feedback_data['S_No'])+1

    feedback_data['S_No'].append(S_No)
    feedback_data['Name'].append(name)
    feedback_data['Rating'].append(rating)
    feedback_data['Feedback'].append(feedback)




for i in range (len(feedback_data['Feedback'])):
    text=feedback_data['Feedback'][i]

    text = text.replace('.','')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace('?', '')

    text=' '.join(text.split())
    text=text.lower()

    feedback_data['Feedback'][i]=text



def count_word_in_feedbacks(word):
    count=0
    for feedback in feedback_data['Feedback']:
        words=feedback.split()

        if word.lower() in words:
            count+=1
    return count

print("\n== WORD COUNT INSIGHTS ==")

print("Feedbacks containing 'good':", count_word_in_feedbacks('good'))
print("Feedbacks containing 'poor':", count_word_in_feedbacks('poor'))
print("Feedbacks containing 'excellent':",count_word_in_feedbacks('excellent'))


print(feedback_data)

average_rating= sum(feedback_data['Rating'])/len(feedback_data['Rating'])
print("Average rating:",average_rating)



longest_feedback = ''
maximum_words = 0

for feedback in feedback_data['Feedback']:

    word_count = len(feedback.split())

    if word_count > maximum_words:
        maximum_words = word_count
        longest_feedback = feedback

print("\n==== LONGEST FEEDBACK ====")

print("Feedback:", longest_feedback)
print("Word Count:", maximum_words)



unique_words = set()
for feedback in feedback_data['Feedback']:

    words = feedback.split()
    for word in words:
        unique_words.add(word)

print("\n==== UNIQUE WORDS ===")
print(sorted(unique_words))



sorted_feedbacks = sorted(
    zip(feedback_data['S_No'],
        feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']),
   
    key=lambda item: item[3],
    reverse=True)

print("\n==== FEEDBACKS SORTED BY RATING ====")
for item in sorted_feedbacks:
    print(item)

