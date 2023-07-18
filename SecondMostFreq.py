#to seee the second most repeating ele in a string
def check(str):
    char_freq_count = {}
    for char in str:
        char_freq_count[char] = char_freq_count.get(char,0)+1
    mostfreq = None
    secondmostfreq = None
    for char,freq in char_freq_count.items():
        if mostfreq is None or freq>char_freq_count[mostfreq]:
            secondmostfreq = mostfreq
            mostfreq = char
        elif secondmostfreq is None or freq>char_freq_count[secondmostfreq]:
            secondmostfreq = char
            
    return secondmostfreq

