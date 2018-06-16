/**
 * 
 * This is a small function that normalizes Myanmar text. It can be used to
 * normalize MM text after converting to Unicode from Zawgyi.
 * 
 * @author Aye Hninn Khine
 * 
 */
public class MMTextNormalizer {

	private MMTextNormalizer() {
	}

	/**
	 * 
	 * @param input
	 *            must be after converting to Unicode from Zawgyi text.
	 * @return The resulting normalized String
	 */
	public static String normalize(String input) {

		if (input == null) {
			return null;
		}

		String normalizedString = input;

		normalizedString = normalizedString.replaceAll("([\u102B-\u1035])([\u103B-\u103E])", "$2$1");
		// reordering storage order
		normalizedString = normalizedString.replaceAll("\u1036\u102F", "\u102F\u1036");
		// reorder
		normalizedString = normalizedString.replaceAll("([\u1000-\u1020])(\u103D)(\u1031)(\u103E)", "$1$2$4$3");
		// For Latest Myanmar 3
		normalizedString = normalizedString.replaceAll("(\u103A)(\u1037)", "$2$1");
		normalizedString = normalizedString.replaceAll("(\u1036)(\u102F)", "$2$1");
		// reorder Ya pint and Ha htoe
		normalizedString = normalizedString.replaceAll("\u103E\u103B", "\u103B\u103E");
		// reorder auk myint and Vowel sign AA
		normalizedString = normalizedString.replaceAll("\u1037\u102C", "\u102C\u1037");
		// remove duplicates
		normalizedString = normalizedString.replaceAll("(\u102B)+", "\u102B");
		normalizedString = normalizedString.replaceAll("(\u102C)+", "\u102C");
		normalizedString = normalizedString.replaceAll("(\u102D)+", "\u102D");
		normalizedString = normalizedString.replaceAll("(\u102E)+", "\u102E");
		normalizedString = normalizedString.replaceAll("(\u102F)+", "\u102F");
		normalizedString = normalizedString.replaceAll("(\u1030)+", "\u1030");
		normalizedString = normalizedString.replaceAll("(\u1031)+", "\u1031");
		normalizedString = normalizedString.replaceAll("(\u1032)+", "\u1032");
		normalizedString = normalizedString.replaceAll("(\u1033)+", "\u1033");
		normalizedString = normalizedString.replaceAll("(\u1034)+", "\u1034");
		normalizedString = normalizedString.replaceAll("(\u1035)+", "\u1035");
		normalizedString = normalizedString.replaceAll("(\u1036)+", "\u1036");
		normalizedString = normalizedString.replaceAll("(\u1037)+", "\u1037");
		normalizedString = normalizedString.replaceAll("(\u1038)+", "\u1038");
		normalizedString = normalizedString.replaceAll("(\u1039)+", "\u1039");
		normalizedString = normalizedString.replaceAll("(\u103A)+", "\u103A");
		normalizedString = normalizedString.replaceAll("(\u103B)+", "\u103B");
		normalizedString = normalizedString.replaceAll("(\u103C)+", "\u103C");
		normalizedString = normalizedString.replaceAll("(\u103D)+", "\u103D");
		normalizedString = normalizedString.replaceAll("(\u103E)+", "\u103E");
		normalizedString = normalizedString.replaceAll("(\u103F)+", "\u103F");
		// remove double or more VOWEL SIGN U and ANUSVARA
		normalizedString = normalizedString.replaceAll("(\u102F\u1036)+", "\u102F\u1036");
		// remove double or more SIGN 1 and SIGN U
		normalizedString = normalizedString.replaceAll("(\u102D\u102F)+", "\u102D\u102F");
		// remove mutlitple vowel sing U
		normalizedString = normalizedString.replaceAll("([\u1000-\u1021])(\u102F)(\u102D)", "$1$3$2");
		normalizedString = normalizedString.replaceAll("([\u1000-\u1021])(\u1030)(\u102D)", "$1$3\u102F");
		normalizedString = normalizedString.replaceAll("\u102F\u102E", "\u102E\u102F");
		normalizedString = normalizedString.replaceAll("([\u1000-\u1020])(\u103E)(\u1031)(\u103B)", "$1$4$2$3");
		// zero and wa
		normalizedString = normalizedString.replaceAll("\u1040\u102D(?!\u0020?/)", "\u101D\u102D");
		normalizedString = normalizedString
				.replaceAll("([^\u1040-\u1049])\u1040([^\u1040-\u1049\u0020]|[\u104a\u104b])", "$1\u101D$2");
		normalizedString = normalizedString.replaceAll("(\u1040)([\u102B-\u1032])", "\u101D$2");
		normalizedString = normalizedString.replaceAll("(\u1040)(\u1036)", "\u101D$2");
		normalizedString = normalizedString.replaceAll("(\u1040)(\u103A)", "\u101D$2");
		normalizedString = normalizedString.replaceAll("(\u1040)(\u103E)", "\u101D$2");
		// seven and ra
		normalizedString = normalizedString.replaceAll(
				"(\u1047)( ? = [\u1000 - \u101C\u101E - \u102A\u102C\u102E - \u103F\u104C - \u109F\u0020])", "\u101B");
		normalizedString = normalizedString.replaceAll("\u1031\u1047", "\u1031\u101B");
		// For the case of ဖံွ့ဖြိုး
		normalizedString = normalizedString.replaceAll("([\u1000-\u1021])(\u1036)(\u103D)(\u1037)", "$1$3$2$4");
		// အိနိ္ဒယ reorder
		normalizedString = normalizedString.replaceAll("([\u1000-\u1021])(\u102D)(\u1039)([\u1000-\u1021])",
				"$1$3$4$2");
		normalizedString = normalizedString.replaceAll("([\u1000-\u1021])(\u1036)(\u103E)", "$1$3$2");
		// reorder Sign U and auk myint
		normalizedString = normalizedString.replaceAll("\u1037\u102F", "\u102F\u1037");
		// reorder Sign Wa and ANUSVARA
		normalizedString = normalizedString.replaceAll("\u1036\u103D", "\u103D\u1036");
		// reorder for သင်္ဘော
		normalizedString = normalizedString.replaceAll("(\u1004)(\u1031)(\u103A)(\u1039)([\u1000-\u1021])",
				"$1$3$4$5$2");
		// type error
		normalizedString = normalizedString.replaceAll("(\u102D)(\u103A)+", "$1");
		// fix nya lay that and Sign U
		normalizedString = normalizedString.replaceAll("\u1025\u103A", "\u1009\u103A");
		normalizedString = normalizedString.replaceAll("\u200B", "");
		normalizedString = normalizedString.replaceAll("\u200C", "");
		normalizedString = normalizedString.replaceAll("\u202C", "");
		normalizedString = normalizedString.replaceAll("\u00A0", "");
		// Type Error (reorder)
		normalizedString = normalizedString.replaceAll("([\u1000-\u1021])(\u1031)(\u103D)", "$1$3$2");
		// Type Error (reorder)
		normalizedString = normalizedString.replaceAll("([\u1000-\u1021])(\u1031)(\u103E)(\u103B)", "$1$3$4$2");

		return normalizedString;
	}
}
