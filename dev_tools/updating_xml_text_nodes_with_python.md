# Updating XML Text Nodes with Python
You can use the Python lxml library to avoid manually changing words or phrases in an XML file.

For example, in the following list of online poll participants, more people answered "No" when asked if they think LeBron James is a better basketball player than Michael Jordan:

	<poll_participants>
		<participant_1>
			<answer>No</answer>
		</participant_1>
		<participant_2>
			<answer>Yes</answer>
		</participant_2>
		<participant_3>
			<answer>No</answer>
		</participant_3>
		<participant_4>
			<answer>No</answer>
		</participant_4>
		<participant_5>
			<answer>Yes</answer>
		</participant_5>
	</poll_participants>

Depending on how you present the data, you might want to provide more context to the answers (for example, "No, Michael Jordan is better" rather than only "No"). Instead of changing each answer manually in the XML, you can create a Python script that uses lxml to update all of the text you want to change at once.

## Before You Begin
* Install a version of [Python](https://www.python.org/downloads/) that's compatible with the lxml library. According to the [lxml documentation](https://lxml.de/installation.html), you must have Python version 2.7 or 3.4 and later.
* If you're using Windows, add Python to your PATH.
* Familiarize yourself with XPath syntax so you that your script selects the correct XML nodes. ([Here's an XPath cheat sheet](https://devhints.io/xpath) provided by [devhints.io](https://devhints.io).)

## Create the Script
The following example Python script parses the previously-referenced XML and updates the XPath-selected text.
> __Note:__ Remember, the XPath expression `//` used in the following steps is just an example and may not properly parse your XML document's structure.

1. In a text editor, create a `.py` file (for example, `update_text.py`) and save it to the same location as the XML file.
2. Load the lxml library.  

		import lxml.etree as et
3. Store the root XML element so your script can read the entire contents of the file.

		root = et.parse("survey_participants.xml").getroot()
4. Create a for loop that (1) finds the "No" answers and (2) replaces those answers with "No, Michael Jordan is better".  

		for no_answer in root.xpath('//answer[starts-with(text(),"No")]'):
			no_answer.text = str("No, Michael Jordan is better")

5. Create another for loop that (1) finds the "Yes" answers and (2) replaces those answers with "Yes, LeBron James is better".  

		for yes_answer in root.xpath('//answer[starts-with(text(),"Yes")]'):
			yes_answer.text = str("Yes, LeBron James is better")
6. Write and format these changes to a new XML file.

		update = open("survey_participants_new.xml", "w")
		update.write(et.tostring(root, pretty_print=True).decode("utf-8"))
		update.close()
7. Run the script.  
	The updated content displays in the new XML file:  

		<survey_participants>
			<participant_1>
				<answer>No, Michael Jordan is better</answer>
			</participant_1>
			<participant_2>
				<answer>Yes, LeBron James is better</answer>
			</participant_2>
			<participant_3>
				<answer>No, Michael Jordan is better</answer>
			</participant_3>
			<participant_4>
				<answer>No, Michael Jordan is better</answer>
			</participant_4>
			<participant_5>
				<answer>Yes, LeBron James is better</answer>
			</participant_5>
		</survey_participants>
