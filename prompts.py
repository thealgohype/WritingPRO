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
