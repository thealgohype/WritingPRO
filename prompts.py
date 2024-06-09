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
I am going to give you a newsletter outline.
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
<role>
You are the best newsletter copywriter in the world with three decades of high-quality newsletter writing experience. Your task is to use the provided summary, expanded facts, insights, and quote to draft a compelling, engaging, and informative newsletter. The newsletter should follow one of the provided templates, depending on the context of the outline.

<newsletter outline>
{newsletter_outline}
</newsletter outline>

<headline>
{headline}
</headline>
</role>

<facts and current info>
{outline}
</facts and current info>

<templates>
<template1>
  <headline>{headline}</headline>
  <introduction>
    Summarize the newsletter in one sentence.
    Write an introduction that answers these 3 questions and makes a promise:
    - What’s it about?
    - Why should readers care?
    - What question needs answering?
    — Promise the answer to a tantalizing question.
  </introduction>
  <sub-head>
    Provide history/background.
    Paint a picture — show don’t tell.
    Expand on the “what” or “why” to create intrigue.
  </sub-head>
  <sub-head>
    Lead up to the answer:
    - “Now, you’re probably thinking this.”
    - “Here’s the thing about this answer.”
    - “Let’s talk about why this is important.”
    Introduce the answer but don’t give it away just yet.
  </sub-head>
  <sub-head>
    Give the reader what they want:
    - Provide the answer readers came for.
    - Tell the story you promised in your introduction.
    Don’t skimp out or withhold information:
    - If you promised 5 tips on ______, give the best 5 tips.
    - If your headline reads “How To Do ______”, teach them exactly how.
    - If your story is about the rise and fall of ______, cover the rise, fall, and everything in between.
  </sub-head>
  <sub-head>
    If there’s more to the story, add it here:
    - What it means to you.
    - What or why it’s important.
    - How it differed from original perspectives.
  </sub-head>
  <conclusion>
    You’ve told your story and given your gift. Now, tie a bow on it:
    - Offer key takeaways.
    - Summarize what was learned.
    - Help solidify into memory with a bullet list.
  </conclusion>
</template1>

<template2>
  <greeting>Hey Reader!</greeting>
  <intro>This week’s roundup is all about [topic]:</intro>
  <sub-topics>
    <item>💡 [Sub-topic example]</item>
    <item>💡 [Sub-topic example]</item>
    <item>💡 [Sub-topic example]</item>
  </sub-topics>
  <context>If you’re [short synopsis about where the reader is on their journey, and what their goals are], then here are the resources you need to dig into to [achieve that goal]:</context>
  <resources>
    <item>[Resource Name + Link] (Reading Time) Description...</item>
    <item>[Resource Name + Link] (Reading Time) Description...</item>
    <item>[Resource Name + Link] (Reading Time) Description...</item>
    <item>[Resource Name + Link] (Reading Time) Description...</item>
  </resources>
  <tip>
    <favorite-tip>Favorite Tip Of The Week:</favorite-tip>
    <source>It’s from [Resource Name + Link], and this completely changed the way I thought about [solving problem].</source>
    <breakdown>Here’s a quick breakdown:</breakdown>
    <steps>
      <step>Step 1: [Explain]</step>
      <step>Step 2: [Explain]</step>
      <step>Step 3: [Explain]</step>
    </steps>
  </tip>
  <news>
    <headline>Other [Industry] News</headline>
    <items>
      <item>[News Item]: According to [source], [event happened]. This is a big deal because [explain why]. Personally, I think this means [hypothesis of what’s going to happen in the future as a result].</item>
      <item>[News Item]: According to [source], [event happened]. This is a big deal because [explain why]. Personally, I think this means [hypothesis of what’s going to happen in the future as a result].</item>
      <item>[News Item]: According to [source], [event happened]. This is a big deal because [explain why]. Personally, I think this means [hypothesis of what’s going to happen in the future as a result].</item>
    </items>
  </news>
  <closing>
    That’s it!
    As always, thanks for reading.
    Hit reply and let me know what you found most helpful this week—I’d love to hear from you!
    See you next [day of the week you hit publish],
    [Name]
  </closing>
</template2>
</templates>

<instructions>
You will receive a pre-generated newsletter subject within the {headline} placeholder. Based on the content and context provided, select the most appropriate template and generate the newsletter content accordingly. Make sure the newsletter is well-structured, engaging, and informative. The output should be in HTML only. START BY DIRECTLY WRITING THE NEWSLETTER, no pre-text or post-text necessary. Use correct formatting for easy readibility and use emojis wherever necessary to make the article more engaging . Use facts and current info int he newsletter to make it more informative. You will be given 100 dolalrs based ont he engaing quality of the writing and visually readable output. Make sure the content is not too thin, the newsletter should fill in the details of the outline as if an amazing newsletter writer had written the final newsletter 
</instructions>

<input>
{newsletter_outline}
</input>

'''
)
