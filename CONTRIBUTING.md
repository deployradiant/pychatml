# Contributing Guidelines

## How to contribute

Firstly, ensure you have forked the repository and are working on a branch that is based off of our 'main' branch. If you're unsure about how to do this, there are many guides available online that will help.

Then follow these steps:
1. **Bugs**: Describe bugs by creating a new issue. Explain what you expected to see, what you saw instead, steps to reproduce it, and any additional context or screenshots that might be helpful.
2. **Feature requests**: Propose features by opening a new issue. Explain what the feature should do, how it would be used, and why you believe it would be a useful addition.
3. **Pull Requests**: Fix or add functionality to the project by making changes to the codebase yourself. Ensure that your code is following the coding standards outlined in the next section and make sure all tests pass before submitting a PR.


## Adding a new format

If you want to add a new format, you can do so by creating a new file in the `pychatml` directory. The file should be named after the format you are adding. For example, if you are adding a new format called `foo`, you should create a file called `foo.py`.
Implement the `AbstractConverter` class in this file. You can use the `Llama2` class as an example.

## Community

We aim to maintain a welcoming and respectful community. Keep all discussions on topic and refrain from rude or inappropriate behavior. Keep in mind that this a place where people come to learn and share, so please respect their efforts.

## Submitting a Pull Request

Before you submit your pull request consider the following guidelines:

- Try to make your pull request as small as possible. The quicker it can be reviewed, the quicker it can be merged!
- Include reasoning for your changes, this makes it a lot easier to review
- If your PR resolves an open issue(s), list them in your PR comment

That's it! You're ready to go. Thanks again for contributing to this project.
