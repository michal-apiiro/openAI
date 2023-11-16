import Anthropic from '@anthropic-ai/sdk';

const anthropic = new Anthropic({
	apiKey: 'my api key', // defaults to process.env["ANTHROPIC_API_KEY"]
});

async function main() {
  const completion = await anthropic.completions.create({
    model: 'claude-2',
    max_tokens_to_sample: 300,
    prompt: `${Anthropic.HUMAN_PROMPT} How many toes do dogs have?${Anthropic.AI_PROMPT}`,
  });
  console.log(completion.completion);
}