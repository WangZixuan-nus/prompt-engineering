# What is prompt?
Prompt is the input content a user give to an AI system to generate a response.

# Prompt engineering 
Promot engineering is the process of writing effective instructions for a model, such that it consistently generates content that meets users' requirements. 

## Break down prompts into components
For use cases that require complex prompts, you can help the model manage this complexity by breaking things down into simpler components.

Break down instructions: Instead of having many instructions in one prompt, create one prompt per instruction. You can choose which prompt to process based on the user's input.

Chain prompts: For complex tasks that involve multiple sequential steps, make each step a prompt and chain the prompts together in a sequence. In this sequential chain of prompts, the output of one prompt in the sequence becomes the input of the next prompt. The output of the last prompt in the sequence is the final output.

Aggregate responses: Aggregation is when you want to perform different parallel tasks on different portions of the data and aggregate the results to produce the final output. For example, you can tell the model to perform one operation on the first part of the data, perform another operation on the rest of the data and aggregate the results.

## Prompt Writing Tips
Summarize and Transfer Between Dialogues
After completing a stage of work in one conversation, start a new chat for the next stage. You can use a prompt like:

"Summarize what we've discussed so far."
Then copy and paste that summary into the new conversation to provide quick context.

Start Fresh When Context Is Unnecessary
If previous context is no longer important, it’s better to start a new conversation. Begin with a clear, standalone prompt like:

"Let's rework this from scratch."

One Task at a Time
Always focus on one task per prompt. Avoid combining multiple unrelated instructions. This improves clarity, reduces confusion, and leads to better results.

# link:
[《GPT提示词大全》进阶版](https://fcnyytadf5ju.feishu.cn/wiki/NJ0awapB7icqXzkyfqfcL2pBnVd)
[How to use ChatGPT with external tools](https://mitsloan.mit.edu/ideas-made-to-matter/how-to-use-chatgpt-external-tools)
Continuously updating...
