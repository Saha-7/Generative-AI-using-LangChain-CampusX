# Generative AI using LangChain


## What is GenAI ?
`
Genarative AI is a type of artificial intelligence that creates new content - such as text, images, music or code by learning patterns from existing data, mimicking human creativity. 
`

## Where is GenAI stand?

```mermaid
graph TD
    subgraph AI
        subgraph ML
            subgraph DL
                GenAI["GenAI"]
            end
        end
    end
```


## GenAI impact areas!

- Customer Support
- Content Creation
- Software Development
- Education


## Mental model

```mermaid
%%{init: {'theme':'dark'}}%%
flowchart TD
    A["Foundation Models"] --> B["User Perspective [Application Building]"]
    A --> C["Builder Perspective"]
    
    style A fill:#1a1a1a,stroke:#fff,stroke-width:2px,color:#fff
    style B fill:#2d2d2d,stroke:#fff,stroke-width:2px,color:#fff
    style C fill:#2d2d2d,stroke:#fff,stroke-width:2px,color:#fff
```


## What is LangChain?

- LangChain is an open-source framework for developing applications powered by LLMs.



## LangChain benefits?

- Concepts of chains
- Model Agnostic Development
- Complete ecosystem
- Memory and state handling


## Components of LangChain

- Models
- Prompts
- Chains
- Memory
- Indexes
- Agents

## What are Models in LangChain & their types?

- Models are the core interfaces through which you interact with AI models.

 Two types of model :->

- Language Models  [LLMs, Chat Models (text -> text)]  
- Embedding Models [text -> Vector]


## What is Prompts ?

- Prompts are input provided to LLMs.


## What are Chains & it's types ?




## What are Indexes & it's types?

- Indexes connect your applications to external knowledge - such as PDFs,
websites or databases.


Types :- 

- Doc Loader
- Text Splitter
- Vector Store
- Retrievers