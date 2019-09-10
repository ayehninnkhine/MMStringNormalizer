#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author Nyan Lynn Myint
#Normalization Rules By Aye Hninn Khine

## reorder dependent vowel and dependent consonant signs
#{ "from": "([\u102B-\u1035]+)([\u103B-\u103E]+)", "to": "\\\\2\\\\1" }

# ## reordering myanmar storage order
#{ "from": "([\u102D\u102E\u1032]{0,})([\u103B-\u103E]{0,})([\u102F\u1030]{0,})([\u1036\u1037\u1038]{0,})([\u102D\u102E\u1032]{0,})", "to": "\\\\2\\\\1\\\\5\\\\3\\\\4" } 
#{ "from": "(^|[^\u1000-\u1021\u103B-\u103E])(\u1031)([\u1000-\u1021])((?:\u1039[\u1000-\u1021])?)([\u103B-\u103E]{0,})", "to": "\\\\1\\\\3\\\\4\\\\5\\\\2" }

## for aukmyit and SIGN AA
#{ "from": "\u1037\u102C", "to": "\u102C\u1037" }

## For Latest Myanmar 3
#{ "from": "\u103A\u1037", "to": "\u1037\u103A" }
#{ "from": "\u1036\u102F", "to": "\u102F\u1036" }

## remove zero width space and zero width non-joiner
#{ "from": "[\u200B\u200C\u202C\u00A0]", "to": "" }

## reorder Ya pint and Ha htoe
#{ "from": "\u103E\u103B", "to": "\u103B\u103E" }

## remove duplicate dependent characters
#{ "from": "([\u102B-\u103E])\\\\1+", "to": "\\\\1" }

## these duplicates based on document frequency errors
## remove double or more SIGN MEDIAL WA and HA
#{ "from": "(\u103D\u103E)+", "to": "\u103D\u103E" }

## remove double or more VOWEL SIGN U and ANUSVARA
#{ "from": "(\u102F\u1036)+", "to": "\u102F\u1036" }

## remove double or more SIGN 1 and SIGN U
#{ "from": "(\u102D\u102F)+", "to": "\u102D\u102F" }

## fixed wrong spelling
#{ "from": "([\u102D\u102E])\u1030", "to": "\\\\1\u102F" }

## For the case of ဖံွ့ဖြိုး
#{ "from": "([\u1000-\u1021])(\u1036)(\u103D)(\u1037)", "to": "\\\\1\\\\3\\\\2\\\\4" }

## For the case of အိနိ္ဒယ
#{ "from": "([\u1000-\u1021])(\u102D)(\u1039)([\u1000-\u1021])", "to": "\\\\1\\\\3\\\\4\\\\2" }
#{ "from": "([\u1000-\u1021])(\u1036)(\u103E)", "to": "\\\\1\\\\3\\\\2" }

## seven and ra
#{ "from": "(\u1047)(?=[\u1000-\u101C\u101E-\u102A\u102C\u102E-\u103F\u104C-\u109F\u0020])", "to": "\u101B" }
#{ "from": "\u1031\u1047", "to": "\u1031\u101B" }

## reorder Sign U and auk myint
#{ "from": "\u1037\u102F", "to": "\u102F\u1037" }

## reorder Sign Wa and  ANUSVARA
#{ "from": "\u1036\u103D", "to": "\u103D\u1036" }

## reorder for သင်္ဘော
#{ "from": "(\u1004)(\u1031)(\u103A)(\u1039)([\u1000-\u1021])", "to": "\\\\1\\\\3\\\\4\\\\5\\\\2" }

## type error
#{ "from": "(\u102D)(\u103A)+", "to": "\\\\1" }

## fix nya lay that and Sign U
#{ "from": "\u1025\u103A", "to": "\u1009\u103A" }

## Type Error (reorder)
#{ "from": "([\u1000-\u1021])(\u1031)(\u103D)", "to": "\\\\1\\\\3\\\\2" } 

## Type Error (reorder)
#{ "from": "([\u1000-\u1021])(\u1031)(\u103E)(\u103B)", "to": "\\\\1\\\\3\\\\4\\\\2" }]'

import json,re
class normalizer:
    def mm_normalize(self,input_string=None):
        json_rules = '[{ "from": "([\u102B-\u1035]+)([\u103B-\u103E]+)", "to": "\\\\2\\\\1" }, { "from": "([\u102D\u102E\u1032]{0,})([\u103B-\u103E]{0,})([\u102F\u1030]{0,})([\u1036\u1037\u1038]{0,})([\u102D\u102E\u1032]{0,})", "to": "\\\\2\\\\1\\\\5\\\\3\\\\4" }, { "from": "(^|[^\u1000-\u1021\u103B-\u103E])(\u1031)([\u1000-\u1021])((?:\u1039[\u1000-\u1021])?)([\u103B-\u103E]{0,})", "to": "\\\\1\\\\3\\\\4\\\\5\\\\2" }, { "from": "\u1037\u102C", "to": "\u102C\u1037" }, { "from": "\u103A\u1037", "to": "\u1037\u103A" }, { "from": "\u1036\u102F", "to": "\u102F\u1036" }, { "from": "[\u200B\u200C\u202C\u00A0]", "to": "" }, { "from": "\u103E\u103B", "to": "\u103B\u103E" }, { "from": "([\u102B-\u103E])\\\\1+", "to": "\\\\1" }, { "from": "(\u103D\u103E)+", "to": "\u103D\u103E" }, { "from": "(\u102F\u1036)+", "to": "\u102F\u1036" }, { "from": "(\u102D\u102F)+", "to": "\u102D\u102F" }, { "from": "([\u102D\u102E])\u1030", "to": "\\\\1\u102F" }, { "from": "([\u1000-\u1021])(\u1036)(\u103D)(\u1037)", "to": "\\\\1\\\\3\\\\2\\\\4" }, { "from": "([\u1000-\u1021])(\u102D)(\u1039)([\u1000-\u1021])", "to": "\\\\1\\\\3\\\\4\\\\2" }, { "from": "([\u1000-\u1021])(\u1036)(\u103E)", "to": "\\\\1\\\\3\\\\2" }, { "from": "(\u1047)(?=[\u1000-\u101C\u101E-\u102A\u102C\u102E-\u103F\u104C-\u109F\u0020])", "to": "\u101B" }, { "from": "\u1031\u1047", "to": "\u1031\u101B" }, { "from": "\u1037\u102F", "to": "\u102F\u1037" }, { "from": "\u1036\u103D", "to": "\u103D\u1036" }, { "from": "(\u1004)(\u1031)(\u103A)(\u1039)([\u1000-\u1021])", "to": "\\\\1\\\\3\\\\4\\\\5\\\\2" }, { "from": "(\u102D)(\u103A)+", "to": "\\\\1" }, { "from": "\u1025\u103A", "to": "\u1009\u103A" }, { "from": "([\u1000-\u1021])(\u1031)(\u103D)", "to": "\\\\1\\\\3\\\\2" }, { "from": "([\u1000-\u1021])(\u1031)(\u103E)(\u103B)", "to": "\\\\1\\\\3\\\\4\\\\2" }]'
        rules = json.loads(json_rules)
        for rule in rules:
            input_string = re.sub(rule["from"], rule["to"], input_string)
        return input_string  


