# define the documents and their categories
import pandas as pd
documents = [
    {'text': 'lemon banana banana plum plum pear', 'category': 'P'},
    {'text': 'pear banana banana plum banana plum', 'category': 'P'},
    {'text': 'lemon banana lemon plum lemon', 'category': 'P'},
    {'text': 'lemon banana lemon lemon plum plum lemon', 'category': 'P'},
    {'text': 'banana lemon pear banana', 'category': 'nP'},
    {'text': 'lemon banana banana lemon', 'category': 'nP'},
    {'text': 'banana lemon lemon lemon', 'category': 'nP'},
    {'text': 'lemon lemon', 'category': 'nP'}
]


word_counts = {}
category_counts = {'P': 0, 'nP': 0}
processor_Wcount = 0
Nprocessor_Wcount = 0

unique_count = []

for doc in documents:
    words = doc['text'].split()
    category = doc['category']
    category_counts[category] += 1
    
    unique_count.extend(words)
    if doc['category'] == 'P':
        processor_Wcount+=len(words)
    else:
        Nprocessor_Wcount+=len(words)
    
    for word in words:
        if word not in word_counts:
            word_counts[word] = {'P': 0, 'nP': 0, 'P(C)Num': 0, 'P(C)Den': 0, 'P(C)': 0, 'P(nC)Num': 0, 'P(nC)Den': 0, 'P(nC)': 0,}
        word_counts[word][category] += 1

unique_count = len(set(unique_count))

word_counts = pd.DataFrame(word_counts).T

word_counts['P(C)'] = (word_counts['P'] + 1)/(processor_Wcount + unique_count)
word_counts['P(C)Num'] = word_counts['P'] + 1
word_counts['P(C)Den'] = processor_Wcount + unique_count


word_counts['P(nC)'] = (word_counts['nP'] + 1)/(Nprocessor_Wcount + unique_count)
word_counts['P(nC)Num'] = word_counts['nP'] + 1
word_counts['P(nC)Den'] = Nprocessor_Wcount + unique_count




new_document = 'banana lemon banana'.split()

p_processor = category_counts['P'] / len(documents)
p_not_processor = category_counts['nP'] / len(documents)
p_new_processor = p_processor
p_new_not_processor = p_not_processor

PC = 1
PnC = 1

PCDen = 2
PnCDen = 2

for i in new_document:
    PC*=word_counts['P(C)Num'].loc[i]
    PCDen*=word_counts['P(C)Den'].loc[i]
    PnC*=word_counts['P(nC)Num'].loc[i]
    PnCDen*=word_counts['P(nC)Den'].loc[i]
    
print(PC, " / ", PCDen)

print(PnC, " / ", PnCDen)




# for word in new_document:
#     if word in word_counts:
#         p_new_processor *= (word_counts[word]['processor'] + 1) / (sum(word_counts[word].values()) + len(word_counts))
#         p_new_not_processor *= (word_counts[word]['not processor'] + 1) / (sum(word_counts[word].values()) + len(word_counts))
#     else:
#         p_new_processor *= 1 / (sum(word_counts[word].values()) + len(word_counts))
#         p_new_not_processor *= 1 / (sum(word_counts[word].values()) + len(word_counts))


# if p_new_processor > p_new_not_processor:
#     print('document 7 is a member of the processor category')
# else:
#     print('document 7 is not a member of the processor category')
# print('P(processor/document 7) =', p_new_processor * p_processor)
# print('P(not processor/document 7) =', p_new_not_processor * p_not_processor)
