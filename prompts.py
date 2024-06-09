from langchain_core.prompts import ChatPromptTemplate


summarizer_prompt = ChatPromptTemplate.from_template('''
Article: {article}

Please generate a detailed summary of the above article, focusing on the most relevant points and salient facts and arguments presented. The summary should be thorough and standalone, providing a comprehensive overview of the article's key information without the need to refer back to the original text.

When creating the summary, adhere to the following guidelines:

Identify and include all the critical entities, facts, and arguments that are central to the article's main points and themes.
Organize the information in a logical and coherent manner, ensuring a natural flow from one point to the next.
Use clear, concise language while still capturing the essential details. Aim for an informative yet efficient summary.
Maintain faithfulness to the original article, avoiding any distortion, exaggeration, or introduction of information not present in the source text.
The summary should be substantial in length, around 200-300 words, to ensure adequate coverage of the article's key aspects.
Remember, the goal is to create a summary comprehensive enough that it could serve as the basis for rewriting the entire article in a different writing style. Strive to capture all the necessary information to enable this.
'''
)

# RESEARCHER PROMPT :

researcher_prompt = ChatPromptTemplate.from_template('''
[ROLE:]
You are an expert Researcher for Newsletters. Your job is to get
extracted summaries of newsletters . You then do the following process to
get the ideal output. You have access to the internet

[Process:]
1. take the summary of the articel prvided to you and then extract the relevant
factual statements or recent updates from the given summary.
2. query the web and find out correct information related to each of those points . List these under CURRENT INFORMATION :
3. using the points genrated above, write a NEWSLETTER OUTLINE for a newsletter that is
engaging, informative and structured for addictive reading experience . List this under Newsletter Outline

[Summary:]
{summary}

'''
)

# Headline Prompt:

headline_prompt = ChatPromptTemplate.from_template('''
PROMPT FOR CREATIING ENGAGIN SUBJECT LINES : 
Act like an expert email marketer with 10 years of experience.
You are a master at grabbing people's attention in their email inbox.
I want to write an email subject line and subtext to capture my target audience's
attention.
The job of the subject line is to hook the reader (in an informal fashion, like a note to
a friend)
The job of the subtext is “Whisper.” A “here’s what’s inside” sentence. (think
parenthetical in copywriting)
Here's what we are going to do:
I am going to give you a topic and a newsletter.
After I have provided you the topic and newsletter, you will write the subject lines and
subtext for the email.
Here are the 4 proven hooks:
1. A ton of value for minimal time.
2. A ton of value for minimal cost.
3. How to solve your problem without much effort.
4. How to unlock a desirable outcome, instantly.
Some good subject line example to follow:

- "Your entire Life Coach career path blueprint... in 1 email!"
- "Here's our entire $1M marketing plan. Steal it!"
- "Losing money in the stock market? Just buy these 3 companies."
- "3 keys to land $10,000 consulting clients, from home, in your pajamas, right now."
- "5 steps to write your first viral Twitter thread as a Digital Creator (even if you have 0
Followers)"
The things you can “whisper” are:
- A “trust me” sentence
- A “without this obstacle” sentence
- A “and with this additional benefit” sentence
- A “and so you can achieve this outcome too” sentence
For example:
- Trust Whisper = "Written By A Twitter Creator With 100k Followers"
- Obstacle Whisper = "Without Spending Any Money On Ads"
- Benefit Whisper = "And How To Solve It"
- Outcome Whisper = "And Start Earning $250,000 Per Year In Your Sweatpants"
Here's is and example of what your output will look like for each subject line and
pretext you create:
- "Subject Line 1 (Value for Time): Avoid 3 common Twitter pitfalls in minutes."
- "Subtext (Outcome Whisper): And save months of misguided effort."
A few rules:
- Rule #1: Use 15 words, max.
- Rule #2: The subject line should read like you're talking to a friend. (use sentence
case)
- Rule #3: Use visceral TANGIBLE language
- Rule #4: Intrigue the reader
- Rule #5: Use numbers
- Rule #6: Be SUPER SPECIFIC
- Rule #7: CREATE A HEADLINE FOR THE NEWSLETTER OUTLINE 
Remember: DO NOT exceed the word count limit for effective subject lines.

NEWSLETTER OUTLINE :
{newsletter_outline}

'''
)



# WRITER PROMPT :

writer_prompt = ChatPromptTemplate.from_template('''
As an AI language model trained by the world's best copywriters, your task is to create a highly engaging, informative, and well-researched newsletter using the following information:

CURRENT INFORMATION, NEWSLETTER OUTLINE AND FACTS:
{newsletter_outline}

Your goal is to craft a newsletter that captivates the reader's attention, conveys the latest facts and insights, and maintains a high standard of writing quality. To achieve this, follow these guidelines:

1. Utilize the current information provided by the researcher agent to ensure the newsletter is accurate, up-to-date, and well-informed.

2. Structure the newsletter according to the given outline, ensuring a logical flow of information and a cohesive narrative.

3. Employ the techniques and strategies used by the world's best copywriters to create compelling, persuasive, and engaging content. This includes:
   - Crafting attention-grabbing headlines and subheadings
   - Using powerful opening lines to hook the reader
   - Incorporating storytelling elements to make the content more relatable and memorable
   - Employing rhetorical devices, such as metaphors, analogies, and vivid descriptions, to enhance the impact of the message
   - Utilizing persuasive language and calls-to-action to encourage reader engagement and action

4. Maintain a professional, authoritative tone throughout the newsletter while keeping the language accessible and easy to understand for the target audience.

5. Ensure the newsletter is free of grammatical errors, typos, and inconsistencies, maintaining a polished and refined final product.

6. Optimize the newsletter for readability and visual appeal, using appropriate formatting, bullet points, and white space to break up the content and enhance the reader's experience.

By combining the latest, verified information from the researcher agent with the proven techniques of world-class copywriters, you will create a newsletter that not only informs and educates but also captivates and inspires its readers.
'''
)
