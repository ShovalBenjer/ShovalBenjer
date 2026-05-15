# Contributing to Gastown Projects

Thank you for your interest in contributing to Gastown! This guide will help you get started with contributing to our projects.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Pull Request Process](#pull-request-process)
- [Project Structure](#project-structure)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Questions or Help](#questions-or-help)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. Please be kind, constructive, and collaborative.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/REPO_NAME.git`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Set up development environment (see [Development Setup](#development-setup))

## Development Setup

### Prerequisites

- Git 2.30+
- Node.js 18+ (for tooling)
- Python 3.10+ (for agent execution)
- Docker (optional, for containerized development)

### Installation

```bash
# Clone and enter repository
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
cd REPO_NAME

# Install dependencies
npm install  # or yarn install

# Link for local development
npm link
```

### Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Required variables:
- `GASTOWN_API_KEY` - For authentication with Gastown services
- `DATABASE_URL` - For local development database

## How to Contribute

### Finding Issues

- Check the [Issues](https://github.com/ShovalBenjer/REPO_NAME/issues) tab for open issues
- Look for `good first issue` labels if you're new to the project
- If you have a feature idea, open a new issue to discuss it first

### Types of Contributions

- **Bug fixes** - Fix something that's broken
- **Features** - Add new functionality
- **Documentation** - Improve or add documentation
- **Tests** - Add or improve test coverage
- **Examples** - Create example code or tutorials

## Pull Request Process

1. **Before you start**: Comment on the issue to let others know you're working on it
2. **Create your branch**: Use descriptive names like `feature/add-user-auth` or `fix/login-error`
3. **Make changes**: Follow the coding standards
4. **Write tests**: Ensure your changes are tested
5. **Update docs**: Update documentation if needed
6. **Commit**: Use clear, descriptive commit messages
7. **Push**: Push to your fork
8. **PR**: Open a pull request against `main`

### Commit Messages

Use clear, descriptive commit messages:

```
feat: add user authentication middleware
fix: resolve memory leak in scheduler
docs: update API documentation for /users endpoint
chore: update dependencies
```

## Project Structure

```
.
├── src/                # Source code
│   ├── agents/         # Gastown agents
│   ├── tools/          # Available tools
│   └── utils/          # Utility functions
├── docs/               # Documentation
├── tests/              # Test files
├── .github/            # GitHub workflows
└── CONTRIBUTING.md     # This file
```

## Coding Standards

### JavaScript/TypeScript

- Use async/await over promises
- Prefer `const` over `let`
- Use 2-space indentation
- Write JSDoc comments for public functions

### Python

- Follow PEP 8
- Use type hints
- Prefer f-strings for string formatting
- Document with docstrings

### General

- Write self-documenting code
- Keep functions under 50 lines
- Use meaningful variable names
- Don't commit secrets or API keys

## Testing

Run tests with:

```bash
npm test      # Run all tests
npm test:watch # Run tests in watch mode
npm test:coverage # Run with coverage
```

### Writing Tests

- Place test files in `tests/` directory
- Name test files with `.test.ts` extension
- Use descriptive test names
- Aim for >80% coverage on new code

## Documentation

Documentation lives in the `docs/` directory and inline in code.

When adding features:
- Update inline comments if needed
- Add/update README sections
- Include usage examples

## Questions or Help

- Open a [Discussion](https://github.com/ShovalBenjer/REPO_NAME/discussions) for questions
- Join our Vancouver tech community Slack: #gastown channel
- Email: shovalb9@gmail.com

## Recognition

Contributors are recognized in:
- Release notes
- Contributors file (if present)
- Community showcase

Thank you for contributing to Gastown! 🎉