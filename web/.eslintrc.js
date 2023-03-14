module.exports = {
  root: true,
  env: {
    node: true
  },
  'extends': [
    'plugin:vue/essential',
    '@vue/standard'
  ],
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    "object-curly-spacing":"off",
    'block-spacing': "off",
    'object-property-newline': "off",
    eqeqeq: ["error", "always", { null: "ignore" }], // 要求使用 === 和 !==
    "no-redeclare": "error", // 禁止多次声明同一变量
    "no-label-var": "error", // 禁用与变量同名的标签
    "no-unused-vars": "error", // 禁止出现未使用过的变量
    "no-use-before-define": "error", // 禁止在变量定义之前使用它们

    // Stylistic Issues
    semi: ["off", "never"], // 要求或禁止使用分号代替 ASI ["always" (默认) 要求在语句末尾使用分号]
    "semi-spacing": ["error", { before: false, after: true }], // 强制分号之前和之后使用一致的空格
    "array-bracket-spacing": ["error", "never"], // 强制数组方括号中使用一致的空格
    "comma-dangle": ["off", "never"], // 要求或禁止末尾逗号 [never,禁止]
  },
  parserOptions: {
    parser: 'babel-eslint'
  },
  overrides: [
    {
      files: [
        '**/__tests__/*.{j,t}s?(x)',
        '**/tests/unit/**/*.spec.{j,t}s?(x)'
      ],
      env: {
        jest: true
      }
    }
  ]
}
