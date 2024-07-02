#factwise_question_1

# If the numbers to are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


count=0
count+=(len("one")*(100+90+1))
count+=(len("two")*(100+90))
count+=(len("three")*(100+90))
count+=(len("four")*(100+90))
count+=(len("five")*(100+90))
count+=(len("six")*(100+90))
count+=(len("seven")*(100+90))
count+=(len("eight")*(100+90))
count+=(len("nine")*(100+90))

count+=(len("ten")*10)
count+=(len("twenty")*100)
count+=(len("thirty")*100)
count+=(len("fourty")*100)
count+=(len("fifty")*100)
count+=(len("sixty")*100)
count+=(len("seventy")*100)
count+=(len("eighty")*100)
count+=(len("ninety")*100)

count+=(len("eleven")*10)
count+=(len("twelve")*10)
count+=(len("thirteen")*10)
count+=(len("fourteen")*10)
count+=(len("fifteen")*10)
count+=(len("sixteen")*10)
count+=(len("seventeen")*10)
count+=(len("eighteen")*10)
count+=(len("nineteen")*10)

count+=(len("hundred")*900)
count+=(len("thousand")*1)

count+=(len("and")*900)
print(count)