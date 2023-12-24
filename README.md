# pychatml

The `pychatml` package allows you to convert chat interfaces from and to the ChatML format.

## Installation

You can install the `pychatml` package using pip:

```shell
pip install pychatml
```

## What

Makes it easy to integrate between different chat formats and models.

```python
import pychatml

PROMPT = """[INST] Hi, how are you? [/INST] Good thanks! 
[INST] Can you help me with this math program? [/INST]"""

pychatml.llama2.to_chatml(PROMPT)
```
```json
[
    {"role": "user", "content": "Hi, how are you?"},
    {"role": "assistant", "content": "Good thanks!"},
    {"role": "user", "content": "Can you help me with this math program?"},
]
```

#### Supported formats


 - [x] Llama 2
 - [x] Anthropic
 - [x] Alpaca
 - [ ] Vicuna/ShareGPT

## Why?

![Motivation tweet](https://github.com/deployradiant/pychatml/assets/6087389/003d8898-d647-46d3-90cb-0051a8860519)
https://github.com/OpenAccess-AI-Collective/axolotl/pull/982

## Questions?

Create an issue or discussion in this repository.

Or, reach out to our team! [@jakob_frick](https://twitter.com/frick_jakob/), [@__anjor](https://twitter.com/__anjor), [@maxnajork](https://twitter.com/maxnajork) on X or [team@radiantai.com](mailto:team@radiantai.com).

## Contributing Guidelines

Thank you for your interest in contributing to our project! Before you begin writing code, it would be helpful if you read these guidelines. Following them will make the contribution process easier and more efficient for everyone involved.

Please note that the project is released with an [MIT License](https://opensource.org/licenses/MIT).

### How to contribute

Firstly, ensure you have forked the repository and are working on a branch that is based off of our 'main' branch. If you're unsure about how to do this, there are many guides available online that will help.

Then follow these steps:
  1. **Bugs**: Describe bugs by creating a new issue. Explain what you expected to see, what you saw instead, steps to reproduce it, and any additional context or screenshots that might be helpful.
  2. **Feature requests**: Propose features by opening a new issue. Explain what the feature should do, how it would be used, and why you believe it would be a useful addition.
  3. **Pull Requests**: Fix or add functionality to the project by making changes to the codebase yourself. Ensure that your code is following the coding standards outlined in the next section and make sure all tests pass before submitting a PR.

### Community

We aim to maintain a welcoming and respectful community. Keep all discussions on topic and refrain from rude or inappropriate behavior. Keep in mind that this a place where people come to learn and share, so please respect their efforts.

### Submitting a Pull Request

Before you submit your pull request consider the following guidelines:

  - Try to make your pull request as small as possible. The quicker it can be reviewed, the quicker it can be merged!
  - Include reasoning for your changes, this makes it a lot easier to review
  - If your PR resolves an open issue(s), list them in your PR comment

That's it! You're ready to go. Thanks again for contributing to this project.
