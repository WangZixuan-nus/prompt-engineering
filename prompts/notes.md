# 什么是prompt？
提示是用户提供给 AI 系统以生成响应的输入内容。

# prompt engineering
由于从模型生成的内容是不确定的，因此提示获取所需输出是艺术与科学的结合。prompt engineering 是通过精心设计prompt，以便模型能够生成满足用户需求的内容。核心在于调整prompt的结构、措辞、上下文和附加信息，优化模型的回答质量。

## 关键要点
1）明确性：明确说明需求，而非模糊不清的描述

2）上下文控制：通过背景信息等限制模型的理解和回答范围（如「你是一名律师……」）

3）结构化指令：分步骤（第一步：计算xxx，第二步：基于xx数据，分析xxx）或指定输出格式

4）角色扮演：赋予模型特定身份（如「假设你是产品经理」）

5）示例引导：提供输入-输出样例，降低歧义。

## 提示写作技巧
1. 利用模板框架，分阶段拆解问题
模板示例：[角色] + [任务] + [具体要求] + [输出格式]

2. 避免在同一个对话中对话太多次。一个阶段结束后，总结阶段性结论，并新开一个对话，您可以使用以下提示：
“总结一下我们目前讨论的内容。”
然后将该总结复制粘贴到新的对话中，以快速提供上下文。
当上下文不再重要时，重新开始
如果之前的上下文不再重要，最好开启新的对话。以清晰、独立的提示开始，例如：
“让我们从头开始重新做这件事。”/“重构以下代码”

3. 一次完成一项任务
每个提示始终专注于一项任务。避免合并多个不相关的指令。这可以提高清晰度，减少混淆，并带来更好的结果。

4. 添加前缀
输入前缀： 向输入信号添加前缀，即输入到模型的语义上有意义的部分。例如，前缀“English：”和“French：”分隔两种不同的语言。
输出前缀： 即使输出是由模型生成的，也可以在提示中为输出添加前缀。输出前缀为模型提供有关预期响应的信息。例如，输出前缀“JSON：”向模型发出信号，表明输出应采用 JSON 格式。
示例前缀： 在少量提示中，向示例添加前缀可提供模型在生成输出时可以使用的标签，从而更轻松地解析输出内容。
在以下示例中，“Text：” 是输入前缀，“The answer is：” 是输出前缀。

Prompt:  
```
Classify the text as one of the following categories.
- large
- small
Text: Rhino
The answer is: large
Text: Mouse
The answer is: small
Text: Snail
The answer is: small
Text: Elephant
The answer is:
```
Response:  
```
The answer is: large
```
将提示分解为组件

5. 参数
每次调用模型时，都会包含一些参数值，用于控制模型如何生成响应。不同的参数值会导致模型输出不同的结果。你可以尝试不同的参数设置，以找到最适合任务的配置。不同模型所支持的参数可能有所不同。最常见的参数包括以下几类：

**最大输出 tokens（Max output tokens）：**
指定模型在响应中最多可以生成的 token 数量。一个 token 大约对应 4 个字符。100 个 token 大约相当于 60–80 个单词。

**温度（Temperature）：**
温度控制 token 选择的随机程度。温度在生成响应时用于采样，尤其是在结合 topP 和 topK 时。较低的温度适合需要更确定性或较少开放式回答的场景，而较高的温度则可能带来更丰富或更具创造性的结果。温度为 0 时是确定性的，表示模型总是选择概率最高的输出。

**topK：**
topK 参数决定模型如何选择输出 token。topK=1 时，表示总是选择概率最高的 token（也称为贪婪解码）；topK=3 时，表示下一个 token 会从概率最高的 3 个候选中，根据温度进行选择。在每一步生成时，模型会先选出概率最高的 topK 个 token，再结合 topP 过滤，最后通过温度采样选择最终的 token。

**topP：**
topP 参数决定模型如何选择输出 token。模型会按照概率从高到低累计，直到总和达到 topP 的值为止，再在这些 token 中通过温度采样选择下一个 token。例如，如果 token A、B、C 的概率分别是 0.3、0.2 和 0.1，而 topP=0.5，那么模型只会在 A 和 B 之间选择，而不会考虑 C。默认的 topP 值为 0.95。

**停止序列（stop\_sequences）：**
你可以设置一个停止序列，让模型在生成到该序列时停止输出。停止序列可以是任意字符组合。但要尽量避免选择可能出现在正常生成内容中的序列，以免影响输出质量。

6. 提示词迭代策略

提示词设计有时需要多次迭代，才能稳定获得你想要的响应。本节提供了一些在迭代提示词时可以尝试的方法：

**使用不同的措辞：**
在提示词中使用不同的单词或表达方式，往往会让模型产生不同的回答，即使它们表达的是同一个意思。如果提示词没有得到预期的结果，可以尝试重新表述。

* **版本 1：** How do I bake a pie?（我该如何烤一个派？）
* **版本 2：** Suggest a recipe for a pie.（推荐一个派的食谱。）
* **版本 3：** What's a good pie recipe?（什么是一个好的派食谱？）

---

**切换到类比任务：**
如果模型无法按照你要求的方式完成任务，可以尝试给它一个类似的任务，从而实现相同的目标。

例如，这个提示词让模型使用预设类别对一本书进行分类：

**提示词：**
Which category does *The Odyssey* belong to:

* thriller
* sci-fi
* mythology
* biography

**响应：**
*The Odyssey* 属于 **mythology（神话）** 类别。

**原因：**

* **Mythology：** *The Odyssey* 讲述了希腊神话中的英雄奥德修斯在特洛伊战争后的归乡之旅，故事中包含了神祇、怪物和超自然事件，这些都是希腊神话的典型元素。

响应是正确的，但模型没有严格按照选项范围作答。你希望模型只从选项中回答，而不是输出完整的句子。在这种情况下，可以把提示词改写为多选题形式，并明确要求模型选择一个选项。

**提示词：**
Multiple choice problem: Which of the following options describes the book *The Odyssey*?
Options:

* thriller
* sci-fi
* mythology
* biography

**响应：**
The correct answer is mythology.

---

**调整提示词内容顺序：**
有时提示词的内容顺序会影响响应。可以尝试更换顺序，观察结果。

* **版本 1：** \[examples] → \[context] → \[input]
* **版本 2：** \[input] → \[examples] → \[context]
* **版本 3：** \[examples] → \[input] → \[context]

---

7. 对抗性测试

通过反向提问验证模型理解：

「如果反对这个观点，可能提出哪些合理质疑？请列出并给出反驳论据」

### 回退响应（Fallback responses）

当提示词或模型响应触发安全过滤时，模型会返回回退响应。例如：

> “我无法帮助处理这个问题，因为我只是一个语言模型。”

如果遇到回退响应，可以尝试 **提高温度（temperature）**。

---

### 需要避免的情况

* 避免依赖模型生成事实性信息。
* 在数学和逻辑问题上要谨慎使用。

---

### 生成模型的工作原理

这一部分回答了一个问题：**生成模型的响应是随机的，还是确定性的？**

简短答案：两者都是。

当你向生成模型输入提示词时，生成文本分为两个阶段：

1. **阶段一：概率分布生成**
   模型处理输入提示词，并对可能的下一个 token（单词）生成概率分布。
   例如，输入 “The dog jumped over the ... ” 时，模型可能给出如下概率分布：

   ```
   [("fence", 0.77), ("ledge", 0.12), ("blanket", 0.03), ...]
   ```

   这一过程是确定性的 —— 输入相同的提示词，生成的概率分布始终相同。

2. **阶段二：解码生成文本**
   模型将概率分布转换为实际文本响应，这里会使用不同的解码策略。

   * 一种简单的策略是每次都选择概率最高的 token（确定性）。
   * 另一种策略是基于概率分布进行随机采样（随机性）。

   随机程度由 **温度（temperature）** 控制：

   * 温度 = 0 → 仅选择概率最高的 token，没有随机性。
   * 温度较高 → 增加随机性，可能产生更加意外和多样的结果。

# link:
[《GPT提示词大全》进阶版](https://fcnyytadf5ju.feishu.cn/wiki/NJ0awapB7icqXzkyfqfcL2pBnVd)
[How to use ChatGPT with external tools](https://mitsloan.mit.edu/ideas-made-to-matter/how-to-use-chatgpt-external-tools)
[open AI-Text generation](https://platform.openai.com/docs/guides/text?api-mode=responses)
Continuously updating...
[Gemini-Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
[Gemini-Prompt Galley](https://ai.google.dev/gemini-api/prompts)
