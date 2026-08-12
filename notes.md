# Introduction to LangChain

## Foundation Models is divided into two parts
* ### User Perspective - develop application using foundation models.
* ### Builder Perspective - developed foundation models.
#
#### User Side of GenAi  
![alt text](/images/image.png)

## In this we will learn langchain to build just LLM Apps.

## LangChain
* ### 1. Fundamental
* ### 1. RAG
* ### 1. Agents

## LangChain
#### Langchain is open soruce framework for developing application using LLM.
#### Pros
##### 1. Concept of chain. 
##### 2. Model agnoistic development.
##### 3. complete ecosystem.
##### 4. memory and state handling.

###  Components of LangChain
![alt text](/images/image-1.png)

## 1. Models
* in Langchain the models are core interface through which you interact with AI models.
* in NLP everyone want to build a chatbot but there are two major problem in that NLU[natural language understanding] and Correct Response Genration.
* Langchain can commucate with two types of model.
![alt text](/images/image-2.png)

## 2. Prompts
* LLM <--- input <--- Prompts

## 3. Chains
* chains does the work like it automatically make first LLM output and that output is input for second LLM without chain you have to do this manually.
* chain is concept in langchain by which you can make pipleines.

## 4. Indexes
* indexes connect your application to external knowledge such as pdf, db, websites
* 4 things comes under indexes [doc loader, text splitter, vector store, retrival].
![alt text](/images/image-3.png)
![alt text](/images/image-4.png)

## 5. Memory
![alt text](/images/image-5.png)
memory used in langcgain
![alt text](/images/image-6.png)

#

## 6. Agents

# 1. Models
