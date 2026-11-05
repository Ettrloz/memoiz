/** @type {import('prettier').Config} */
module.exports = {
  printWidth: 100,
  semi: true,
  singleQuote: true,
  jsxSingleQuote: false,
  arrowParens: 'avoid',
  trailingComma: 'none',
  plugins: ['prettier-plugin-jinja-template'],
  overrides: [
    {
      files: ['**/*.{css,scss}'],
      options: {
        singleQuote: false
      }
    },
    {
      files: ['**/*.html'],
      options: {
        parser: 'jinja-template'
      }
    }
  ]
};
