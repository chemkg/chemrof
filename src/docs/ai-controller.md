# AI Controller Guide: Using @dragon-ai-agent

This guide explains how to use the AI agent (@dragon-ai-agent) that can help with ChemROF schema development tasks directly through GitHub issues and pull requests.

## How it works

The AI agent is integrated into this repository through GitHub Actions and can perform various tasks such as:

- Adding or updating class descriptions in the schema
- Creating example instances 
- Generating documentation
- Analyzing schema structure
- Making code changes and submitting pull requests

The agent operates with knowledge of LinkML best practices, ChemROF schema conventions, and the specific development workflow used in this repository.

## How to invoke the AI agent

### Basic invocation

The AI agent is invoked by mentioning `@dragon-ai-agent` followed by the exact word `please` in a GitHub issue or pull request comment:

```
@dragon-ai-agent please [your request here]
```

**Important**: The word `please` must follow the mention exactly. This is a safety mechanism to prevent accidental invocation.

### Example requests

Here are some example ways to invoke the agent:

```
@dragon-ai-agent please add descriptions to classes that are missing them
```

```
@dragon-ai-agent please create an example for the MolecularEntity class
```

```
@dragon-ai-agent please resolve this issue by updating the schema documentation
```

## Authorization

The AI agent will **only** respond to requests from authorized controllers. 

### Check if you're authorized

To see who is currently authorized, check the file [.github/ai-controllers.json[(https://github.com/chemkg/chemrof/blob/main/.github/ai-controllers.json) in this repository.

If you want to add yourself, edit this file and make a PR in the normal way

**Important**: Follow proper JSON syntax with quotes around usernames and commas between entries.

**Note**: Controller access should only be requested by trusted contributors who understand the schema development process and will use the AI agent responsibly.

## AI system instructions

The AI agent follows detailed instructions stored in `CLAUDE.md` at the repository root. These instructions include:

- ChemROF schema development best practices
- LinkML conventions and workflows  
- Specific commands for generating and testing changes
- Guidelines for creating examples and documentation
- GitHub workflow procedures

Advanced users can submit pull requests to update these instructions to improve the AI's capabilities.

## Best practices for working with the AI agent

### Start simple

For your first request, choose a straightforward, mechanical task where the requirements are clear. For example:

```
@dragon-ai-agent please add a description to the MolecularIon class based on its usage in the schema
```

### Be specific

Provide clear, detailed instructions. Include context about what you want accomplished:

```
@dragon-ai-agent please create an example for the PolyatomicIon class, using sulfate ion as the example, making sure to include the elemental_charge field
```

### Request research when needed

The AI can perform background research using web search:

```
@dragon-ai-agent please research current best practices for representing chemical reactions in semantic models, then propose updates to our Reaction class
```

### Complex tasks

The AI can handle multi-step tasks and will create branches and pull requests:

```
@dragon-ai-agent please analyze which classes are missing descriptions, then add scientifically accurate descriptions to all of them, creating examples for each class as needed
```

## What the AI agent can do

- **Schema analysis**: Examine class hierarchies, find missing descriptions, analyze slot usage
- **Documentation**: Generate or update markdown documentation  
- **Example creation**: Create valid YAML examples following LinkML conventions
- **Code generation**: Write scripts for schema manipulation or validation
- **Research**: Look up scientific information to ensure accuracy
- **Git operations**: Create branches, commit changes, and submit pull requests
- **Testing**: Run validation tests and fix issues

## Troubleshooting

### No response from the agent

- Check that you're an authorized controller
- Ensure you used the exact format: `@dragon-ai-agent please`
- Verify the repository has GitHub Actions enabled

### Timeouts or incomplete responses

- Break large tasks into smaller steps
- Ask the AI to create an initial PR with partial work, then continue iterating

### Debugging failures

1. Go to the "Actions" tab in GitHub
2. Find the workflow run triggered by your request  
3. Check the logs for error messages
4. The AI agent will typically comment on the issue if it encounters problems

## Getting help

If you encounter issues or need guidance:

1. Create a new issue describing the problem
2. Tag @cmungall for assistance
3. Include relevant error messages or unexpected behavior details

The AI agent is designed to be helpful and safe, but it's always learning and improving. Your feedback helps make it more effective for ChemROF development tasks.
