### plg_functions.py

class PigLatin:
    def encodeit(self,message):
        vowel_index = 'AaEeIiOoUuYy'
        punc_index = "@():,+!'.-+?/"
        message = message.split()
        result = ''
        for word in message:
            if word[0].isalpha() and word[0] not in vowel_index:
                if word[1] in vowel_index:
                    mod_word = word[1:]+word[0]+'-'+'ay'
                    result += mod_word + ' '
                elif word[1] not in vowel_index:
                    mod_word = word[2:]+word[0]+word[1]+'-'+'ay'
                    result += mod_word + ' '
            elif word[0].isalpha() and word[0] in vowel_index:
                mod_word = word[0:]+'-'+'yay'
                result += mod_word + ' '
            else:
                result += word
        if result[-1] == ' ':
            result = result[:-1]
        else:
            pass
        return str(result.capitalize())
