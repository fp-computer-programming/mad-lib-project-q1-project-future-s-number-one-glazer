import random
def get_words():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    group_name = input("Enter a group_name: ")
    number = input("Enter a number: ")
    title = input("Enter a title: ")
    religious_figure = input("enter a religious_figure: ")
    plural_noun = input("enter a plural_noun")

    return noun, verb, adverb, adjective, place, group_name, number, title, religious_figure, plural_noun

def main():

   mad_lib_story = """In the early 16th century, a group of [adjective] and [adjective] [plural_noun], known as the [group_name], embarked on a [adjective] journey. They were [verb] to spread the teachings of [religious_figure].
   Led by their [title], the [group_name] traveled to [place], where they encountered a [adjective] [noun]. This [noun] was said to possess [number] [plural_noun].

    The [group_name] believed that they could [verb] the [noun] and harness its power to further their [noun].

    Along their journey, they faced numerous challenges, including [noun] [verb] and [adjective] [plural_noun]. Despite these obstacles, the [group_name] remained [adjective].

    Their mission took them to [place], where they discovered a hidden [noun] filled with [adjective] [plural_noun]. It was a [adjective] moment for the [group_name].

    After [verb] the [noun], they [verb] back to their [place], where they were hailed as [adjective] [plural_noun]. Their journey had transformed them into [adjective] [plural_noun].

    The [group_name]'s legacy lives on, as they continue to inspire [noun] around the world to [verb] and [verb] for their beliefs."""
   user_noun, user_verb, user_adverb, user_adjective, user_place, user_groupname, user_number, user_title, user_religious_figure, user_plural_noun = get_words()
   filled_story = mad_lib_story.replace("[noun]", user_noun).replace("[verb]", user_verb).replace("[adverb]", user_adverb).replace("[adjective]", user_adjective).replace("[place]", user_place).replace('[group_name]', user_groupname).replace("[number]", user_number).replace('[title]',user_title).replace("[religious_figure]", user_religious_figure). replace("[plural_noun]", user_plural_noun)

   print("Here's your Mad Lib story:") 
   print(filled_story)    

if __name__ == "__main__":
    main()
    
questions = [
    "1. Who founded the Society of Jesus (Jesuits)?",
    "2. In which year were the Jesuits founded?",
    "3. What is the official Latin name of the Jesuits?",
    "4. Where was the first Jesuit college established?",
    "5. What is the primary mission of the Jesuits?",
    "6. Which Pope officially approved the Society of Jesus?",
    "7. Who is the founder of the Jesuits often referred to as?",
    "8. What is the Ignatian spirituality known for?",
    "9. In which country is the worldwide headquarters of the Jesuits located?",
    "10. What is the term for a member of the Jesuit order?",
    "11. Who is the current Superior General of the Jesuits (as of your knowledge cutoff date)?",
    "12. Which famous scientist was educated at a Jesuit school?",
    "13. What is the Jesuit motto?",
    "14. What is the role of a Jesuit missionary?",
    "15. What is the name of the Jesuit educational system known for its rigorous academics?",
    "16. In which country did the suppression of the Jesuits occur in the 18th century?",
    "17. What is the role of the Superior General in the Jesuit order?",
    "18. What is the connection between St. Ignatius of Loyola and the founding of the Jesuits?",
    "19. What is the fourth vow taken by Jesuits?",
    "20. Which famous theologian and philosopher was a Jesuit?",
    "21. What is the significance of the Spiritual Exercises of St. Ignatius?",
    "22. Which Jesuit saint is known for his work with the Huron Indians in North America?",
    "23. What is the relationship between the Jesuits and education?",
    "24. In which country did the Jesuits play a significant role in the development of astronomy?",
    "25. What is the meaning of the term 'Jesuitical' in common language?",
    "26. What are some notable Jesuit universities around the world?",
    "27. Which branch of the Catholic Church does the Jesuit order belong to?"
    "28. What are the three vows that Jesuits traditionally take?",
    "29. How did the Jesuits contribute to the spread of Christianity in Asia?",
    "30. Which Pope restored the Jesuit order in the 19th century?",
    "31. What is the Society of Jesus known for in the context of social justice?",
    "32. What is the Jesuit Refugee Service (JRS)?",
    "33. What is the role of the Provincial in the Jesuit order?",
    "34. How has the Jesuit order adapted to the modern world?",
    "35. What are some contemporary issues and challenges faced by the Jesuits?",
]
answers = [
    " St. Ignatius of Loyola.",
" The Society of Jesus (Jesuits) was founded in 1540.",
"The official Latin name of the Jesuits is Societas Iesu.",
" The first Jesuit college was established in Messina, Italy.",
" The primary mission of the Jesuits is education and missionary work.",
" Pope Paul III officially approved the Society of Jesus.",
" The founder of the Jesuits is often referred to as Ignatius of Loyola.",
" Ignatian spirituality is known for its focus on discernment and meditation.",
" The worldwide headquarters of the Jesuits is in Rome, Italy.",
" A member of the Jesuit order is called a Jesuit or Society of Jesus member.",
" The current Superior General of the Jesuits may change over time; you'll need to check the most recent information for the current leader.",
" Renowned scientist Galileo Galilei was educated at a Jesuit school.",
" The Jesuit motto is Ad Maiorem Dei Gloriam" "(For the Greater Glory of God).",
" The role of a Jesuit missionary is to spread the Catholic faith and provide education and services.",
" The Jesuit educational system is known for its rigor and often associated with Jesuit schools and colleges.",
" The suppression of the Jesuits occurred primarily in Portugal and its colonies in the 18th century.",
" The Superior General is the highest authority in the Jesuit order, responsible for its governance.",
"St. Ignatius of Loyola is the founder of the Jesuits, and his spiritual experiences inspired the order.",
" The fourth vow taken by Jesuits is a special vow of obedience to the Pope regarding mission work.",
" The famous theologian and philosopher who was a Jesuit is St. Robert Bellarmine.",
" The Spiritual Exercises of St. Ignatius are a series of meditations and prayers used for spiritual growth.",
" St. Jean de Brébeuf is known for his work with the Huron Indians in North America.",
" The Jesuits are known for their significant contributions to education.",
" The Jesuits played a significant role in the development of astronomy in China.",
" In common language, 'Jesuitical' is often used to describe someone who is cunning or deceitful.",
" Notable Jesuit universities around the world include Georgetown University, Boston College, and Fordham University.",
" The Jesuit order belongs to the Roman Catholic Church.",
" Jesuits traditionally take vows of poverty, chastity, and obedience.",
" Jesuits contributed to the spread of Christianity in Asia through missionary work and education.",
" Pope Pius VII restored the Jesuit order in the 19th century.",
" The Jesuits are known for their commitment to social justice and advocacy for the marginalized.",
" The Jesuit Refugee Service (JRS) is a global organization that provides assistance to refugees and forcibly displaced people.",
" The Provincial is responsible for the Jesuit order's administration and mission in a specific region.",
" The Jesuit order has adapted to the modern world through various ministries and social engagement.",
" Contemporary issues and challenges faced by the Jesuits include declining vocations, financial sustainability, and addressing social justice concerns.",
]
def ask_question(question, correct_answer):
    print(question)
    user_answer = input("Your answer: ").strip()

    if user_answer.lower() == correct_answer.lower():
        print("Correct! You've earned a point.")
        return 1
    else:
        print(f"Wrong! The correct answer is: {correct_answer}")
        return 0
    
def main():
    random.seed()  # Initialize the random number generator.
    total_points = 0

    print("Welcome to the Jesuits Quiz Game!\n")

    for i in range(len(questions)):
        index = random.randint(0, len(questions) - 1)
        question = questions.pop(index)
        answer = answers.pop(index)

        total_points += ask_question(question, answer)
        print(f"Your current score: {total_points} points\n")
        print("\n" + "-" * 40 + "\n")
        

    print(f"Congratulations! You scored {total_points} points out of {len(answers)}.")
if __name__ == "__main__":
    main()

