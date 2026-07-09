print("------------<Paragraph Analyser>------------")
print("Select paragraph: \n[0] Custom\n[1] Old Workshop (Test paragraph 1)\n[2] Tech Device (Test paragraph 2)\n[3] Nature (Test paragraph 3)")

para_1 = "The old workshop at the edge of town had a strange charm to it. Dusty shelves were stacked with forgotten tools, and sunlight slipped through the cracked windows in thin golden lines. Every object inside seemed to hold a quiet story, waiting for someone patient enough to uncover it. Even the air felt heavy with memories, as if the room itself remembered every hand that had shaped something within its walls."
para_2 = "When the device finally powered on, the screen flickered with a soft blue glow that reflected off the metal casing. Lines of diagnostic text scrolled rapidly, revealing processes that had been dormant for years. It wasn’t clear whether the system was stable or simply pretending to be, but the hum of the internal fans suggested it still had some life left. For a moment, it felt like watching an old friend wake up after a long sleep."
para_3 = "A faint shimmer rolled across the horizon as the first hints of morning light touched the quiet landscape. The air still carried the coolness of night, mixing with the earthy scent of dew settling on the grass. In the distance, a lone bird called out, its voice echoing softly between the hills as if announcing the start of something important. Nothing moved quickly; everything unfolded with a slow, deliberate calm that made the moment feel almost suspended in time."
selection = int(input("Select your paragrpah by typing 0, 1, 2 or 3:\n> "))

def analyse_para():
    def sentence_count():
        sentence_list = para_custom.split(". ")
        print(f"> {len(sentence_list)} sentences")
    def word_count():
        word_list = para_custom.split()
        print(f"> {len(word_list)} words")
    def character_count_no_space():
        word_list = para_custom.replace(" ", "")
        print(f"> {len(word_list)} characters (Excluding space)")
    def character_count_space():
        print(f"> {len(para_custom)} characters (Including space)")
    print(f"Paragraph:\n  {para_custom}")
    print(f"\nStats:")
    sentence_count()
    word_count()
    character_count_no_space()
    character_count_space()


if selection == 0:
    para_custom = input("Type/Paste your paragraph here:\n> ")
    analyse_para()
elif selection == 1:
    para_custom = para_1
    analyse_para()
elif selection == 2:
    para_custom = para_2
    analyse_para()
elif selection == 3:
    para_custom = para_3
    analyse_para()
else:
    print("Error please select a valid selection. Exiting the program...")
