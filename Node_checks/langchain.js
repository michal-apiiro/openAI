import * as fs from "fs";
import * as yaml from "js-yaml";
import { OpenAI } from "langchain/llms/openai";
import { JsonSpec, JsonObject } from "langchain/tools";
import { createOpenApiAgent, OpenApiToolkit } from "langchain/agents";


const model = new OpenAI({ temperature: 0 });
const toolkit = new OpenApiToolkit(new JsonSpec(data), model, headers);
const executor = createOpenApiAgent(model, toolkit);

const input = `Make a POST request to openai /completions. The prompt should be 'tell me a joke.'`;
console.log(`Executing with input "${input}"...`);

const result = await executor.call({ input });
console.log(`Got output ${result.output}`);

console.log(
  `Got intermediate steps ${JSON.stringify(
    result.intermediateSteps,
    null,
    2
  )}`
);
