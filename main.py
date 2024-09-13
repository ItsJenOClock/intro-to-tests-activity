def count_a_letter(sentence, letter):
    if not letter.isalpha():
        return None
    if not sentence:
        return None
    if len(letter) > 1:
        return "Enter one letter only"
    
    count = 0
    for char in sentence:
        if char == letter:
            count +=1
    
    return count