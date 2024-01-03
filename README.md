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
from pychatml.llama2_converter import Llama2

PROMPT = """[INST] Hi, how are you? [/INST] Good thanks!
[INST] Can you help me with this math program? [/INST]"""

converter = Llama2()

converter.to_chatml(PROMPT)
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
 - [x] Vicuna/ShareGPT (from https://github.com/lm-sys/FastChat/blob/e67b21dcbde91a5ad9740b081c59c433093f54da/fastchat/conversation.py#L394C1-L404C2)

## Why?

![Motivation tweet](https://github.com/deployradiant/pychatml/assets/6087389/003d8898-d647-46d3-90cb-0051a8860519)
https://github.com/OpenAccess-AI-Collective/axolotl/pull/982

## Questions?

Create an issue or discussion in this repository.

Or, reach out to our team! [@jakob_frick](https://twitter.com/frick_jakob/), [@__anjor](https://twitter.com/__anjor), [@maxnajork](https://twitter.com/maxnajork) on X or [team@radiantai.com](mailto:team@radiantai.com).

## How to create a new release

A new release will automatically be published to pypi. For this to happen you need to
- update the version specificed in `setup.py`
- create a `git tag` with the version you want to release and push it via `git push --tags`
- create a new release in Github

A Github action will automatically publish the new version to pypi.

## Contributing Guidelines

Thank you for your interest in contributing to our project! Before you begin writing code, it would be helpful if you read these [contributing guidelines](CONTRIBUTING.md). Following them will make the contribution process easier and more efficient for everyone involved.

Please note that the project is released with an [MIT License](https://opensource.org/licenses/MIT).


