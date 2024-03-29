package normalizer

import (
	"encoding/json"
	"fmt"

	"github.com/dlclark/regexp2"
)

type NormalizeRules struct {
	From string
	To   string
}

func MMTextNormalizer(input string) (string, error) {
	var rules []NormalizeRules
	output := input
	jsonRules := `[
		{
			"from":"([\u102B-\u1035])([\u103B-\u103E])", 
			"to":"$2$1"
		},
		{
			"from": "\u1036\u102F", 
			"to":"\u102F\u1036"
		},
		{
			"from":"([\u1000-\u1020])(\u103D)(\u1031)(\u103E)",
			"to":"$1$2$4$3"
		},
		{
			"from":"(\u103A)(\u1037)",
			"to":"$2$1"
		},
		{
			"from":"(\u1036)(\u102F)",
			"to":"$2$1"
		},
		{
			"from":"\u103E\u103B", 
			"to":"\u103B\u103E"
		},
		{
			"from":"\u1037\u102C", 
			"to":"\u102C\u1037"
		},
		{
			"from":"(\u102B)+", 
			"to":"\u102B"
		},
		{
			"from":"(\u102C)+", 
			"to":"\u102C"
		},
		{
			"from":"(\u102D)+",
			"to":"\u102D"
		},
		{
			"from":"(\u102E)+", 
			"to":"\u102E"
		},
		{
			"from":"(\u102F)+",
			"to": "\u102F"
		},
		{
			"from":"(\u1030)+",
			"to": "\u1030"
		},
		{
			"from":"(\u1031)+",
			"to": "\u1031"
		},
		{
			"from":"(\u1032)+",
			"to": "\u1032"
		},
		{
			"from":"(\u1033)+",
			"to": "\u1033"
		},
		{
			"from":"(\u1034)+",
			"to": "\u1034"
		},
		{
			"from":"(\u1035)+",
			"to": "\u1035"
		},
		{
			"from":"(\u1036)+",
			"to": "\u1036"
		},
		{
			"from":"(\u1037)+",
			"to": "\u1037"
		},
		{
			"from":"(\u1038)+",
			"to": "\u1038"
		},
		{
			"from":"(\u1039)+",
			"to": "\u1039"
		},
		{
			"from":"(\u103A)+",
			"to": "\u103A"
		},
		{
			"from":"(\u103B)+",
			"to": "\u103B"
		},
		{
			"from":"(\u103C)+",
			"to": "\u103C"
		},
		{
			"from":"(\u103D)+",
			"to": "\u103D"
		},
		{
			"from":"(\u103E)+",
			"to": "\u103E"
		},
		{
			"from":"(\u103F)+",
			"to": "\u103F"
		},
		{
			"from":"(\u102F\u1036)+",
			"to": "\u102F\u1036"
		},
		{
			"from":"(\u102D\u102F)+",
			"to": "\u102D\u102F"
		},
		{
			"from":"([\u1000-\u1021])(\u102F)(\u102D)",
			"to": "$1$3$2"
		},
		{
			"from":"([\u1000-\u1021])(\u1030)(\u102D)",
			"to": "$1$3\u102F"
		},
		{
			"from":"\u102F\u102E",
			"to": "\u102E\u102F"
		},
		{
			"from":"([\u1000-\u1020])(\u103E)(\u1031)(\u103B)",
			"to": "$1$4$2$3"
		},
		{
			"from":"\u1040\u102D(?!\u0020?/)",
			"to": "\u101D\u102D"
		},
		{
			"from":"([^\u1040-\u1049])\u1040([^\u1040-\u1049\u0020]|[\u104a\u104b])",
			"to": "$1\u101D$2"
		},
		{
			"from":"(\u1040)([\u102B-\u1032])",
			"to": "\u101D$2"
		},
		{
			"from":"(\u1040)(\u1036)",
			"to": "\u101D$2"
		},
		{
			"from":"(\u1040)(\u103A)",
			"to": "\u101D$2"
		},
		{
			"from":"(\u1040)(\u103E)",
			"to": "\u101D$2"
		},
		{
			"from":"(\u1047)( ? = [\u1000 - \u101C\u101E - \u102A\u102C\u102E - \u103F\u104C - \u109F\u0020])",
			"to": "\u101B"
		},
		{
			"from":"\u1031\u1047",
			"to": "\u1031\u101B"
		},
		{
			"from":"([\u1000-\u1021])(\u1036)(\u103D)(\u1037)",
			"to": "$1$3$2$4"
		},
		{
			"from":"([\u1000-\u1021])(\u102D)(\u1039)([\u1000-\u1021])",
			"to":"$1$3$4$2"
		},
		{
			"from":"([\u1000-\u1021])(\u1036)(\u103E)",
			"to": "$1$3$2"
		},
		{
			"from":"\u1037\u102F",
			"to": "\u102F\u1037"
		},
		{
			"from":"\u1036\u103D",
			"to": "\u103D\u1036"
		},
		{
			"from":"(\u1004)(\u1031)(\u103A)(\u1039)([\u1000-\u1021])",
			"to":"$1$3$4$5$2"
		},
		{
			"from":"(\u102D)(\u103A)+", 
			"to":"$1"
		},	
		{
			"from":"\u1025\u103A",
			"to": "\u1009\u103A"
		},
		{
			"from":"\u200B",
			"to": ""
		},
		{
			"from":"\u200C",
			"to": ""
		},
		{
			"from":"\u202C",
			"to": ""
		},
		{
			"from":"\u00A0",
			"to": ""
		},	
		{
			"from":"([\u1000-\u1021])(\u1031)(\u103D)",
			"to": "$1$3$2"
		},
		{
			"from":"([\u1000-\u1021])(\u1031)(\u103E)(\u103B)",
			"to": "$1$3$4$2"
		}
	]`

	err := json.Unmarshal([]byte(jsonRules), &rules)
	if err != nil {
		panic(err.Error())
	}

	re2 := regexp2.MustCompile("", 0)

	for _, rule := range rules {
		re2 = regexp2.MustCompile(rule.From, 1)
		res, err := re2.Replace(output, rule.To, -1, -1)
		output = res
		if err != nil {
			return "", fmt.Errorf("Can't normalize the text: %w", err)
		}
	}

	return output, nil
}
